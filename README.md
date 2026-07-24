# Distill Public Persona

> Turn a public timeline into a reusable persona model — with receipts.

Most “AI clones” begin with vibes. This project begins with evidence.

`distill-public-persona` is a Codex Skill for studying a person’s public writing and extracting four separate layers:

- **language fingerprint** — rhythm, vocabulary, structure, humor, and audience shifts;
- **reasoning patterns** — evidence preferences, heuristics, uncertainty, and value trade-offs;
- **knowledge map** — demonstrated topics, depth, date coverage, and blind spots;
- **evidence cards** — source-linked claims with confidence and competing explanations.

The result is a reusable persona package or derived Skill that can explain where each inference came from, preserve uncertainty, and disclose that its output is an AI simulation.

## What is inside

```text
distill-public-persona/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── analysis-prompts.md
│   ├── corpus-schema.md
│   └── evaluation.md
└── scripts/
    └── validate_corpus.py
```

## Quick start

1. Export or collect lawful public content as JSONL or CSV.
2. Normalize it using `references/corpus-schema.md`.
3. Validate the corpus:

```bash
python3 scripts/validate_corpus.py path/to/corpus.jsonl
```

4. Invoke the Skill:

```text
Use $distill-public-persona to turn this public corpus into an
evidence-grounded persona model and evaluation set.
```

5. Keep raw corpus files in a private data directory. Publish the reusable method, source manifest, and synthetic examples.

## Design principle

Style is observable. Reasoning is inferable with evidence. Knowledge is topic-specific. Private mental states remain unknown.

Every material claim should carry:

```text
claim → evidence IDs → confidence → competing explanation → boundary
```

## Responsible use

Use the Skill for research, writing analysis, education, public-communication studies, and clearly disclosed creative simulations. Preserve source terms, copyright, privacy, deletion requests, and local law.

Derived persona Skills should use neutral aliases, disclose AI simulation, and exclude identity claims, authorization claims, private-message simulation, sensitive-attribute inference, high-stakes impersonation, financial solicitation, and attributed political persuasion.

## License

MIT
