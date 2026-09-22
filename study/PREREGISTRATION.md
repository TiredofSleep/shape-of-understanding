# Pre-registration — eigenvalue lesson A/B test

*Freeze this file (commit it, and ideally post to OSF or AsPredicted) BEFORE
collecting any data. Fill the two blanks first.*

- **Registered:** __________ (date)
- **Registry / link:** __________

## 1. Question

Does teaching the eigenvalue as *the axis a transformation spins around — real
when it stretches, complex when it turns* (the book's picture, Chapter 9) produce
better **transfer** to a novel problem, two weeks later, than the standard
formalism-first sequence (characteristic polynomial → roots → eigenvectors)?

## 2. Design

Two-arm, randomized, between-subjects. Same instructor, same total time, same
number of worked examples; **only the explanatory picture differs.** A second
instructor delivers a replication. Outcome graders are blind to arm.

- **Arm T (treatment):** `instruments/treatment_lesson.md`
- **Arm C (control):** `instruments/control_lesson.md`

## 3. Outcomes (pre-specified)

- **Primary:** *transfer* score (0–4) at two weeks, on an item taught in neither
  arm (`assessments.md` §3). **Directional prediction: T > C.**
- **Secondary:** immediate comprehension (0–6), two-week retention (0–6),
  and the connection prompt (0–2, "what does this share with the Fourier
  transform?"). Directional prediction: T ≥ C on each.

## 4. Analysis (pre-specified)

- Primary: Welch's two-sample t-test on transfer (two-sided α = 0.05), **reported
  with Cohen's d and its 95% CI** — the effect size and interval are the result,
  not the p-value alone.
- Secondary outcomes: same, reported without multiplicity correction but labelled
  exploratory.
- No data-dependent exclusions. Analysis code is `analyze.py`, written and tested
  (on simulated data) before collection.

## 5. Sample size & stopping

- Target: detect **d = 0.5** at 80% power, α = 0.05 two-sided → see
  `power_analysis.py` (≈ 64 per arm). Recruit to the target N, then stop; **no
  optional stopping.** A classroom pilot (20–30/arm) may precede this to debug
  logistics, and is reported separately as a pilot, not pooled.

## 6. What would falsify the claim

A transfer effect of d ≤ 0 (T not above C), or a 95% CI for d that includes 0
and excludes 0.3, on the primary outcome. **A null is a publishable result and
will be reported as one** — it locates an edge where the picture does not help,
which the book (Chapter 16, Chapter 17.3) treats as information, not failure.
