# omp: Use the AI Subscriptions You Already Pay For, From Any App

*By **Elias Bachaalany** — [@0xeb](https://github.com/0xeb) on GitHub · [Binary Wizards](https://www.youtube.com/@binary-wizards) on YouTube · [@eliasbchlny](https://x.com/eliasbchlny) on X*

*One local address for every AI plan you already pay for: how omp's auth broker and gateway work, and how to run Claude Code through them.*

If you're like many people, you pay for more than one AI plan: ChatGPT Plus for work, Claude
Pro, Max or Ultra for writing, GitHub Copilot or Cursor through your job, maybe a Z.AI GLM Coding
Plan on the side. Each one works only inside its vendor's own app.

Then you find a tool you'd like to try: an editor plugin, a notes app with an "AI" button, a
script a friend shared, a different coding agent. It asks for an **API key**. That's a separate
product, billed per token, on top of the subscription you already pay for.

**There's a way around that.** [omp](https://omp.sh) is an open-source coding agent, and it ships a
small server that most people never notice: the **auth gateway**. You log in to your subscriptions
once, and it gives every app on your machine one address to talk to. It speaks the same "API
language" as OpenAI and Anthropic, which most AI tools already understand.

What that gets you:

- **One address for all your plans.** Claude, ChatGPT/Codex, Copilot, Cursor, OpenCode, Z.AI and
  DeepSeek all sit behind `http://127.0.0.1:4000`, and the model name in each request decides
  which plan answers.
- **Tools that already work with it.** Anything with a "custom base URL" or "OpenAI-compatible"
  setting connects: SDKs, editor plugins, `curl`, Claude Code, Codex CLI.
- **Your real logins stay put.** Apps get one gateway token that you can rotate. Your passwords
  and OAuth tokens never leave omp's vault.
- **Mix and match.** Run Claude Code on a GPT model, or point an OpenAI-SDK script at Claude.

Here is the whole idea, start to finish:

```bash
omp auth-broker login openai-codex                     # 1. log in once, in your browser
omp auth-broker serve                                  # 2. the vault (leave it running)
OMP_AUTH_BROKER_URL=http://127.0.0.1:8765 \
  omp auth-gateway serve                               # 3. the gateway, in a second terminal
# 4. in any app: base URL http://127.0.0.1:4000/v1, API key = the output of `omp auth-gateway token`
```

The rest of this article covers the CLI, the setup in five phases, and then a worked example:
setting up Claude Code to run through the gateway. Before you connect a consumer plan, read the
[note on subscription terms](#a-note-on-subscription-terms) at the end.

> Written against **omp 18.18.1** (November 2026). The gateway is moving fast; check
> `omp auth-gateway --help` on your version.

## How the pieces fit

```
  any client (curl, SDKs, Claude Code, Codex CLI, editor plugins…)
        │  Authorization: Bearer <gateway token>
        ▼
  omp auth-gateway serve      127.0.0.1:4000   /v1/messages, /v1/chat/completions, /v1/responses, …
        │  broker token (the gateway only)
        ▼
  omp auth-broker serve       127.0.0.1:8765   SQLite vault, background OAuth refresher
        │
        ▼
  api.anthropic.com · chatgpt.com (Codex) · api.githubcopilot.com · opencode.ai · …
```

- The **broker** is the only process that holds OAuth refresh tokens. It refreshes them in the
  background (it checks every 60 s and renews anything due to expire within 5 minutes). It is
  **not** the endpoint clients call.
- The **gateway** is a broker client. It receives a redacted credential snapshot, in which every
  refresh token is replaced by a sentinel, and asks the broker to refresh a credential when its
  access token expires. Each request goes through omp's own provider code, so the request shaping,
  provider quirks and refresh-on-401 are the same ones omp's agent uses. There is no raw
  passthrough.
- Neither service runs omp's agent loop. The client keeps its own planning, tools and
  conversation; omp supplies only upstream auth and format translation.

## The CLI

Two command families, each with a handful of verbs.

### `omp auth-broker`: the vault

```
omp auth-broker serve   [--bind=host:port] [--trust-proxy-headers]   # run the vault (default 127.0.0.1:8765)
omp auth-broker token   [--regenerate] [--json]                      # print or rotate the broker token
omp auth-broker list                                                 # every provider omp can log in to
omp auth-broker login   [<provider>] [--via=user@host] [--dry-run]   # log in (no provider: pick from a menu)
omp auth-broker logout  [<provider>]
omp auth-broker import  <file|dir> [--provider=<id>] [--dry-run]     # bring in exported credentials
omp auth-broker migrate --from-local [--include-oauth] [--include-env] [--dry-run]
omp auth-broker status  [--json]
```

`omp auth-broker list` is worth running once. On 18.18.1 it lists about sixty providers. The big
ones:

| Provider id | What it is |
| --- | --- |
| `anthropic` | Claude Pro, Max and Ultra plans |
| `openai-codex` | ChatGPT Plus/Pro (Codex subscription); `openai-codex-device` for headless logins |
| `github-copilot` | GitHub Copilot |
| `cursor` | Cursor (browser login; serves Claude, GPT and more) |
| `zai-coding-plan`, `zai` | Z.AI GLM Coding Plan: browser sign-in, or an API key (`ZAI_API_KEY`) |
| `opencode-go`, `opencode-zen` | OpenCode plans (API key, `OPENCODE_API_KEY`) |
| `deepseek` | DeepSeek (API key, `DEEPSEEK_API_KEY`) |
| `openrouter`, `kimi-code`, `google-gemini-cli`, `xai-oauth`, … | the long tail |

### `omp auth-gateway`: the HTTP front end

```
omp auth-gateway serve  [--bind=host:port] [--no-auth] [--clients=<file>] [--trust-proxy-headers]
omp auth-gateway token  [--regenerate] [--json]     # the token clients send (created on first run)
omp auth-gateway status [--json]                    # local token file + broker reachability
omp auth-gateway check  [--strict] [--json]         # probe every credential; --strict spends a little quota
omp auth-gateway stdio                              # same routes as JSON lines, for one parent process
```

`serve` needs to know where the broker is, through `OMP_AUTH_BROKER_URL` (or `auth.broker.url` in
`config.yml`). The default bind is `127.0.0.1:4000`.

## Setup, in phases

Do every phase **as the same OS user, with the same omp config**. The broker reads the credential
store that your logins wrote, and a different user or profile means a different, empty store.

### Phase 1: log in to your subscriptions

```bash
omp auth-broker login anthropic          # Claude Pro/Max/Ultra
omp auth-broker login openai-codex       # ChatGPT Plus/Pro (Codex)
omp auth-broker login github-copilot     # Copilot
omp auth-broker login cursor             # Cursor
omp auth-broker login zai-coding-plan    # Z.AI GLM Coding Plan
```

Each one prints a URL to open in a browser, and some ask you to paste a code back. API-key
providers such as OpenCode and DeepSeek go through omp's interactive login instead: run `omp`,
type `/login`, and pick the provider. For OpenCode it points you to `https://opencode.ai/auth`
and stores the key as `OPENCODE_API_KEY`; DeepSeek works the same way with `DEEPSEEK_API_KEY`.

Check each login before going further:

```bash
omp models openai-codex
omp -p --no-session --model openai-codex/gpt-5.6-sol "Reply with exactly: PONG"
```

### Phase 2: start the broker

```bash
omp auth-broker serve
```

On first start it writes its token to `<config-dir>/auth-broker.token` (mode `0600`). Leave it
running in its own terminal, `screen` or `tmux` window, or service.

### Phase 3: start the gateway

In a second terminal:

```bash
OMP_AUTH_BROKER_URL=http://127.0.0.1:8765 omp auth-gateway serve
```

On the same host and user, the gateway finds the broker token file by itself. A gateway on another
host or user needs the broker token passed explicitly.

The gateway rebuilds its model catalog every 15 minutes and checks for credential changes every
10 seconds. Still, **restart the gateway after adding or removing a login**. It is the quickest way
to be sure `/v1/models` reflects the change.

### Phase 4: choose how clients authenticate

By default every route except `/healthz` requires the gateway token:

```bash
export OMP_GATEWAY_TOKEN="$(omp auth-gateway token)"
```

There are two alternatives.

- **`--no-auth`** turns the bearer check off. Any process that can reach the listener can spend your
  subscriptions, so use it only on loopback, and keep `--bind` explicit, because the flag doesn't
  force a loopback bind:

  ```bash
  OMP_AUTH_BROKER_URL=http://127.0.0.1:8765 \
    omp auth-gateway serve --bind=127.0.0.1:4000 --no-auth
  ```

- **`--clients=<file>`** admits extra, **scoped** tokens. Each one is limited to a list of models
  and accounts. The file stores only SHA-256 digests and is re-read every 10 seconds while the
  gateway runs:

  ```json
  {
    "ci": {
      "tokenSha256": "<printf %s \"$TOKEN\" | shasum -a 256>",
      "models": ["openai-codex/*", "anthropic/claude-haiku-5-5"]
    }
  }
  ```

  A model outside the list answers `404 Unknown model`, and that client's `/v1/models` shows only
  what it was granted.

### Phase 5: smoke test

```bash
G=http://127.0.0.1:4000
AUTH="Authorization: Bearer $OMP_GATEWAY_TOKEN"

curl -s $G/healthz                                   # {"ok":true,"version":"18.18.1"}
curl -s $G/v1/models -H "$AUTH" | jq -r '.data[].id'
```

`/v1/models` is the **authoritative list** of what you can call: the catalog, filtered to the
providers you hold credentials for. Each row carries more than an ID:

```json
{
  "id": "anthropic/claude-fable-5",
  "owned_by": "anthropic",
  "api": "anthropic-messages",
  "display_name": "Claude Fable 5",
  "input_modalities": ["text", "image"],
  "context_length": 1000000,
  "max_output_tokens": 128000
}
```

Then one request per chat format:

```bash
# Anthropic Messages
curl -s $G/v1/messages -H "$AUTH" -H 'anthropic-version: 2023-06-01' -H 'Content-Type: application/json' \
  -d '{"model":"anthropic/claude-haiku-5-5","max_tokens":100,
       "messages":[{"role":"user","content":"What is 17*3?"}]}'

# OpenAI Chat Completions
curl -s $G/v1/chat/completions -H "$AUTH" -H 'Content-Type: application/json' \
  -d '{"model":"openai-codex/gpt-5.6-sol","messages":[{"role":"user","content":"What is 17*3?"}]}'

# OpenAI Responses
curl -s $G/v1/responses -H "$AUTH" -H 'Content-Type: application/json' \
  -d '{"model":"openai-codex/gpt-6.1-sol","input":"What is 17*3?"}'
```

Add `"stream": true` to get SSE back in the same wire format.

## Routing: the path picks the format, `model` picks the backend

| Path | Wire format |
| --- | --- |
| `POST /v1/messages` | Anthropic Messages |
| `POST /v1/chat/completions` | OpenAI Chat Completions |
| `POST /v1/responses` | OpenAI Responses |
| `POST /v1/pi/stream` | omp's native stream format |

The gateway never guesses the format from the body. The backend comes only from the `model` field,
as `provider/model-id`, so **the two are independent**. Here is an Anthropic-format request answered
by a Codex subscription, a real reply:

```json
{
  "type": "message",
  "role": "assistant",
  "model": "openai-codex/gpt-5.6-sol",
  "content": [{ "type": "text", "text": "17 × 3 is 51." }],
  "stop_reason": "end_turn",
  "usage": { "input_tokens": 18, "output_tokens": 12, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0 }
}
```

Bare IDs work too. `gpt-5.6-sol` with no prefix goes to the highest-ranked provider that serves
it. Native accounts (`openai-codex`, `anthropic`, `openai`) rank ahead of aggregators, and
`modelProviderOrder` in `config.yml` overrides the ranking. Use the prefixed form when it matters
which account pays.

## Beyond chat

The gateway has more routes than chat. They are real, but omp doesn't generate audio or images
itself. Each route forwards to a provider that offers that kind of model, so it only works once
the broker holds a login for such a provider:

| Route | What | Who serves it (omp 18.18.1) |
| --- | --- | --- |
| `POST /v1/images/generations`, `/v1/images/edits` | image generation and edits (OpenAI Images wire) | **Codex subscription** (`gpt-image-2`), OpenAI API key, OpenRouter |
| `POST /v1/audio/speech` | text-to-speech, returns raw audio | xAI (`grok-tts`: API key, or the SuperGrok / X Premium+ login), OpenRouter, DeepInfra |
| `POST /v1/audio/transcriptions` | speech-to-text (multipart `file`, 25 MiB cap) | OpenAI API key, OpenRouter |
| `POST /v1/embeddings` | embeddings (OpenAI wire) | OpenAI API key, OpenRouter |
| `POST /v1/rerank` | rerank (OpenRouter wire) | OpenRouter |
| `POST /v1/videos`, `GET /v1/videos/:id[/content]` | video jobs: submit, poll, download | OpenRouter |
| `GET /v1/usage` | your subscription usage windows, across every account | every login |
| `GET /v1/credentials/check` | per-credential health, handy when something starts returning 401 | every login |

Of the big subscriptions, only Codex adds anything here: image generation. Claude, Copilot,
Cursor, OpenCode, Z.AI and DeepSeek are chat-only through the gateway. An OpenRouter key turns on almost every route, and
the "OpenAI API key" rows mean a direct `OPENAI_API_KEY`, not the Codex login.

`/v1/models` marks non-chat rows with a `kind` field (`image`, `tts`, `stt`, `embedding`,
`rerank`, `video`, …), so check there what your logins actually unlock. With no provider for a
modality, its route has no model to call and the request is refused. Sending a chat route a
non-chat model fails with a `400` that names the route to use instead.

**`omp auth-gateway stdio`** serves all of these to a single parent process over stdin/stdout,
with no port and no token. It suits editor plugins and scripts:

```bash
echo '{"id":1,"path":"/v1/chat/completions","body":{"model":"@smol","messages":[{"role":"user","content":"hi"}]}}' \
  | omp auth-gateway stdio
```

Unlike `serve`, stdio uses your normal omp setup, including `models.yml`, extension providers and
role selectors like `@smol`.

## Worked example: Claude Code on the gateway

Claude Code speaks Anthropic Messages, and it lets you replace its endpoint and credential through
environment variables.

### 1. The essentials

```bash
export ANTHROPIC_BASE_URL=http://127.0.0.1:4000          # no /v1: Claude Code appends it
export ANTHROPIC_AUTH_TOKEN="$OMP_GATEWAY_TOKEN"          # sent as Authorization: Bearer
unset ANTHROPIC_API_KEY
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1       # let /model list the gateway's models
claude
```

Use **`ANTHROPIC_AUTH_TOKEN`, not `ANTHROPIC_API_KEY`**. The gateway accepts only
`Authorization: Bearer`, and `ANTHROPIC_API_KEY` sends `x-api-key`, which gets a `401`. With
`--no-auth` the token is ignored, but set it to a placeholder such as `unused` if a client insists
on one.

Inside Claude Code, run `/status` to confirm the base URL, and `/model` to pick from what the
gateway serves. A gateway ID that's missing from the picker can be added with
`ANTHROPIC_CUSTOM_MODEL_OPTION=anthropic/claude-sonnet-5-5`.

### 2. Pin every model slot

Claude Code doesn't use one model for everything. Background tasks, the "fast" model and subagents
each pick their own. If you don't set them, they ask the gateway for model names it may not serve.
Pin them all:

```bash
M=anthropic/claude-sonnet-5-5
export ANTHROPIC_MODEL=$M
export ANTHROPIC_DEFAULT_OPUS_MODEL=$M
export ANTHROPIC_DEFAULT_SONNET_MODEL=$M
export ANTHROPIC_DEFAULT_HAIKU_MODEL=anthropic/claude-haiku-5-5   # cheaper model for background work
export ANTHROPIC_DEFAULT_FABLE_MODEL=$M
export CLAUDE_CODE_SUBAGENT_MODEL=$M
```

### 3. Or: Claude Code's harness, a GPT brain

Because the backend is just the `model` field, you can point the same Claude Code at your Codex
subscription:

```bash
M=gpt-5.6-sol            # bare ID; resolves to openai-codex/gpt-5.6-sol
export ANTHROPIC_MODEL=$M ANTHROPIC_DEFAULT_OPUS_MODEL=$M ANTHROPIC_DEFAULT_SONNET_MODEL=$M \
       ANTHROPIC_DEFAULT_HAIKU_MODEL=$M ANTHROPIC_DEFAULT_FABLE_MODEL=$M CLAUDE_CODE_SUBAGENT_MODEL=$M
export CLAUDE_CODE_EFFORT_LEVEL=high
claude
```

This works day to day. The tool calls translate, streaming works and the agent loop runs.
Anthropic doesn't support Claude Code on non-Claude models, though, and features that exist on
only one side (prompt caching details, some thinking controls, server-side tools) don't translate
into each other.

### 4. Wrap it

Put the block in a small launcher script (`claude-omp`) and keep Claude Code's state separate from
your normal setup with `CLAUDE_CONFIG_DIR=~/.claude-omp`. Then your regular `claude` stays on its
own login, and `claude-omp` runs on the gateway.

### Other clients, briefly

- **OpenAI SDKs and tools** use `base_url="http://127.0.0.1:4000/v1"` with the gateway token as
  the API key.
- **Codex CLI** needs a custom provider with base URL `http://127.0.0.1:4000/v1`, the `responses`
  wire API, the gateway token, and an exact model ID from `/v1/models`. Its own ChatGPT login has
  nothing to do with omp's Codex login.
- **Anything Anthropic-shaped** uses the Claude Code variables above.

## Two tokens, different power

| Token | File | Grants | Give it to |
| --- | --- | --- | --- |
| Gateway token | `<config-dir>/auth-gateway.token` | inference through the gateway, never the upstream credentials | your clients |
| Broker token | `<config-dir>/auth-broker.token` | **credential snapshots**: real OAuth access tokens and stored API keys | the gateway, and nothing else |

"Clients need no API keys" means clients never receive an upstream credential. It doesn't mean the
gateway is open. The gateway token is a real secret, and anyone holding it can spend your quota.
Transport security is up to you: the gateway speaks plain HTTP, so if it leaves loopback, put TLS
or a private network in front of it. A request that carries the gateway token in its URL, or in a
logged or forwarded header, is rejected before any credential lookup, which keeps the token out of
logs.

## Limits and gotchas

- **`models.yml` is ignored by `serve`.** Your custom providers, local base URLs and overrides are
  deliberately left out, so local config can't redirect broker-backed traffic. (`stdio` honours
  them.)
- **No aliases and no default model.** Clients must send a model the gateway serves.
- **No web-search route.** Clients' built-in web-search tools aren't backed by omp's search
  engines.
- **A catalog entry is not account access.** `/v1/models` lists what your credentials can reach in
  principle, and your plan decides the rest.
- **Envelope translation is not feature parity.** A cross-format request carries text, images,
  tools and streaming, not every vendor-specific knob.
- **Same user, same config.** Most "it lists no models" problems come from a broker started under
  a different user or profile from the one that did the logins.

## A note on subscription terms

The gateway makes it easy to use a consumer subscription from any client. Whether your
subscription *allows* that is a separate question, and the answer differs by vendor and changes
over time. Claude Pro/Max/Ultra in particular is meant for Anthropic's own apps and Claude Code, and
re-exposing it to other clients can get an account flagged. omp offering a login doesn't make
every use of it allowed. Read the current terms for each plan you wire in. Where it matters, use
the provider's API-key option, which the gateway routes the same way.
