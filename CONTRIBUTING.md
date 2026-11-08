# Contributing

Thanks for contributing to The Big Prompt Library. The rules below exist so the collection stays trustworthy and navigable.

## The one rule that matters: verbatim only

Contribute the prompt **exactly as the system emitted it**. Do not summarize, paraphrase, condense into bullets, clean up, or translate.

A summary is not useful here. The value of this repository is that a reader can see precisely how a real product prompts its model - the wording, the ordering, the hedges, the typos. A condensed version destroys all of that and cannot be verified by anyone.

Long is fine. Extracted coding-agent prompts in this repo routinely run 500+ lines.

If you can only capture part of a prompt, say so explicitly and label the entry **Partial**.

## Where things go

| Directory | Contents |
|-----------|----------|
| `SystemPrompts/<Vendor>/` | System prompts from LLM products and services |
| `CustomInstructions/ChatGPT/` | Custom GPT instructions |
| `Jailbreak/<Vendor>/` | Jailbreak prompts |
| `Security/GPT-Protections/` | Instruction-protection techniques |
| `Articles/<topic>/` | Write-ups and analysis |

## Naming

Use one of these two forms:

- `YYYYMMDD-ProviderName.md` - e.g. `20251202-Claude-Opus4.5-Soul-Document.md`
- `provider_feature_YYYYMMDD.md` - e.g. `github_copilot_cli_20260221.md`

Custom GPTs are named `{gpt_id}.md`; generate the file with `python Tools/openai_gpts/idxtool.py --template <CHATGPT_URL>`.

## Provenance header

Every new entry starts with a header block so readers can judge and re-verify it:

```markdown
# <Name> (unverified)

- **Contributed by**: [username](https://github.com/username)
- **Contributed on**: MM/DD/YYYY
- **Source**: <product, tier, platform - e.g. "Android Gemini App (Paid tier)">
- **Note**: <extraction method, discrepancies, anything partial or uncertain>
```

Drop `(unverified)` only if the prompt is officially published by the vendor or you can point at a public source. A link to a gist, tweet, or vendor repo in the `Source` line is worth more than any assertion.

If you are not the original extractor, credit whoever was.

## Update the index in the same pull request

- `SystemPrompts/README.md` is maintained **by hand**. Add your entry to the right vendor section - newest first. If the vendor has no section yet, add one before `## Miscellanous`, with a `See: <vendor url>` line.
- `CustomInstructions/README.md` is **generated**. Run `python Tools/openai_gpts/idxtool.py --toc` and commit the result.
- `Jailbreak/`, `Security/`, and `Articles/` each have their own `README.md` to update.

A file nobody can find from an index may as well not be in the repo.

## Multi-file agent contexts

Most contributions are a single markdown file. When a system exposes its context as many files - a module tree, a set of `AGENTS.md` files, tool declarations - keep the structure and add a folder instead:

```
SystemPrompts/<Vendor>/<provider_feature_YYYYMMDD>/
    README.md      <- provenance header, what's captured, what's missing, an index
    ...            <- the files, unmodified
```

Link the folder's `README.md` from `SystemPrompts/README.md`. See [`SystemPrompts/Notion/notion-ai_20260322/`](./SystemPrompts/Notion/notion-ai_20260322/README.md) for a worked example.

Source files are in scope when they are what the *model* sees - tool and type declarations, instruction files. A product's actual implementation source is not.

## No secrets, no other people's data

Sandbox and workspace dumps leak. Before opening a pull request, check your files for API keys, tokens, session identifiers, real email addresses, and any workspace content belonging to real people. Redact it, and note the redaction in the entry.

## No advertising

Entries document other people's prompts; they are not a place to promote your own work. Do not add links to, install instructions for, or "regenerate with" steps using your own (or your employer's) tools, products, services, or prompt archives.

- Describe the extraction method generically ("a local proxy recorded the request", "read from the shipped bundle") - that is what `Note` asks for.
- For the `Source` line, link the vendor's own public source (their repo, package, docs) rather than a copy hosted by the capture tool.
- The `Contributed by` link to your GitHub profile is fine and expected.

Pull requests that promote a contributor's product are either closed or merged with the promotion removed.

## Screenshots

Evidence screenshots are welcome next to the prompt they support (see `SystemPrompts/xAI/08212024-Grok2-fun.png`). Keep them small and crop out anything personal.

## Scope

This repository is for educational and research use - understanding how these systems are prompted, and how prompts leak. Contributions aimed at operationalizing abuse aren't accepted.
