"""
Generate markdown templates for ChatGPT GPTs by downloading and parsing their metadata.

By Elias Bachaalany

Usage:
    gen_template.py <gpt_url|gpt_id|g-prefixed_id> [--debug]
    gen_template.py @response_file.txt [--debug]
"""
import re
import json
import os
import sys
import argparse
import requests
from collections import namedtuple

# Named tuple for generate_template return value
GenerateTemplateResult = namedtuple('GenerateTemplateResult', 
    ['template', 'short_url', 'gpt_id', 'parser'])

# Global template string
TEMPLATE = """GPT URL: https://chatgpt.com/g/{short_url}

GPT logo: <img src="{profile_pic}" width="100px" />

GPT Title: {title}

GPT Description: {description} - By {author_display_name}

GPT instructions:

```markdown

```"""

# ----------------------------------------------------------
def parse_gpt_id(url):
    """
    Parse the GPT ID from a ChatGPT URL
    
    Args:
        url (str): Full ChatGPT URL like https://chatgpt.com/g/g-VgbIr9TQQ-ida-pro-c-sdk-and-decompiler
    
    Returns:
        str or None: The GPT ID (e.g., 'VgbIr9TQQ') or None if not found
    """
    # Pattern to match g- followed by 9 characters
    pattern = r'/g/g-([a-zA-Z0-9]{9})'
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)
    return None

# ----------------------------------------------------------
# Compile regex to extract streamController.enqueue arguments
_ENQUEUE_RE = re.compile(
    r'window\.__reactRouterContext\.streamController\.enqueue\(\s*'       # find the call
    r'(?P<q>["\'])'                         # capture whether it's " or '
    r'(?P<raw>(?:\\.|(?!\1).)*?)'           # any escaped-char or char not the opening quote
    r'(?P=q)\s*'                            # matching closing quote
    r'\)',
    flags=re.DOTALL
)

# ----------------------------------------------------------
def extract_enqueue_args(html_text, decode_escapes=True):
    """
    Scans html_text for all streamController.enqueue(...) calls,
    returns a list of the raw string-literals inside the quotes.
    """
    args = []
    for m in _ENQUEUE_RE.finditer(html_text):
        raw = m.group('raw')
        if decode_escapes:
            # Only decode actual escape sequences, not Unicode characters
            # This prevents double-encoding of emojis and other Unicode chars
            try:
                # First try to parse as JSON string to handle escapes properly
                raw = json.loads('"' + raw + '"')
            except:
                # Fallback to simple replacement of common escapes
                raw = raw.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')
        args.append(raw)
    return args


