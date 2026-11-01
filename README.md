# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

# What This Does

Provenance Guard is a small backend a writing site could plug into. A piece of
text goes in; a guess about who wrote it comes out, along with how confident
the system is, a plain-English label a reader actually sees, and a way for the
writer to push back.

The path a submission takes, from arriving to the label:

1. **A `POST /submit` request arrives** with `{"text": ..., "creator_id": ...}`
   — the writing, and who submitted it.
2. **The input is checked** — is `text` present, non-empty, and not enormous?
   Bad input is rejected with a 4xx before the model runs, and the rejection is
   written to the audit log.
3. **A `content_id` is generated** (`uuid`) — a unique identity the writer can
   use to appeal this decision later.
4. **Signal one reads the text for meaning** (`detector.model_signal`): a local
   language model asks how *predictable* the text is. Predictable text tends to
   be model-written, so this returns a score where higher means more likely AI.
5. **Signal two measures the text as text** (`stylometry.style_signal`):
   sentence-length spread, word variety, punctuation density — the shape of the
   writing, without reading a word of it. Also higher = more likely AI.
6. **The two scores are combined** into one confidence number
   (`scoring.combine_signals`).
7. **The number becomes a label** (`scoring.score_to_label`) — a full sentence a
   non-technical reader sees, not a bare score. One of three: high-confidence
   human, unsure, or high-confidence AI.
8. **The decision is written to the audit log** (`audit.log_decision`) as one
   JSON line in `logs/audit.jsonl` — timestamp, ids, both signal scores, the
   combined score, the label, and a status.
9. **JSON comes back** with `content_id`, `guess`, `confidence`, `label`, and
   both signal scores.

If a writer thinks the guess is wrong, they hit `POST /appeal` with the
`content_id` and their reasoning. The item moves to `under_review`, the appeal
is recorded beside the original decision in the append-only log, and nothing is
re-checked automatically — a person is now in the loop. That path matters most
for the writer who was wrongly accused; it is the only thing standing between a
wrong label and no recourse at all.

---

## Signals and Scoring

### Signal one — the model signal (`detector.model_signal`)

**What it measures:** how *predictable* the text is to a language model
(perplexity). Low perplexity ("I could have guessed this") → high AI score.
Direction: higher = more likely AI.

**Why that might differ between human and AI writing:** a model writes by
repeatedly picking the likely next word, so model-written text tends to be text
a model finds easy to predict. Human writing wanders — odd word choices, abrupt
turns, the specific rather than the typical.

**What it can't see:** predictability is not authorship. What it actually
rewards is *common words in short, ordinary sentences* — a second-language
writer sticking to safe vocabulary, a younger writer, anyone writing plainly on
purpose. The reverse also trips: dense, ornate prose full of rare words often
scores as *human*, because rare words are exactly what a model fails to
predict. In calibration, a formal human notice scored *highest* on this signal
(model_score 0.8216), above clear AI text (0.7692) — the reverse blind spot in
practice. The writers this signal is most likely to accuse are the ones with
the least room to argue back.

### Signal two — the style signal (`stylometry.style_signal`)

**What it measures:** the *shape* of the text — sentence-length spread (stdev /
mean), word variety (type-token ratio), punctuation density. No reading of
meaning. Direction after normalisation: higher = more likely AI.

**Why that might differ between human and AI writing:** generated prose tends
toward even, mid-length sentences and a narrower vocabulary band; human writing
is lumpier — a three-word sentence next to a forty-word one.

**What it can't see:** it cannot read. It has no idea what the text says.
Anything that changes the shape without changing the substance moves it —
typos, broken-up sentences, a pasted quotation. That is very cheap to do on
purpose, and Unit 8's attack set will do exactly that. It also degrades on
longer texts: in calibration the style score stayed flat at 0.40–0.48 across
four 150–250-word inputs, because its normalisation was tuned on short texts.

### The combining rule

