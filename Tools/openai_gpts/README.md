# Custom GPTs scripts and tools

This directory contains utilities for working with ChatGPT Custom GPTs in TheBigPromptLibrary:

- **idxtool.py** - GPT indexing and searching tool
- **gen_gpt_templ.py** - Generate markdown templates for ChatGPT GPTs by downloading and parsing their metadata
- **oneoff.py** - One-off operations on GPT files (e.g., batch reformatting)

## idxtool

The `idxtool` script is a Custom GPT indexing and searching tool used in TheBigPromptLibrary.

### Command line

```
usage: idxtool.py [-h] [--toc [TOC]] [--find-gpt FIND_GPT] 
                  [--template TEMPLATE] [--parse-gptfile PARSE_GPTFILE] 
		  [--rename]

idxtool: A GPT indexing and searching tool for the CSP repo

options:
  -h, --help            show this help message and exit
  --toc [TOC]           Rebuild the table of contents of GPT custom instructions
  --find-gpt FIND_GPT   Find a GPT file by its ID or full ChatGPT URL
  --template TEMPLATE   Creates an empty GPT template file from a ChatGPT URL
  --parse-gptfile PARSE_GPTFILE
                        Parses a GPT file name
  --rename              Rename the GPT file names to include their GPT ID
```

### Features

- Rebuild TOC: Use `--toc` to rebuild the table of contents for GPT custom instructions.
- Find GPT File: Use `--find-gpt [GPTID or Full ChatGPT URL or a response file with IDs/URLs]` to find a GPT by its ID or URL.
- Rename GPT: Use `--rename` to rename all the GPTs to include their GPTID as prefix.
- Create a starter template GPT file: Use `--template [Full ChatGPT URL]` to create a starter template GPT file.
- Help: Use `--help` to display the help message and usage instructions.

### Example

To rebuild the custom GPTs files, run:

```bash
python idxtool.py --toc
```

To find a GPT by its ID, run:

```bash
python idxtool.py --find-gpt 3rtbLUIUO
```

or by URL:
  
```bash
python idxtool.py --find-gpt https://chat.openai.com/g/g-svehnI9xP-retro-adventures
```

Additionally, you can have a file with a list of IDs or URLs and pass it to the `--find-gpt` option:

```bash
python idxtool.py --find-gpt @gptids.txt
```

(note the '@' symbol).

The `gptids.txt` file contains a list of IDs or URLs, one per line:

```text
3rtbLUIUO
https://chat.openai.com/g/g-svehnI9xP-retro-adventures
#vYzt7bvAm
w2yOasK1r
waDWNw2J3
```

## gen_gpt_templ

The `gen_gpt_templ` script generates markdown templates for ChatGPT GPTs by downloading and parsing their metadata from the ChatGPT website.

### Command line

```bash
usage: gen_gpt_templ.py [-h] [--debug] [--dump] [input]

Generate markdown template for ChatGPT GPTs

positional arguments:
  input       GPT URL, GPT ID, g-prefixed GPT ID, or @response_file

options:
  -h, --help  show this help message and exit
  --debug     Save debug files (HTML and dump)
  --dump      Save parsed names and values to .txt file
```

### Features

- Downloads GPT metadata from ChatGPT URLs
- Parses GPT information including title, description, author, and profile picture
- Generates markdown templates with GPT metadata
- Supports multiple input formats:
  - Full ChatGPT URL: `https://chatgpt.com/g/g-VgbIr9TQQ-ida-pro-c-sdk-and-decompiler`
  - Conversation URL: `https://chatgpt.com/g/g-m5lMeGifF-sql-expert-querygpt/c/682cd38c-ca8c-800d-b6e2-33b8ba763824`
  - GPT ID: `VgbIr9TQQ`
  - Prefixed GPT ID: `g-VgbIr9TQQ`
  - Response file: `@gptids.txt` (processes multiple GPTs from a file)

### Examples

Generate template for a single GPT:

```bash
python gen_gpt_templ.py https://chatgpt.com/g/g-VgbIr9TQQ-ida-pro-c-sdk-and-decompiler
```

Process multiple GPTs from a file:

```bash
python gen_gpt_templ.py @gptids.txt
```

Generate template with debug output:

```bash
python gen_gpt_templ.py g-VgbIr9TQQ --debug --dump
```

## Differences between idxtool and gen_gpt_templ

### idxtool --template
- Uses gen_gpt_templ internally to download actual GPT metadata from ChatGPT
- Creates templates with real GPT information (title, description, author, logo)
- Generates properly named files (`{gpt_id}.md`) without RENAMEME suffix
- Simpler interface for basic template generation within the idxtool workflow

### gen_gpt_templ
- Full-featured standalone tool with additional capabilities:
  - `--dump` flag to save all parsed metadata to .txt file
  - `--debug` flag to save HTML and debug information
  - Batch processing with @response_file for multiple GPTs
  - More detailed console output showing download and parsing progress
  - Can be used as a module by other tools (like idxtool)

Use `idxtool --template` when you need a quick template as part of your GPT file management workflow. Use `gen_gpt_templ` directly when you need the advanced features like metadata dumping or batch processing.

## oneoff

The `oneoff` script performs one-off operations on GPT files, primarily batch processing tasks.

### Features

- **Reformat GPT files**: Reformats all GPT markdown files in a source directory and saves them to a destination directory
- Validates GPT file structure during processing
- Preserves GPT metadata (ID, name) during reformatting

### Usage

The script is designed for batch operations. Currently supports:

1. **Batch reformatting**: Process all `.md` files in a source directory, reformat them according to the standard GPT markdown structure, and save to a destination directory.

Example usage in code:

```python
from oneoff import reformat_gpt_files

success, message = reformat_gpt_files("source_gpts/", "formatted_gpts/")
print(message)
```

## License

This tool is open-sourced under the GNU General Public License (GPL). Under this license, you are free to use, modify, and redistribute this software, provided that all copies and derivative works are also licensed under the GPL.

For more details, see the [GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.html).
