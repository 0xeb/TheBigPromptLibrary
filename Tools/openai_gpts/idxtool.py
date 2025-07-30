"""
idxtool is a script is used to perform various GPT indexing and searching tasks

- Find a GPT file by its ID or full ChatGPT URL or via a file containing a list of GPT IDs.
- Rename all the GPTs to include their ChatGPT/g/ID in the filename.
- Generate TOC
- etc.
"""

import sys, os, argparse
from typing import Tuple
from urllib.parse import quote

import gptparser
from gptparser import enum_gpts, parse_gpturl, enum_gpt_files, get_prompts_path
import gen_gpt_templ

TOC_FILENAME = os.path.abspath(os.path.join(get_prompts_path(), '..', 'README.md'))
TOC_GPT_MARKER_LINE = '## ChatGPT GPT instructions'

def rename_gpts():
    effective_rename = nb_ok = nb_total = 0

    for ok, gpt in enum_gpts():
        nb_total += 1
        if not ok or not (id := gpt.id()):
            print(f"[!] {gpt.filename}")
            continue
        # Skip files with correct prefix
        basename = os.path.basename(gpt.filename)
        if basename.startswith(f"{id.id}_"):
            nb_ok += 1
            continue
        effective_rename += 1

        # New full file name with ID prefix
        new_fn = os.path.join(os.path.dirname(gpt.filename), f"{id.id}_{basename}")
        print(f"[+] {basename} -> {os.path.basename(new_fn)}")
        if os.system(f"git mv \"{gpt.filename}\" \"{new_fn}\"") == 0:
            nb_ok += 1
            continue

        # If git mv failed, then try os.rename
        try:
            os.rename(gpt.filename, new_fn)
            nb_ok += 1
            continue
        except OSError as e:
            print(f"Rename error: {e.strerror}")

    msg = f"Renamed {nb_ok} out of {nb_total} GPT files."
    ok = nb_ok == nb_total
    if effective_rename == 0:
        msg = f"All {nb_total} GPT files were already renamed. No action taken."
        print(msg)

    return (ok, msg)


def parse_gpt_file(filename) -> Tuple[bool, str]:
    ok, gpt = gptparser.GptMarkdownFile.parse(filename)
    if ok:
        file_name_without_ext = os.path.splitext(os.path.basename(filename))[0]
        dst_fn = os.path.join(
            os.path.dirname(filename),
            f"{file_name_without_ext}.new.md")
        gpt.save(dst_fn)
    else:
        print(gpt)

    return (ok, gpt)


def rebuild_toc(toc_out: str = '') -> Tuple[bool, str]:
    """
    Rebuilds the table of contents GPT custom instructions file by reading all the GPT files in the CustomInstructions/ChatGPT directory.
    """
    if not toc_out:
        print(f"Rebuilding Table of Contents GPT custom instructions in place")
    else:
        print(f"Rebuilding Table of Contents GPT custom instructions to '{toc_out}'")

    toc_in = TOC_FILENAME
    if not toc_out:
        toc_out = toc_in

    if not os.path.exists(toc_in):
        return (False, f"TOC File '{toc_in}' does not exist.")

    # Read the TOC file and find the marker line for the GPT instructions
    out = []
    marker_found = False
    with open(toc_in, 'r', encoding='utf-8') as file:
        for line in file:
            out.append(line)
            if line.startswith(TOC_GPT_MARKER_LINE):
                out.append('\n')
                marker_found = True
                break
    if not marker_found:
        return (False, f"Could not find the marker '{TOC_GPT_MARKER_LINE}' in '{toc_in}'. Please revert the TOC file and try again.")

    # Write the TOC file all the way up to the marker line
    try:
        ofile = open(toc_out, 'w', encoding='utf-8')
    except:
        return (False, f"Failed to open '{toc_out}' for writing.")

    # Count GPTs
    enumerated_gpts = list(enum_gpts())
    nb_ok = sum(1 for ok, gpt in enumerated_gpts if ok and gpt.id())    

    # Write the marker line and each GPT entry
    out.append(f"There are {nb_ok} GPTs total:\n\n")

    nb_ok = nb_total = 0
    gpts = []
    for ok, gpt in enumerated_gpts:
        nb_total += 1
        if ok:
            if gpt_id := gpt.id():
                nb_ok += 1
                gpts.append((gpt_id, gpt))
            else:
                print(f"[!] No ID detected: {gpt.filename}")
        else:
            print(f"[!] {gpt}")

    # Consistently sort the GPTs by ID and GPTs title
    def gpts_sorter(key):
        gpt_id, gpt = key
        version = f"{gpt.get('version')}" if gpt.get('version') else ''
        return f"{gpt.get('title')}{version} (id: {gpt_id.id}))"
    gpts.sort(key=gpts_sorter)

    for id, gpt in gpts:
        file_link = f"./ChatGPT/{quote(os.path.basename(gpt.filename))}"
        version = f" {gpt.get('version')}" if gpt.get('version') else ''
        out.append(f"- [{gpt.get('title')}{version} (id: {id.id})]({file_link})\n")

    ofile.writelines(out)
    ofile.close()
    msg = f"Generated TOC with {nb_ok} out of {nb_total} GPTs."

    ok = nb_ok == nb_total
    if ok:
        print(msg)
    return (ok, msg)