**The rule:** a weighted average of the two signals, with a disagreement pull.
The model signal reads meaning and carries more weight (0.6); the style signal
is cheap to manipulate but covers the model's blind spot (0.4). When the two
disagree by more than 0.4, the combined score is pulled 20% toward 0.5 — two
methods disagreeing is itself uncertainty.

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.6`, `WEIGHT_STYLE_SIGNAL = 0.4`,
disagreement threshold `0.4`, pull `0.2` (all in `config.py`).

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** the
plain-human short-text input scored model 0.8311 / style 0.1985 — a split of
0.63, above the 0.4 threshold. The model found the short, plain sentences very
predictable (high AI score); the style signal found the irregular sentence
lengths and dense punctuation very human (low AI score). The rule pulls the
weighted average (0.6×0.8311 + 0.4×0.1985 = 0.5781) 20% toward 0.5, landing at
0.5624 — "unsure", which is the honest answer when the two methods disagree
this hard## Signals and Scoring

### Signal one — the model signal (`detector.model_signal`)

**What it measures:** how *predictable* the text is to a language model
(perplexity). Low perplexity ("I could have guessed this") → high AI score.
Direction: higher = more likely AI.

**Why that might differ between human and AI writing:** a model writes by
repeatedly picking the likely next word, so model-written text tends to be text
a model finds easy to predict. Human writing wanders — odd word choices, abrupt
turns, the specific rather than the typical.

**What it can't see:** predictability is not authorship. What it actually
rewards is *common words in short, ordinary sentences* — a second-language
writer sticking to safe vocabulary, a younger writer, anyone writing plainly on
purpose. The reverse also trips: dense, ornate prose full of rare words often
scores as *human*, because rare words are exactly what a model fails to
predict. In calibration, a formal human notice scored *highest* on this signal
(model_score 0.8216), above clear AI text (0.7692) — the reverse blind spot in
practice. The writers this signal is most likely to accuse are the ones with
the least room to argue back.

### Signal two — the style signal (`stylometry.style_signal`)

**What it measures:** the *shape* of the text — sentence-length spread (stdev /
mean), word variety (type-token ratio), punctuation density. No reading of
meaning. Direction after normalisation: higher = more likely AI.

**Why that might differ between human and AI writing:** generated prose tends
toward even, mid-length sentences and a narrower vocabulary band; human writing
is lumpier — a three-word sentence next to a forty-word one.

**What it can't see:** it cannot read. It has no idea what the text says.
Anything that changes the shape without changing the substance moves it —
typos, broken-up sentences, a pasted quotation. That is very cheap to do on
purpose, and Unit 8's attack set will do exactly that. It also degrades on
longer texts: in calibration the style score stayed flat at 0.40–0.48 across
four 150–250-word inputs, because its normalisation was tuned on short texts.

### The combining rule

**The rule:** a weighted average of the two signals, with a disagreement pull.
The model signal reads meaning and carries more weight (0.6); the style signal
is cheap to manipulate but covers the model's blind spot (0.4). When the two
disagree by more than 0.4, the combined score is pulled 20% toward 0.5 — two
methods disagreeing is itself uncertainty.

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.6`, `WEIGHT_STYLE_SIGNAL = 0.4`,
disagreement threshold `0.4`, pull `0.2` (all in `config.py`).

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** the
plain-human short-text input scored model 0.8311 / style 0.1985 — a split of
0.63, above the 0.4 threshold. The model found the short, plain sentences very
predictable (high AI score); the style signal found the irregular sentence
lengths and dense punctuation very human (low AI score). The rule pulls the
weighted average (0.6×0.8311 + 0.4×0.1985 = 0.5781) 20% toward 0.5, landing at
0.5624 — "unsure", which is the honest answer when the two methods disagree
this hard

### Calibration status (Unit 7)