# ----------------------------------------------------------
class CustomGPTParser:
    def __init__(self):
        self._parse_cache = {}  # Cache for parsed data
        self._parsed_items = None  # Store parsed items internally
    
    def parse(self, source, debug: bool = False):
        # Determine if source is a filename or content
        # First check if it could be a file (avoid treating content as filename)
        is_likely_filename = (
            len(source) < 1000 and  # Reasonable filename length
            '|' not in source and  # Filenames don't contain pipes
            os.path.isfile(source)
        )
        
        if is_likely_filename:
            try:
                with open(source, encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                return (False, f"Error reading file: {e}")
        else:
            # Treat as content
            content = source
        
        # Parse the content
        if not (enqueue_args := extract_enqueue_args(content)):
            msg = "No enqueue arguments found in the provided string."
            if debug:
                print(msg)
            return (False, msg)
        
        if not enqueue_args:  # Additional safety check for empty list
            msg = "No enqueue arguments found in the provided string."
            if debug:
                print(msg)
            return (False, msg)
        
        try:
            # Use the argument with the longest length (most likely the Gizmo data)
            s = max(enqueue_args, key=len)  
            data = json.loads(s)
            parsed_items = []
            for item in data:
                if isinstance(item, dict):
                    for k, v in item.items():
                        parsed_items.append((k, v))
                else:
                    if debug:
                        print(f"   {item}  (type: {type(item).__name__})")
                    parsed_items.append(item)
            
            self._parsed_items = parsed_items
            return (True, None)
            
        except json.JSONDecodeError as e:
            return (False, f"JSON decoding error: {e}")
    
    def get_title(self):
        """
        Extract the title of the GPT by finding the item preceding 'description'.
        
        The algorithm walks through items to find 'description', then returns
        the immediately preceding item as the title.
        
        Returns:
            str: The title value or empty string on failure
        """
        # Check cache first
        if 'title' in self._parse_cache:
            return self._parse_cache['title']
        
        # Need parsed items to work with
        if not self._parsed_items:
            return ''
        
        # Convert to list if not already to allow indexing
        items_list = list(self._parsed_items)
        
        # Find 'description' and get the preceding item
        for i, item in enumerate(items_list):
            # Skip tuples
            if isinstance(item, tuple):
                continue
            
            # Found 'description'?
            if item == 'description' and i > 0:
                # Get the previous item as title
                prev_item = items_list[i - 1]
                
                # Make sure it's a string value, not a tuple
                if isinstance(prev_item, str):
                    self._parse_cache['title'] = prev_item
                    return prev_item
        
        # Not found
        return ''
    
    def get_author_display_name(self):
        """
        Extract the author display name by finding the item after 'user-{id}'.
        
        The pattern is:
        - 'user_id' (literal string)
        - 'user-{actual_user_id}' (e.g., 'user-IUwuaeXwGuwv0UoRPaeEqlzs')
        - '{author_display_name}' (e.g., 'Elias Bachaalany')
        
        Returns:
            str: The author display name or empty string on failure
        """
        # Check cache first
        if 'author_display_name' in self._parse_cache:
            return self._parse_cache['author_display_name']
        
        # Need parsed items to work with
        if not self._parsed_items:
            return ''
        
        # Convert to list if not already to allow indexing
        items_list = list(self._parsed_items)
        
        # Find pattern: 'user_id' -> 'user-{id}' -> '{display_name}'
        for i, item in enumerate(items_list):
            # Skip tuples
            if isinstance(item, tuple):
                continue
            
            # Found 'user_id'?
            if item == 'user_id' and i + 2 < len(items_list):
                # Check if next item is a user ID (starts with 'user-')
                next_item = items_list[i + 1]
                if isinstance(next_item, str) and next_item.startswith('user-'):
                    # The item after that should be the display name
                    display_name_item = items_list[i + 2]
                    if isinstance(display_name_item, str):
                        self._parse_cache['author_display_name'] = display_name_item
                        return display_name_item
        
        # Not found
        return ''
    def get_str_value(self, name: str, default: str = None):
        """
        Get a string value by name from the parsed items.
        
        Args:
            name: The key/name to search for
            default: Default value if not found
            
        Returns:
            str: The value associated with the name or default
        """
        # Check cache first
        if name in self._parse_cache:
            return self._parse_cache[name]
        
        # Need parsed items to work with
        if not self._parsed_items:
            return default
        
        # Search through items
        it = iter(self._parsed_items)
        for item in it:
            # Handle tuple items (key-value pairs from dictionaries)
            if isinstance(item, tuple):
                # We don't handle tuple items now
                continue
            
            # Handle flat list items (name followed by value)
            if item == name:
                try:
                    val = next(it)
                    # Cache and return the value
                    self._parse_cache[name] = str(val)
                    return str(val)
                except StopIteration:
                    return default
        
        return default
    
    def clear_cache(self):
        """Clear the internal cache"""
        self._parse_cache.clear()
    
    def get_parsed_items(self):
        """Get the parsed items (for backward compatibility)"""
        return self._parsed_items if self._parsed_items else []
    
    def dump(self, safe_ascii=True):
        """
        Dump all parsed items in a formatted way.
        
        Args:
            safe_ascii (bool): If True, encode non-ASCII characters safely
        
        Returns:
            None (prints to stdout)
        """
        if not self._parsed_items:
            print("No parsed items to dump")
            return
        
        print(f"Dumping {len(self._parsed_items)} parsed items:")
        print("-" * 60)
        
        for item in self._parsed_items:
            if isinstance(item, tuple) and len(item) == 2:
                # Handle key-value pairs from dictionaries
                k, v = item
                if safe_ascii:
                    # Handle Unicode characters safely by encoding to ASCII with replacement
                    k_safe = str(k).encode('ascii', errors='replace').decode('ascii')
                    v_safe = str(v).encode('ascii', errors='replace').decode('ascii')
                    print(f"   {k_safe}: {v_safe}  (type: {type(v).__name__})")
                else:
                    print(f"   {k}: {v}  (type: {type(v).__name__})")
            else:
                # Handle non-tuple items
                if safe_ascii:
                    # Handle Unicode characters safely for non-dict items
                    item_safe = str(item).encode('ascii', errors='replace').decode('ascii')
                    print(f"   {item_safe}  (type: {type(item).__name__})")
                else:
                    print(f"   {item}  (type: {type(item).__name__})")
        
        print("-" * 60)

# ----------------------------------------------------------
def download_page(url: str, out_filename: str = '') -> tuple[bool, object]:
    """
    Download a page using browser-like headers
    
    Args:
        url (str): The full URL to download
        out_filename (str): Optional filename to save to. If empty, no file is written.
    
    Returns:
        tuple[bool, object]: (success, content/error_message)
            - (True, content) if successful
            - (False, error_message) if failed
    """
    # Ensure we have a full URL
    if not url.startswith('http'):
        return (False, "Please provide a full URL starting with http:// or https://")
    
    # Base headers from the sample request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # Remove Accept-Encoding to get uncompressed response
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
        'TE': 'trailers'
    }
    
    try:
        # Create a session to handle cookies and connections properly
        session = requests.Session()
        session.headers.update(headers)
        
        # Make the GET request
        response = session.get(url, timeout=30)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Save to file if filename provided
        if out_filename:
            with open(out_filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
        
        return (True, response.text)
        
    except requests.exceptions.RequestException as e:
        return (False, f"Error downloading page: {e}")
    except Exception as e:
        return (False, f"Unexpected error: {e}")

# ----------------------------------------------------------
def process_gpt_input(input_str):
    """
    Process GPT input which can be:
    - Full URL: https://chatgpt.com/g/g-VgbIr9TQQ-ida-pro-c-sdk-and-decompiler
    - Conversation URL: https://chatgpt.com/g/g-m5lMeGifF-sql-expert-querygpt/c/682cd38c-ca8c-800d-b6e2-33b8ba763824
    - GPT ID: VgbIr9TQQ
    - Prefixed GPT ID: g-VgbIr9TQQ
    
    Returns:
        tuple: (full_url, gpt_id)
    """
    # Check if it's a full URL
    if input_str.startswith('https://') or input_str.startswith('http://'):
        gpt_id = parse_gpt_id(input_str)
        if not gpt_id:
            raise ValueError(f"Could not parse GPT ID from URL: {input_str}")
        
        # If it's a conversation URL (contains /c/), extract the base GPT URL
        if '/c/' in input_str:
            # Extract the GPT part before /c/
            base_url = input_str.split('/c/')[0]
            return (base_url, gpt_id)
        
        return (input_str, gpt_id)
    
    # Check if it's a prefixed GPT ID (g-XXXXXXXXX)
    if input_str.startswith('g-') and len(input_str) >= 11:
        # Extract just the 9-character ID after 'g-'
        gpt_id = input_str[2:11]  # Get exactly 9 characters after 'g-'
        url = f"https://chatgpt.com/g/{input_str}"
        return (url, gpt_id)
    
    # Assume it's a bare GPT ID (9 characters)
    if len(input_str) == 9:
        url = f"https://chatgpt.com/g/g-{input_str}"
        return (url, input_str)
    
    raise ValueError(f"Invalid GPT input format: {input_str}")

def generate_template(url, debug=False, dump=False):
    """
    Download and parse GPT data, then generate markdown template
    
    Args:
        url: Full GPT URL
        debug: Whether to save debug files (HTML and dump)
        dump: Whether to print parsed items to console
    
    Returns:
        tuple: (success, result_or_error)
            - (True, GenerateTemplateResult) if successful
            - (False, error_message) if failed
    """
    print(f"[DOWNLOAD] Fetching page from: {url}")
    # Download the page
    save_file = None
    if debug:
        save_file = "debug_download.html"
        print(f"[DEBUG] Will save HTML to: {save_file}")
    
    success, content = download_page(url, save_file)
    if not success:
        return (False, f"Download failed: {content}")
    
    print(f"[DOWNLOAD] Successfully downloaded {len(content)} bytes")
    
    # Parse the content
    print(f"[PARSE] Parsing GPT data...")
    parser = CustomGPTParser()
    success, error = parser.parse(content)
    if not success:
        return (False, f"Parsing failed: {error}")
    
    print(f"[PARSE] Successfully parsed {len(parser.get_parsed_items())} items")
    
    # Save dump if debug mode
    if debug:
        from io import StringIO
        old_stdout = sys.stdout
        sys.stdout = buffer = StringIO()
        parser.dump(safe_ascii=True)
        dump_content = buffer.getvalue()
        sys.stdout = old_stdout
        
        dump_file = "debug_dump.txt"
        with open(dump_file, 'w', encoding='utf-8') as f:
            f.write(dump_content)
        print(f"[DEBUG] Saved parsed data dump to: {dump_file}")
    
    # Extract required fields
    print(f"[EXTRACT] Extracting GPT metadata...")
    short_url = parser.get_str_value('short_url', 'UNKNOWN')
    profile_pic = parser.get_str_value('profile_picture_url', '')
    title = parser.get_title()
    description = parser.get_str_value('description', '')
    author_display_name = parser.get_author_display_name()
    
    print(f"[EXTRACT] Found:")
    print(f"  - Short URL: {short_url}")
    print(f"  - Title: {title}")
    print(f"  - Author: {author_display_name}")
    try:
        print(f"  - Description: {description[:50]}..." if len(description) > 50 else f"  - Description: {description}")
    except UnicodeEncodeError:
        # Handle special characters that can't be printed to console
        safe_desc = description.encode('ascii', errors='replace').decode('ascii')
        print(f"  - Description: {safe_desc[:50]}..." if len(safe_desc) > 50 else f"  - Description: {safe_desc}")
    print(f"  - Profile Pic: {'Yes' if profile_pic else 'No'}")
    
    # Dump parsed items if requested
    if dump:
        print("\n[DUMP] Parsed items:")
        parser.dump(safe_ascii=False)
    
    # Generate template
    template = TEMPLATE.format(
        short_url=short_url,
        profile_pic=profile_pic,
        title=title,
        description=description,
        author_display_name=author_display_name
    )
    
    # Extract GPT ID from short_url (remove 'g-' prefix if it exists)
    gpt_id = short_url[2:] if short_url.startswith('g-') else short_url
    
    return (True, GenerateTemplateResult(template, short_url, gpt_id, parser))

def process_response_file(filename, debug=False, dump=False):
    """
    Process a response file containing multiple GPT URLs/IDs
    
    Args:
        filename: Path to the response file
        debug: Whether to save debug files
        dump: Whether to dump parsed items
    
    Returns:
        tuple: (success_count, error_count)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading response file: {e}")
        return (0, 1)
    
    # Process each non-empty line
    inputs = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
    
    if not inputs:
        print(f"No valid inputs found in {filename}")
        return (0, 0)
    
    print(f"\n{'=' * 70}")
    print(f"PROCESSING RESPONSE FILE: {filename}")
    print(f"Found {len(inputs)} items to process")
    print(f"{'=' * 70}")
    
    success_count = 0
    error_count = 0
    
    for i, input_str in enumerate(inputs, 1):
        print(f"\n[ITEM {i}/{len(inputs)}] Processing: {input_str}")
        print("-" * 60)
        
        try:
            # Process input
            url, gpt_id = process_gpt_input(input_str)
            print(f"[PARSED] Full URL: {url}")
            print(f"[PARSED] GPT ID: {gpt_id}")
            
            # Generate template
            success, result = generate_template(url, debug, dump)
            if success:
                filename = f"{result.gpt_id}.md"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(result.template)
                print(f"[SUCCESS] Template saved to: {filename}")
                
                # Save dump file if requested
                if dump:
                    dump_filename = f"{result.gpt_id}.txt"
                    from io import StringIO
                    old_stdout = sys.stdout
                    sys.stdout = buffer = StringIO()
                    result.parser.dump(safe_ascii=True)
                    dump_content = buffer.getvalue()
                    sys.stdout = old_stdout
                    
                    with open(dump_filename, 'w', encoding='utf-8') as f:
                        f.write(dump_content)
                    print(f"[SUCCESS] Dump saved to: {dump_filename}")
                
                success_count += 1
            else:
                print(f"[FAILED] Error: {result}")
                error_count += 1
                
        except Exception as e:
            print(f"[ERROR] Exception: {e}")
            error_count += 1
    
    print(f"\n{'=' * 70}")
    print(f"RESPONSE FILE COMPLETE")
    print(f"Success: {success_count}, Errors: {error_count}")
    print(f"{'=' * 70}")
    
    return (success_count, error_count)

def main():
    parser = argparse.ArgumentParser(description='Generate markdown template for ChatGPT GPTs')
    parser.add_argument('input', nargs='?', help='GPT URL, GPT ID, g-prefixed GPT ID, or @response_file')
    parser.add_argument('--debug', action='store_true', help='Save debug files (HTML and dump)')
    parser.add_argument('--dump', action='store_true', help='Save parsed names and values to .txt file')
    
    args = parser.parse_args()
    
    # Check if input was provided
    if not args.input:
        parser.print_help()
        return 1
    
    try:
        # Check if input is a response file
        if args.input.startswith('@'):
            # Process response file
            filename = args.input[1:]  # Remove the @ prefix
            success_count, error_count = process_response_file(filename, args.debug, args.dump)
            return 0 if error_count == 0 else 1
        else:
            # Process single input
            print(f"\n[INPUT] Processing: {args.input}")
            url, gpt_id = process_gpt_input(args.input)
            print(f"[PARSED] Full URL: {url}")
            print(f"[PARSED] GPT ID: {gpt_id}")
            
            # Generate template
            success, result = generate_template(url, args.debug, args.dump)
            if success:
                # Save to file
                filename = f"{result.gpt_id}.md"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(result.template)
                print(f"Template saved to: {filename}")
                
                # Save dump file if requested
                if args.dump:
                    dump_filename = f"{result.gpt_id}.txt"
                    from io import StringIO
                    old_stdout = sys.stdout
                    sys.stdout = buffer = StringIO()
                    result.parser.dump(safe_ascii=True)
                    dump_content = buffer.getvalue()
                    sys.stdout = old_stdout
                    
                    with open(dump_filename, 'w', encoding='utf-8') as f:
                        f.write(dump_content)
                    print(f"Dump saved to: {dump_filename}")
                
                # Also print the template
                print("\nGenerated template:")
                print("=" * 50)
                try:
                    print(result.template)
                except UnicodeEncodeError:
                    # Handle special characters that can't be printed to console
                    safe_template = result.template.encode('ascii', errors='replace').decode('ascii')
                    print(safe_template)
            else:
                print(f"Error: {result}")
                return 1
            
            return 0
            
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())