def make_template(input_str, verbose=True):
    """Creates a GPT template file from a ChatGPT URL/ID by downloading metadata"""
    try:
        # Process the input to handle URLs, IDs, conversation URLs, etc.
        url, gpt_id = gen_gpt_templ.process_gpt_input(input_str)
        
        if verbose:
            print(f"[PARSED] Full URL: {url}")
            print(f"[PARSED] GPT ID: {gpt_id}")
        
        # Use gen_gpt_templ to generate the template with actual metadata
        success, result = gen_gpt_templ.generate_template(url, debug=False, dump=False)
        
        if not success:
            msg = f"Failed to generate template: {result}"
            if verbose:
                print(msg)
            return (False, msg)
        
        # Extract the template content and gpt_id from the result
        template_content = result.template
        gpt_id = result.gpt_id
        
        # Save to the current working directory with the proper filename
        filename = f"{gpt_id}.md"
        
        # Check if file already exists
        if os.path.exists(filename):
            msg = f"File '{filename}' already exists."
            if verbose:
                print(msg)
            return (False, msg)
        
        # Write the template content
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(template_content)
        
        msg = f"Created template '{filename}' for URL '{url}'"
        if verbose:
            print(msg)
        return (True, msg)
        
    except Exception as e:
        msg = f"Error creating template: {str(e)}"
        if verbose:
            print(msg)
        return (False, msg)

def find_gptfile(keyword, verbose=True):
    """Find a GPT file by its ID or full ChatGPT URL
    The ID can be prefixed with '@' to indicate a file containing a list of GPT IDs.
    """
    keyword = keyword.strip()
    # Response file with a set of GPT IDs
    if keyword.startswith('@'):
        with open(keyword[1:], 'r', encoding='utf-8') as file:
            ids = set()
            for line in file:
                line = line.strip()
                # Skip comments
                if line.startswith('#'):
                    continue
                # If the line is a GPT URL, then extract the ID
                if gpt_info := parse_gpturl(line):
                    ids.add(gpt_info.id)
                    continue
                # If not a GPT URL, then it's a GPT ID
                ids.add(line)
    elif gpt_info := parse_gpturl(keyword):
        # A single GPT URL
        ids = {gpt_info.id}
    else:
        # A single GPT ID
        ids = {keyword}

    if verbose:
        print(f'Looking for GPT files with IDs: {", ".join(ids)}')
    matches = []
    for id, filename in enum_gpt_files():
        if id in ids:
            if verbose:
                print(filename)
            matches.append((id, filename))

    return matches


def main():
    parser = argparse.ArgumentParser(description='idxtool: A GPT indexing and searching tool for the TBPL repo')

    parser.add_argument('--toc', nargs='?', const='', type=str, help='Rebuild the table of contents of custom GPTs')
    parser.add_argument('--find-gpt', type=str, help='Find a GPT file by its ID or full ChatGPT URL')
    parser.add_argument('--template', type=str, help='Creates a GPT template file from a ChatGPT URL, GPT ID, or g-prefixed ID')
    parser.add_argument('--parse-gptfile', type=str, help='Parses a GPT file name')
    parser.add_argument('--rename', action='store_true', help='Rename the GPT file names to include their GPT ID')

    # Handle arguments
    ok = True

    args = parser.parse_args()
    
    # Check if no arguments were provided
    # For --toc, we need to check if it's None (not provided) vs '' (provided without value)
    args_dict = vars(args)
    if not any(v is not None and v is not False for v in args_dict.values()):
        parser.print_help()
        return 0
    
    if args.parse_gptfile:
        ok, err = parse_gpt_file(args.parse_gptfile)
        if not ok:
            print(err)
    elif args.toc is not None:
        ok, err = rebuild_toc(args.toc)
        if not ok:
            print(err)
    elif args.find_gpt:
        find_gptfile(args.find_gpt)
    elif args.template:
        ok, _ = make_template(args.template)
    elif args.rename:
        ok, err = rename_gpts()
        if not ok:
            print(err)

    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