Four calibration inputs produced a confidence range of 0.56–0.68. The
clear-AI vs clear-human gap was 0.066, below my M2 criterion 2 target of 0.30.
The formal human notice scored highest (0.675), confirming signal one's
reverse blind spot; style_score stayed flat at 0.40–0.48 because its
normalisation was tuned on short texts. This is not resolved in Unit 7 —
Unit 8 diagnoses and attempts a fix.

---

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | "We think this was probably written by a person." |
| unsure | 0.35 – 0.65 | "We're not sure who wrote this. It could be either, so we're not making a call either way." |
| high-confidence AI | 0.65 – 1.00 | "This looks like it was probably generated by AI." |

**Why I worded the "unsure" one this way:** it is the hardest of the three. It
has to admit uncertainty without sounding like an accusation, because the
person reading it may well have written every word themselves. It says "we're
not making a call" rather than "we suspect you" — the reader is told the system
does not know, not that the system doubts them.

**Reachability note (Unit 7):** across calibration inputs, confidence stayed in
0.56–0.63, so only the `unsure` label was actually reachable. The
high-confidence human and high-confidence AI labels are written and wired in,
but the score distribution kept them from appearing. This is the M4 separation
problem surfacing at the label layer; Unit 8's `run_eval` diagnoses it.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must handle a wide variety of inputs.","creator_id":"sample_user"}'
```

```json
{
  "confidence": 0.7001,
  "content_id": "13350cb1-b6c0-4030-a9a2-32d7d871b202",
  "guess": "unsure",
  "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
  "model_score": 0.8309,
  "style_score": 0.5038
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"8d9d15e5-2432-4f81-b626-3f51463d0c64","reasoning":"I wrote this myself. It is my own work."}'
```

```json
{
  "content_id": "8d9d15e5-2432-4f81-b626-3f51463d0c64",
  "message": "Your appeal has been recorded. A person will review it.",
  "ok": true,
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=6"
```

```json
{
  "count": 6,
  "entries": [
    {
      "combined_score": 0.675,
      "content_id": "519be8a4-7b3f-4c60-8f71-2f77510b1a93",
      "creator_id": "calib_human_formal",
      "guess": "unsure",
      "label": "PLACEHOLDER label (filled in at Milestone 5)",
      "model_score": 0.8216,
      "status": "decided",
      "style_score": 0.4551,
      "timestamp": "2026-11-01T07:47:56+00:00"
    },
    {
      "combined_score": 0.5624,
      "content_id": "8d9d15e5-2432-4f81-b626-3f51463d0c64",
      "creator_id": "label_human_test",
      "guess": "unsure",
      "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
      "model_score": 0.8311,
      "status": "decided",
      "style_score": 0.1985,
      "timestamp": "2026-11-01T08:20:52+00:00"
    },
    {
      "content_id": "8d9d15e5-2432-4f81-b626-3f51463d0c64",
      "creator_id": "label_human_test",
      "event": "appeal",
      "reasoning": "I wrote this myself. It is my own work.",
      "status": "under_review",
      "timestamp": "2026-11-01T08:27:29+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked for help understanding what the two signals could
and couldn't see, and for wording of the three label texts.

- *What came back:* an explanation of the model signal's blind spot (plain
writers get accused; ornate prose reads as human) and three candidate label
sentences.

- *What I changed:* I kept the blind-spot framing but rewrote the "unsure"
label myself — the first version sounded like a soft accusation ("we suspect
this may be AI"), which is exactly what the brief warns against. The version
in Label Variants says "we're not making a call" instead.

**Moment 2**

- *What I asked for:* help debugging why HF_HUB_OFFLINE didn't take effect
and the service kept trying to reach huggingface.co on startup.

- *What came back:* the explanation that app.py is a separate process and
does not inherit the variable set in another terminal.

- *What I changed:* set HF_HUB_OFFLINE=1 in the same terminal that starts
app.py, and then as a permanent user environment variable so Unit 8's
run_attacks.py and run_eval.py won't hit the same problem.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
