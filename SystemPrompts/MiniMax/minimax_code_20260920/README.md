# MiniMax Code - three system prompts - 09/20/2026 (partial)

- **Contributed by**: [xizhuomengcontin](https://github.com/xizhuomengcontin)
- **Contributed on**: 09/20/2026
- **Source**: MiniMax Code ([`@minimax-ai/code`](https://www.npmjs.com/package/@minimax-ai/code/v/0.4.12)) 0.4.12, `exec`, bring-your-own-key run against `deepseek/deepseek-v4-flash-free`. The prompt text ships in the package as Handlebars templates (`assets/agents/_v2/{tui,coding,work}/SYSTEM.md.hbs`), with harness sections in the bundled JS and skill descriptions in `assets/skills/*/SKILL.md`.
- **Note**: Recorded off the wire by a local proxy while the CLI ran unmodified, not asked from the model. Complete for a bring-your-own-key run, partial for a signed-in one; see [What is missing](#what-is-missing). Every captured line except the runtime environment block was checked against the 0.4.12 package contents.

## What this is

MiniMax Code ships **three** system prompts and picks one per surface (`--prompt-mode`), so all three
are here. They are three documents rather than one with a flag in it: `coding` swaps the whole
`Deliverable Files` section for `Media Output`, and `work` adds an `Artifact Completion Contract` on
top of that.

| `--prompt-mode` | file | chars | tools |
|---|---|--:|--:|
| `tui` (default) | [tui.md](./tui.md) | 14,674 | 18 |
| `coding` | [coding.md](./coding.md) | 16,054 | 18 |
| `work` | [work.md](./work.md) | 17,618 | 18 |

All three declare the same [18 tools](./tools.json) - the three captures came out byte-identical, so
they share the one file.

## The model is not the variable

Seven models across six labs - MiniMax, DeepSeek, OpenAI, Kimi, GLM, Hunyuan - on two different
gateways produced **119 identical lines each**. The only difference was one line, `- Model: <id>`,
and the tool set never moved. None of the templates' conditionals branches on a model or a
provider, so the model in the capture is the one that answered, not a variant.

## What is missing

These are the BYOK shape. The code that answers a bring-your-own-key run forces `disableMemory` and
`disableMavis`, which drops a 3,381-character `# Memory` section and a 210-character block that a
signed-in run carries. Setting `memory.enabled: true` in the config does not bring it back -
measured, byte-identical output. Capturing the fuller prompt needs a MiniMax credential, and this
capture deliberately used none.

## Scrubbing

Home directory, username, git identity, hostnames and uuids are replaced with `{{PLACEHOLDER}}`
tokens. No keys, tokens or session ids. Nothing else is reworded, reordered or trimmed.

The capture was taken from a directory that is a git repository and has no MCP config: the harness
is told whether it is in one, and an MCP config would add those servers' tools to the tool list.
