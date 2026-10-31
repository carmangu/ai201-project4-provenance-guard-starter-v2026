# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---

## 1. Of my own 10 pieces, at most 1 is labelled high-confidence AI — in every trial

Of 10 pieces I wrote myself, at most 1 is labelled high-confidence AI, in each
of three trials.

**Why this target:**
On a writing site a wrong accusation costs the writer far more than a missed AI
text costs the site. 1-in-10 is a ceiling, not a goal — it accepts the first
signal's structural blind spot (plain writers get accused) while leaving usable
detection power. It has to hold in all three trials because the model signal
jitters; passing once is not passing.

---

## 2. Clearly-AI and clearly-human text score at least 0.30 apart — in every trial

Using four calibration inputs (clearly AI, clearly human, plain human,
lightly-edited AI), the combined score of the clearly-AI input is at least 0.30
higher than the clearly-human input, in each of three trials.

**Why this target:**
If the two ends don't separate, the labels are being assigned on noise. A 0.30
gap requires both signals to carry different information and the combining rule
not to flatten that difference. It is a floor for "the signals do something",
not a claim about detection quality.

---

## 3. All three labels appear at least once — in every trial

Across the label-coverage inputs, each of the three labels (high-confidence
human, unsure, high-confidence AI) appears at least once in each of three
trials.

**Why this target:**
An unreachable label is a product state that does not exist. `config.py` warns
that while `style_signal` is still the stub returning 0.5, the combined score
cannot leave 0.25–0.75, and the human label needs a model score below 0.20 to
be reachable at all. This criterion forces M4 to make `style_signal` actually
vary — `scoring.label_ranges()` prints the bands, but a band existing is not the
same as a band being reachable, and this tests the latter.

---

## 4. Every appeal on a real content_id adds an under_review entry and leaves the original intact

For each of 5 different real `content_id`s, an appeal adds a new log entry with
`status: "under_review"` and leaves the original decision entry unchanged — 5 of
5, in each of three trials.

**Why this target:**
The appeal is the only thing standing between a wrong accusation and no
recourse at all. The original not being overwritten is the point of an
append-only audit log: you can see what was decided, that it was challenged, and
in what order. 5-of-5 rather than "most", because a failed appeal is
catastrophic for that writer — there is no partially working appeal path.

*Tested by hand (submit then appeal) or by extending `run_eval.py`; say which in
the README.*

---

## 5. Four kinds of bad input are rejected with 4xx and logged — never 5xx

Each of: missing `text`, empty `text`, `text` = null, and a 50,000-word `text`
returns a 4xx status, never a 5xx and never a crash, and each rejection writes a
`rejected` entry to the audit log — in each of three trials.

**Why this target:**
Crashing on a malformed input is one of the most common real failures there is,
and unit 8's attack set goes straight at it. 4xx rather than 500 means "I
expected this and refused it", not "I fell over". Requiring the rejection to be
logged is because an attack that shows up only as an absence is one you never
find — a refused request that left no trace looks exactly like a quiet
afternoon

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
