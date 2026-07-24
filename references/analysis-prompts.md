# Analysis prompts

Replace bracketed variables before use. Run each stage on normalized target-authored content and retain source IDs.

## 1. Language fingerprint

```text
Analyze the public language fingerprint of [ALIAS] from [CORPUS].

Measure vocabulary, sentence length, openings, transitions, endings, punctuation,
humor, emotional intensity, rhetorical devices, language switching, and audience
adaptation. Separate stable traits from topic-specific and platform-specific traits.

For every finding provide:
- finding
- evidence_ids: at least 3 when available
- confidence: 0.00–1.00
- contexts
- competing_explanation
- overfitting_risk

Finish with executable generation rules. Preserve natural variation and avoid copying
distinctive passages.
```

## 2. Public reasoning model

```text
Analyze [ALIAS]'s publicly demonstrated reasoning patterns from [CORPUS].

Map recurring questions, evidence preferences, inference sequences, analogies,
heuristics, uncertainty handling, disagreement behavior, risk weighting, time horizon,
value priorities, and documented belief updates.

Classify each claim as explicit, supported_inference, or unknown. Attach evidence_ids,
confidence, applicable contexts, and at least one competing explanation. Describe only
patterns demonstrated by the supplied corpus.
```

## 3. Topic knowledge map

```text
Build a topic-by-topic map of knowledge demonstrated in [CORPUS].

For each topic report observation count, date coverage, concept diversity, factual
density, reasoning depth, uncertainty awareness, representative evidence_ids, and
confidence. List questions the corpus supports, questions requiring clarification, and
questions outside observed coverage. Use "sample insufficient" for sparse topics.
```

## 4. Evidence cards

```text
Convert validated findings into JSONL evidence cards with:
id, layer, claim, evidence_ids, source_urls, contexts, confidence,
competing_explanation, first_observed_at, last_observed_at.

Use layers: language, reasoning, knowledge, values, interaction, boundary.
Create only cards supported by the corpus.
```

## 5. Persona specification

```text
Compile the language fingerprint, reasoning model, topic map, and evidence cards into
a reusable public-persona specification.

Include:
1. role definition and cutoff date
2. corpus coverage and limitations
3. language rules
4. reasoning procedure
5. topic knowledge boundaries
6. context-dependent behavior
7. uncertainty policy
8. style strength: light, medium, strong
9. retrieval procedure for evidence cards
10. AI-simulation disclosure
11. restricted and high-risk uses
12. evaluation criteria

Make each operational rule traceable to evidence-card IDs.
```

## 6. Derived skill generator

```text
Create a Codex skill named [DERIVED_SKILL_NAME] from [PERSONA_SPECIFICATION].

Generate only:
- SKILL.md
- agents/openai.yaml
- references/persona-model.md
- references/evidence-cards.jsonl
- references/evaluation-set.md
- references/source-manifest.json

Keep raw corpus data outside the skill. Use a neutral alias. Require evidence retrieval,
uncertainty preservation, current-fact verification, AI-simulation disclosure, and
topic boundaries. Avoid identity or authorization claims. Output complete file contents.
```
