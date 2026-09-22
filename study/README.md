# The Shape of Understanding — A/B study kit

This folder turns Chapter 17's protocol from a *description* into something a
teacher or researcher can actually run. It does **not** contain results — no
study has been run yet. It contains everything needed to run one honestly.

> **Honest status.** This is a study *kit*, not a study. The claim of the book
> ("one small visual vocabulary teaches deep mathematics faster and more
> connectedly") is testable as pedagogy, and this is the apparatus to test it.
> Until a cohort is actually run, the pedagogical claim is **unverified** — a
> hypothesis with a protocol, nothing more.

## What's here

| file | what it is |
|---|---|
| [`PREREGISTRATION.md`](PREREGISTRATION.md) | the pre-registered design: hypotheses, primary outcome, analysis plan, stopping rules. Fill in the date/registry and freeze it *before* collecting data. |
| [`instruments/treatment_lesson.md`](instruments/treatment_lesson.md) | the treatment lesson (eigenvalue as axis-vs-rotation) — the picture under test. |
| [`instruments/control_lesson.md`](instruments/control_lesson.md) | the matched control lesson (formalism-first), same length and worked-example count. |
| [`instruments/assessments.md`](instruments/assessments.md) | the four instruments (immediate / retention / transfer / connection) with scoring rubrics and answer keys. |
| [`power_analysis.py`](power_analysis.py) | computes the sample size per arm for a target effect and power. |
| [`analyze.py`](analyze.py) | runs the pre-registered analysis; ships with a simulated dataset so it runs today. |

## Run it

```bash
python power_analysis.py                 # how many students per arm you need
python analyze.py --simulate             # end-to-end on simulated data (sanity check)
python analyze.py --data results.csv      # once you have real data (same columns as the sim)
```

`results.csv` columns: `id, arm, immediate, retention, transfer, connection`
(`arm` ∈ {treatment, control}; the four scores as described in `assessments.md`).

## The discipline (same as the book's)

- **Pre-register** the primary outcome (transfer at two weeks) and the predicted
  direction *before* any data. `analyze.py` reports the effect size and its
  interval, not just a p-value.
- **Publish the null.** A clean null on the primary outcome falsifies this
  lesson's pedagogical claim — and that is a result, recorded, not buried.
- **Replicate across lessons** (√2, the group, one extension lesson) before
  claiming the *vocabulary* transfers rather than one lucky picture.
