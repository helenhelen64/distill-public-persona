# Distill Public Persona

> 把一个人的公开动态“慢火熬制”成可复用的人格模型，而且每个判断都得带小票。

[中文](#中文介绍) · [English](#english)

## 中文介绍

有人管这叫 AI 分身，我们更愿意叫它：**带证据的数字考古**。

`distill-public-persona` 是一个 Codex Skill。它会阅读一个人的公开推文、文章、访谈或文字记录，然后分四层整理：

- **语言指纹**：常用词、节奏、句式、幽默感，以及面对不同人时怎么切换语气；
- **思考习惯**：偏爱什么证据、怎么推理、怎么处理不确定性和价值冲突；
- **知识地图**：熟悉哪些主题、聊到了什么深度、哪里属于语料盲区；
- **证据卡片**：每个判断对应哪些原文、可信度多高，还有什么其他解释。

最终可以产出一份人物分析、一个可复用的人格资料包，或者一个新的模拟 Skill。

### 它的原则

先留证据，再学语气。

```text
判断 → 证据编号 → 可信度 → 其他解释 → 适用边界
```

这样生成出来的内容既能“有那味儿”，也能说明这股味儿是从哪里来的。

### 里面有什么

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

### 快速开始

1. 把依法获取的公开内容整理成 JSONL 或 CSV。
2. 按照 `references/corpus-schema.md` 统一格式。
3. 检查语料：

```bash
python3 scripts/validate_corpus.py path/to/corpus.jsonl
```

4. 调用 Skill：

```text
Use $distill-public-persona to turn this public corpus into an
evidence-grounded persona model and evaluation set.
```

5. 原始语料放在私有数据目录，公开仓库保存通用方法、来源清单和合成示例。

### 使用边界

适合研究公开表达、写作风格、传播方式、创意模拟和教育用途。生成内容应明确标注为 AI 模拟，并尊重来源平台规则、版权、隐私、删除请求和当地法律。

派生的人格 Skill 建议使用人物代号，保留知识边界和不确定性，避开身份冒充、授权声明、私信模拟、敏感属性推断、高风险代言、金融募资和冒名政治宣传。

---

## English

Some people call this an AI clone. We prefer: **digital archaeology with receipts**.

`distill-public-persona` is a Codex Skill that studies public posts, articles, interviews, and transcripts, then organizes the findings into four layers:

- **Language fingerprint**: vocabulary, rhythm, sentence patterns, humor, and audience shifts.
- **Reasoning habits**: evidence preferences, inference patterns, uncertainty, and value trade-offs.
- **Knowledge map**: demonstrated topics, depth, date coverage, and blind spots.
- **Evidence cards**: source-linked claims with confidence scores and competing explanations.

It can produce a public-persona analysis, a reusable persona package, or a derived simulation Skill.

### The rule of the kitchen

Keep the evidence before seasoning the voice.

```text
claim → evidence IDs → confidence → competing explanation → boundary
```

The goal is recognizable flavor with a clear ingredient list.

### What is inside

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

### Quick start

1. Export or collect lawful public content as JSONL or CSV.
2. Normalize it with `references/corpus-schema.md`.
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

### Responsible use

Use the Skill for public-writing research, communication studies, education, and clearly disclosed creative simulations. Respect platform terms, copyright, privacy, deletion requests, and local law.

Derived persona Skills should use neutral aliases, preserve uncertainty and topic boundaries, disclose AI simulation, and exclude identity claims, authorization claims, private-message simulation, sensitive-attribute inference, high-stakes impersonation, financial solicitation, and attributed political persuasion.

## License

MIT
