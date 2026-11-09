# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 14:46
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `37453d45-9837-48e4-a8e6-a801b46d8acf` | human | 0.277 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `dd172ba3-1dfc-4896-8a8e-a8f26b60f633` | unsure | 0.430 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `3171c8ed-e594-4e0b-9d4a-7535fa24c6a4` | unsure | 0.520 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `74ea4912-70f1-40f2-b490-5140caea911f` | unsure | 0.536 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e2a67702-fd3d-44b0-a80c-1e46eb28c2d0` | human | 0.288 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c96fa58b-75bc-4e71-b06f-41131af365cf` | unsure | 0.469 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `76c20fe5-bf66-44a4-a9f8-70a946e921a4` | unsure | 0.527 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `f4fff7b9-1eea-4513-b4f7-5a9677bef72a` | human | 0.246 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `e28e4263-4180-4334-b1eb-2122000c127a` | unsure | 0.547 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `9e08ad40-87bc-41f4-9357-5f5ce21b4be1` | ai | 0.906 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `1563aa18-94d8-4dc8-aa06-20884f3d9c54` | unsure | 0.568 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `376f3b62-ca6a-4d68-bc1c-9195aa277fd0` | ai | 0.676 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `4138587e-7537-4079-a2db-fde446e0e949` | ai | 0.709 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `989a71b2-21f2-4931-8165-0b539bff1422` | unsure | 0.626 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `3ae3ae72-c370-4256-96b1-d2a618b90403` | ai | 0.732 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `29bfaa74-dd67-463d-af04-816707e56535` | ai | 0.658 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `4912cd15-8093-42a2-b8d8-ad3d8ef0b11b` | ai | 0.666 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `4ce2ecc5-9162-4712-9dd5-ca4255d9c3ee` | human | 0.263 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `655ab2e5-7442-41a4-a41a-1decc6f6b64a` | unsure | 0.363 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `d7c87cf7-4126-4c12-8a93-cb6fb30aab82` | human | 0.166 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `076d9a7c-54cc-40fd-a198-4a6a1b8d3bfe` | unsure | 0.516 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `d1ae3fed-51a9-4b20-8e90-ba0cf127f486` | unsure | 0.457 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `d394d0a9-b52f-426a-95d0-a1e0f22018af` | unsure | 0.457 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `af0bfb6e-0508-4904-a19a-2b0ef2fe2160` | unsure | 0.535 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `d93972ad-e6de-40f4-8461-a48efc4af33c` | human | 0.313 |  |
| MF04 | malformed | text is only punctuation | 200 | `82f447ee-0def-432f-a42b-589edce00c1a` | unsure | 0.425 |  |
| MF05 | malformed | text is a very long single word | 200 | `d370492b-6589-4972-8ba8-c9b687a1a7d2` | ai | 0.865 |  |
| MF06 | malformed | text is emoji only | 200 | `160db707-b851-4c11-89e7-3eab81cea0ce` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `54cfd6ca-c33f-49c8-8890-18dc6f43d7e5` | ai | 0.944 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `aba72311-1345-4467-a32e-5a4dc828a2f2` | human | 0.350 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `d17fb0fd-0622-4946-8c9a-2c070eb2a9b8` | human | 0.163 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `af440fc9-d39a-4238-91b4-915f10618118` | human | 0.268 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `76aab171-8443-403c-a5ee-f9bdf8f967cc` | human | 0.268 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `211bf495-b381-4536-a45f-e7178dc739c5` | human | 0.268 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `21d3f9cc-4371-4921-9840-a6da329f482b` | human | 0.268 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `54135747-cd9c-4c4b-aa23-288b8a4cf830` | human | 0.268 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "37453d45-9837-48e4-a8e6-a801b46d8acf",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.2767,
  "model_score": 0.1635,
  "style_score": 0.4466,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "dd172ba3-1dfc-4896-8a8e-a8f26b60f633",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4301,
  "model_score": 0.5943,
  "style_score": 0.1401,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "3171c8ed-e594-4e0b-9d4a-7535fa24c6a4",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5205,
  "model_score": 0.6662,
  "style_score": 0.3019,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "74ea4912-70f1-40f2-b490-5140caea911f",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5357,
  "model_score": 0.6114,
  "style_score": 0.4221,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "e2a67702-fd3d-44b0-a80c-1e46eb28c2d0",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.288,
  "model_score": 0.3212,
  "style_score": 0.2383,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c96fa58b-75bc-4e71-b06f-41131af365cf",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.469,
  "model_score": 0.5727,
  "style_score": 0.3134,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "76c20fe5-bf66-44a4-a9f8-70a946e921a4",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5273,
  "model_score": 0.5862,
  "style_score": 0.439,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "f4fff7b9-1eea-4513-b4f7-5a9677bef72a",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.2456,
  "model_score": 0.2452,
  "style_score": 0.2463,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "e28e4263-4180-4334-b1eb-2122000c127a",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5468,
  "model_score": 0.7042,
  "style_score": 0.3107,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "9e08ad40-87bc-41f4-9357-5f5ce21b4be1",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9059,
  "model_score": 0.9792,
  "style_score": 0.7959,
  "label": "This looks like it was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "1563aa18-94d8-4dc8-aa06-20884f3d9c54",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5681,
  "model_score": 0.6175,
  "style_score": 0.494,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "376f3b62-ca6a-4d68-bc1c-9195aa277fd0",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6761,
  "model_score": 0.7387,
  "style_score": 0.5823,
  "label": "This looks like it was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "4138587e-7537-4079-a2db-fde446e0e949",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7091,
  "model_score": 0.8051,
  "style_score": 0.565,
  "label": "This looks like it was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "989a71b2-21f2-4931-8165-0b539bff1422",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6262,
  "model_score": 0.8329,
  "style_score": 0.3951,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "3ae3ae72-c370-4256-96b1-d2a618b90403",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7323,
  "model_score": 0.8005,
  "style_score": 0.6301,
  "label": "This looks like it was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "29bfaa74-dd67-463d-af04-816707e56535",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6584,
  "model_score": 0.8814,
  "style_score": 0.4228,
  "label": "This looks like it was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "4912cd15-8093-42a2-b8d8-ad3d8ef0b11b",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6657,
  "model_score": 0.8816,
  "style_score": 0.4453,
  "label": "This looks like it was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "4ce2ecc5-9162-4712-9dd5-ca4255d9c3ee",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.2633,
  "model_score": 0.3223,
  "style_score": 0.1748,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "655ab2e5-7442-41a4-a41a-1decc6f6b64a",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3629,
  "model_score": 0.4625,
  "style_score": 0.2136,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "d7c87cf7-4126-4c12-8a93-cb6fb30aab82",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1657,
  "model_score": 0.2044,
  "style_score": 0.1076,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "076d9a7c-54cc-40fd-a198-4a6a1b8d3bfe",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5163,
  "model_score": 0.5943,
  "style_score": 0.3994,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "d1ae3fed-51a9-4b20-8e90-ba0cf127f486",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4571,
  "model_score": 0.4998,
  "style_score": 0.393,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "d394d0a9-b52f-426a-95d0-a1e0f22018af",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4573,
  "model_score": 0.6401,
  "style_score": 0.1565,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "af0bfb6e-0508-4904-a19a-2b0ef2fe2160",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.535,
  "model_score": 0.5583,
  "style_score": 0.5,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "d93972ad-e6de-40f4-8461-a48efc4af33c",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.3133,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "82f447ee-0def-432f-a42b-589edce00c1a",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.4254,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "d370492b-6589-4972-8ba8-c9b687a1a7d2",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8652,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "This looks like it was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "160db707-b851-4c11-89e7-3eab81cea0ce",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9981,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "This looks like it was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "54cfd6ca-c33f-49c8-8890-18dc6f43d7e5",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9438,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "This looks like it was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "aba72311-1345-4467-a32e-5a4dc828a2f2",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.3498,
  "model_score": 0.2395,
  "style_score": 0.5152,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "d17fb0fd-0622-4946-8c9a-2c070eb2a9b8",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.1628,
  "model_score": 0.0492,
  "style_score": 0.3333,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "af440fc9-d39a-4238-91b4-915f10618118",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2679,
  "model_score": 0.0287,
  "style_score": 0.4815,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "76aab171-8443-403c-a5ee-f9bdf8f967cc",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2679,
  "model_score": 0.0287,
  "style_score": 0.4815,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "211bf495-b381-4536-a45f-e7178dc739c5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2679,
  "model_score": 0.0287,
  "style_score": 0.4815,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "21d3f9cc-4371-4921-9840-a6da329f482b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2679,
  "model_score": 0.0287,
  "style_score": 0.4815,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "54135747-cd9c-4c4b-aa23-288b8a4cf830",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2679,
  "model_score": 0.0287,
  "style_score": 0.4815,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
