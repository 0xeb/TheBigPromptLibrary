# Kimi Code CLI system prompt templates (official source, partial)

- **Contributed by**: [MILESMAKMAK](https://github.com/MILESMAKMAK)
- **Contributed on**: 11/09/2026
- **Source**: [Moonshot AI Kimi Code CLI](https://github.com/MoonshotAI/kimi-code), packages/agent-core-v2/src/app/agentProfileCatalog/*.md
- **Source commit**: [725194d](https://github.com/MoonshotAI/kimi-code/commit/725194d7e127811ed754dde0e98c4788866d779f) (apps/kimi-code version 2.5.2)
- **License**: Kimi Code CLI is MIT-licensed; see the [upstream license](https://github.com/MoonshotAI/kimi-code/blob/725194d7e127811ed754dde0e98c4788866d779f/LICENSE). The files below are preserved verbatim.
- **Note**: system.md is the base template; profile-shared.ts in the same folder fills its `${...}` placeholders at runtime (product name defaults to "Kimi Code CLI") and inserts the coding, delivering-work (or delivering-work-read-only) and project-information sections. Runtime values such as the working directory, OS, shell, directory listing, AGENTS.md, skills, plugins and agent lists, the guidance strings defined in TypeScript, and the tool descriptions are not included. This replaces the archived Python [kimi-cli](https://github.com/MoonshotAI/kimi-cli), which is not covered here.

The prompt files below are copied byte-for-byte from the official source at the commit above.

## Files

- [system.md](./system.md) - base system prompt template
- [coding.md](./coding.md) - coding section (`${coding_section}`, omitted for read-only profiles)
- [delivering-work.md](./delivering-work.md) - delivering-work section (`${delivering_work_section}`)
- [delivering-work-read-only.md](./delivering-work-read-only.md) - delivering-work section for read-only profiles
- [project-information.md](./project-information.md) - project information section wrapping AGENTS.md content
