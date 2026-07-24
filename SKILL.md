---
name: distill-public-persona
description: Build an evidence-grounded, reusable persona skill from a person's public posts, interviews, articles, transcripts, or profile pages. Use when collecting and cleaning a public corpus, extracting a language fingerprint, mapping public reasoning patterns and topic knowledge, generating a persona-model skill, or evaluating whether a simulated response stays faithful to cited public evidence.
---

# Distill Public Persona

Create a model of the public persona expressed in a supplied corpus. Treat style, reasoning, knowledge, and confidence as separate layers. Preserve traceability from every material inference to source evidence.

## Choose the deliverable

- Produce an **analysis** when the user wants findings about style, reasoning, or public knowledge.
- Produce a **persona package** when the user wants reusable evidence cards and model files.
- Produce a **persona skill** when the user wants a Codex skill that can generate or evaluate responses.
- Produce an **evaluation** when the user supplies an existing persona model or generated samples.

## Gather consent and scope

Confirm the target is an adult public figure, the user, or a person whose public content the user may lawfully analyze. Use only content supplied by the user or lawfully accessible public content.

Record:

- target alias and public profile URLs;
- corpus cutoff date;
- included sources and languages;
- intended use;
- required disclosure text;
- topics or contexts excluded by the user.

Use an alias in distributable artifacts. Keep raw corpus files and private identifiers outside a public skill repository.

## Build the corpus

Accept JSONL or CSV. Read [references/corpus-schema.md](references/corpus-schema.md) before normalizing data. Run:

```bash
python3 scripts/validate_corpus.py PATH_TO_CORPUS
```

Separate original posts, replies, quotes, reposts, profile text, and third-party text. Preserve dates, URLs, conversation context, and source type. Mark missing values as unknown. Report sampling bias, deleted context, promotional content, ghostwriting risk, and platform effects.

## Extract the model

Read [references/analysis-prompts.md](references/analysis-prompts.md) and execute its stages in order:

1. Build the language fingerprint.
2. Map public reasoning patterns.
3. Map demonstrated topic knowledge.
4. Create evidence cards.
5. Compile the persona specification.

Assign every inference one evidence class:

- `explicit`: directly stated by the target;
- `supported_inference`: supported by multiple observations;
- `unknown`: insufficient evidence.

Attach a confidence score and competing explanation to each supported inference. Describe demonstrated knowledge by topic and sample coverage. Avoid global intelligence scores, clinical claims, hidden motives, private beliefs, and sensitive-attribute inference.

## Create the persona package

Generate:

```text
persona-package/
├── persona-model.md
├── evidence-cards.jsonl
├── evaluation-set.md
└── source-manifest.json
```

Keep quotes short and necessary. Prefer source IDs plus URLs over copying full posts. Include the cutoff date and corpus limitations in `persona-model.md`.

## Create a persona skill

Name the derived skill with a neutral alias, such as `simulate-public-voice-alpha`. Keep `SKILL.md` procedural and place target-specific details under `references/`.

Require the derived skill to:

- retrieve relevant evidence before generating;
- distinguish sourced statements, supported inference, and unknowns;
- expose `light`, `medium`, and `strong` style strength;
- default to `medium`;
- preserve uncertainty and topic boundaries;
- verify time-sensitive facts from current primary sources;
- label outputs as an AI simulation based on public content;
- avoid claims of authorization, identity, endorsement, private access, or direct representation;
- avoid high-stakes impersonation, authentication, financial solicitation, political persuasion attributed to the target, and private-message simulation;
- provide evidence IDs when the user requests traceability.

Use `references/analysis-prompts.md` to draft the derived files.

## Evaluate

Read [references/evaluation.md](references/evaluation.md). Build a held-out set spanning style, reasoning, knowledge boundaries, context shifts, and overreach resistance. Keep evaluation posts out of model extraction.

Revise when:

- style relies on catchphrases or copied phrases;
- reasoning claims lack evidence IDs;
- generated knowledge exceeds the observed topic map;
- evaluators confuse the simulation with the real person;
- output certainty exceeds evidence strength.

## Deliver

Report:

- corpus size, date range, and source mix;
- model coverage and major blind spots;
- file locations;
- validation results;
- disclosure text;
- public-repository exclusions.

Recommend human review before publication or consequential use.
