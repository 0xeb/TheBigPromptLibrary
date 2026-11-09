# Mistral Vibe default system prompt (official source, partial)

- **Contributed by**: [MILESMAKMAK](https://github.com/MILESMAKMAK)
- **Contributed on**: 11/09/2026
- **Source**: [Mistral Vibe](https://github.com/mistralai/mistral-vibe), vibe/core/prompts/cli.md
- **Source commit**: [c96a6db](https://github.com/mistralai/mistral-vibe/commit/c96a6dbb34d34f8a868b3f67b279ecabbf1aa616) (package version 3.1.0; cli.md last changed in v3.0.3)
- **License**: Mistral Vibe is Apache-2.0 licensed; see the [upstream license](https://github.com/mistralai/mistral-vibe/blob/c96a6dbb34d34f8a868b3f67b279ecabbf1aa616/LICENSE). cli.md is preserved verbatim.
- **Note**: `cli` is the default `system_prompt_id` (vibe/core/config/vibe_schema.py). This is the static base prompt; at runtime Vibe adds project and git context, AGENTS.md instructions and other sections (vibe/core/system_prompt.py), plus tool context. Those additions, the bundled experiment variants (cli_2026-*.md) and the explore/lean agent prompts are not included.

The prompt file below is copied byte-for-byte from the official source at the commit above.

## Files

- [cli.md](./cli.md) - default system prompt (`vibe/core/prompts/cli.md`)
