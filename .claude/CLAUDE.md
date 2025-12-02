# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a collection repository for LLM system prompts, custom GPT instructions, jailbreak prompts, and instruction protection techniques. The content is primarily markdown documentation for educational purposes around prompt engineering and LLM security research.

## Repository Structure

- **SystemPrompts/** - System prompts from various LLM providers (OpenAI, Anthropic, Google, Meta, xAI, etc.), organized by vendor with date-stamped filenames
- **CustomInstructions/** - Custom GPT instructions and configurations, including a large index in `CustomInstructions/README.md` (the table of contents for ChatGPT GPTs)
- **Jailbreak/** - Jailbreak prompts organized by LLM provider
- **Security/** - GPT instruction protection techniques
- **Articles/** - Technical articles about LLM internals and prompt engineering
- **Tools/openai_gpts/** - Python utilities for managing GPT documentation

## Tools

Python scripts in `Tools/openai_gpts/`:

```bash
# Rebuild the CustomInstructions/README.md table of contents
python Tools/openai_gpts/idxtool.py --toc

# Find a GPT by ID or URL
python Tools/openai_gpts/idxtool.py --find-gpt <GPT_ID_OR_URL>

# Generate a markdown template for a new GPT entry
python Tools/openai_gpts/idxtool.py --template <CHATGPT_URL>

# Generate template with metadata dump (standalone tool)
python Tools/openai_gpts/gen_gpt_templ.py <URL_OR_ID> --dump
```

## File Naming Conventions

- **SystemPrompts**: `MMDDYYYY-ProviderName.md` or `provider_feature_MMDDYYYY.md`
- **CustomInstructions GPTs**: `{gpt_id}.md` with GPT metadata in frontmatter-style headers

## Contributing New Prompts

When adding system prompts or GPT instructions:
1. Use the appropriate date-stamped naming convention
2. For GPTs, use `idxtool.py --template` to generate the initial file structure
3. Run `idxtool.py --toc` after adding new GPT files to update the table of contents
