# Corpus schema

Use UTF-8 JSONL when possible. Store one content item per line.

## Required fields

| Field | Type | Meaning |
|---|---|---|
| `id` | string | Stable local source ID |
| `text` | string | Content text |
| `created_at` | string | ISO 8601 timestamp or date |
| `source_type` | string | `original`, `reply`, `quote`, `repost`, `profile`, `article`, `transcript`, or `other` |

## Recommended fields

| Field | Type | Meaning |
|---|---|---|
| `url` | string | Public permalink |
| `author_alias` | string | Neutral target alias |
| `language` | string | BCP 47 tag such as `en` or `zh-CN` |
| `conversation_id` | string | Thread or conversation identifier |
| `in_reply_to_id` | string | Parent content ID |
| `quoted_id` | string | Quoted content ID |
| `context` | string | Minimal context required for interpretation |
| `is_target_authored` | boolean | Whether the target authored the text |
| `collected_at` | string | Collection timestamp |

## Example

```json
{"id":"p-001","text":"Example public post.","created_at":"2026-01-02T09:00:00Z","source_type":"original","url":"https://example.com/p-001","author_alias":"persona-alpha","language":"en","is_target_authored":true,"collected_at":"2026-07-25T00:00:00Z"}
```

## Data handling

- Keep raw exports in a private data directory.
- Publish source manifests, schemas, prompts, and synthetic examples.
- Replace real names with aliases in reusable templates.
- Record URLs and source IDs for traceability.
- Respect source terms, copyright, deletion requests, and applicable privacy rules.
- Minimize verbatim excerpts in distributable artifacts.
