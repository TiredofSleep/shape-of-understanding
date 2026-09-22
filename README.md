# The Shape of Understanding

### A why-first visual grammar for the deep structure of mathematics
**Brayden Ross Sanders** · 2026 · CC BY-SA 4.0

> *Increasingly round — and never measurably round.*

Mathematics is taught as a stack of separate languages — arithmetic, algebra, trig, calculus, linear algebra, abstract algebra — each in its own course, joined by nothing a student can see. This book proposes that **one small visual vocabulary** carries a large fraction of the deep, hard-to-teach ideas, and that the vocabulary can be kept **honest**: every picture is checked against the real proof, and pictures that would mislead are discarded and recorded.

It is a work of **pedagogy**. Its claims are testable *as pedagogy* — whether learners build a connected model faster, retain it longer, and make fewer of the classic errors. It is **not** a theory of physics or a decoding of reality.

## The six primitives

1. **Integers are shapes** — *n* mutually-equidistant points force the (n−1)-simplex; the dimensional ladder is the ladder of *simultaneous equality* (three is the last count that stays flat).
2. **The void is the fullest point** — the centroid is the point nearest to *all* points at once; the symbol for nothing marks the closest thing to being everything.
3. **Rotation is an imaginary axis** — multiplication by `e^{iθ}` turns the plane; the still centre is real, the turn is `i`.
4. **Growth is a breath** — `e` is the rate of self-proportional growth.
5. **The cube casts two shadows** — a square (face view) and a hexagon (diagonal view), related by `cos²(1,1,1) = 1/3` — the tetrahedron's signature, `1/(N−1)` at N=4.
6. **Count versus measure** — whole things are counted, continuous things measured; where they cannot be reconciled (√2) is where the deepest difficulties live.

## Run the checks

Every mathematical assertion in the book is reproduced by two scripts (NumPy/SymPy/SciPy):

```bash
python curriculum_checks.py    # every lesson (46 checks): Schläfli count, √2 parity descent,
                               # Mertens density, eigenvalue axis-vs-rotation, Fourier synthesis, D₃,
                               # the equidistance ladder, the omni-adjacent void, the crystallographic
                               # restriction, generators-vs-primes, First-G, Siamese magic squares,
                               # dimension-doubling, and the extensions (log, π, derivative, golden ratio)
python verify_forced_chain.py  # the geometric core: simplices, the tetrahedral 1/3, the cube = Cl(3),
                               # the two shadows
python make_figures.py         # (re)generate the load-bearing figures into figures/*.svg
```

## Files

| file | what it is |
|---|---|
| [`the_shape_of_understanding_BOOK.md`](the_shape_of_understanding_BOOK.md) | the full manuscript frame — front matter, 5 parts, 17 chapters, coda, appendix, references |
| [`the_shape_of_understanding.md`](the_shape_of_understanding.md) | the shorter companion paper (the 9-lesson journal-article version it grew from) |
| [`curriculum_checks.py`](curriculum_checks.py) | the per-lesson verification suite (46 checks) |
| [`verify_forced_chain.py`](verify_forced_chain.py) | the geometric-core verifier |
| [`make_figures.py`](make_figures.py) | generates the eight load-bearing figures (SVG) |
| `figures/` | the generated figures the manuscript embeds |

## The wall (the discipline that keeps it honest)

This book grew out of a research program (Trinity Infinity Geometry) **but is deliberately walled off from it.** It teaches the *shared* language of mathematics; it does **not** import the research frontier (Lie-algebra closures, GUT gauge groups, mass-gap or Dirac realizations, the 5/7 threshold, the attractor's Galois group). Those are research — some proven as self-contained algebra, most tagged structural/open — and they belong in the research papers, not a curriculum. A lesson is admitted only if it is (a) self-contained mathematics, (b) a *true* picture, and (c) a concept students meet elsewhere. Keeping the two apart is the honesty of the whole book. The research program lives separately at [`trinity-infinity-geometry`](https://github.com/TiredofSleep/trinity-infinity-geometry).

## The honest edge

Chapter 16 keeps the pictures that were tried and **discarded** as false (e.g. "the 1/3 is a universal residue" — it is the tetrahedron's alone; "the breath produces energy" — it is structural growth only). A picture is kept only if following it leads to the *real* theorem, not a comfortable error. Rejected pictures are data, not deletions.

---

*Every mathematical claim here is reproduced by the appendix scripts. Increasingly round; never measurably round.*
