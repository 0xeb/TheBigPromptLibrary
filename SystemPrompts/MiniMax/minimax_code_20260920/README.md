# MiniMax Code - three system prompts - 09/20/2026

- **Contributed by**: [xizhuomengcontin](https://github.com/xizhuomengcontin)
- **Contributed on**: 09/20/2026
- **Source**: MiniMax Code (`@minimax-ai/code`) 0.4.12, `exec`, bring-your-own-key run against `deepseek/deepseek-v4-flash-free`
- **Extraction**: recorded off the wire by [OrcaReplay](https://github.com/Continuum-AI-Corp/OrcaReplay)'s local proxy while the CLI ran unmodified - not asked from the model. One command per file reproduces it, see [Regenerate](#regenerate).
- **Note**: complete for a bring-your-own-key run, partial for a signed-in one. See [What is missing](#what-is-missing).

## What this is

MiniMax Code ships **three** system prompts and picks one per surface, so all three are here. They
are three documents rather than one with a flag in it: `coding` swaps the whole `Deliverable Files`
section for `Media Output`, and `work` adds an `Artifact Completion Contract` on top of that.

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
and the tool set never moved. The prompts are Handlebars templates shipped inside the package
(`assets/agents/_v2/*/SYSTEM.md.hbs`), not fetched from a server, and none of their conditionals
branches on a model or a provider. The model in the capture is the one that answered, not a variant.

## What is missing

These are the BYOK shape. The code that answers a bring-your-own-key run forces `disableMemory` and
`disableMavis`, which drops a 3,381-character `# Memory` section and a 210-character block that a
signed-in run carries. Setting `memory.enabled: true` in the config does not bring it back -
measured, byte-identical output. Capturing the fuller prompt needs a MiniMax credential, and this
capture deliberately used none.

## Scrubbing

Home directory, username, git identity, hostnames and uuids are replaced with `{PLACEHOLDER}`
tokens before the file is written. No keys, tokens or session ids. Nothing else is reworded,
reordered or trimmed.

## Regenerate

```console
npm i -g orcareplay
git clone https://github.com/Continuum-AI-Corp/OrcaReplay && cd OrcaReplay
node capture/capture.mjs mcode --model deepseek/deepseek-v4-flash-free --prompt-mode tui    --allow-failed
node capture/capture.mjs mcode --model deepseek/deepseek-v4-flash-free --prompt-mode coding --allow-failed
node capture/capture.mjs mcode --model deepseek/deepseek-v4-flash-free --prompt-mode work   --allow-failed
```

`--allow-failed` keeps the capture when the turn comes back `401`, which it will: the key written
into the generated config is a placeholder, and the prompt is captured regardless because it
travels in the request. Run it from a directory that is a git repository and has no MCP config -
the harness is told whether it is in one, and an MCP config would add those servers' tools to the
tool list.

Both this and the run notes behind it are in
[OrcaPromptVault](https://github.com/Continuum-AI-Corp/OrcaPromptVault/tree/main/MiniMax-Code).
