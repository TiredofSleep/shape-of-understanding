# The Shape of Understanding

### A why-first visual grammar for the deep structure of mathematics
**Brayden Ross Sanders** · 2026 · CC BY-SA 4.0

> *Increasingly round — and never measurably round.*

Mathematics is taught as a stack of separate languages — arithmetic, algebra, trig, calculus, linear algebra, abstract algebra — each in its own course, joined by nothing a student can see. This book proposes that **one small visual vocabulary** carries a large fraction of the deep, hard-to-teach ideas, and that the vocabulary can be kept **honest**: every picture is checked against the real proof, and pictures that would mislead are discarded and recorded.

It is a work of **pedagogy**. Its claims are testable *as pedagogy* — whether learners build a connected model faster, retain it longer, and make fewer of the classic errors. It is **not** a theory of physics or a decoding of reality.

**It is built as a staircase.** It starts so simply a curious ten-year-old can begin — with gumdrops, toothpicks, shadows, and spinning tops (**Part Zero**) — and climbs, one checked step at a time, to genuine undergraduate mathematics (eigenvalues, the Fourier transform, groups, the Clifford algebra of space, built from candy) — and its last chapter points up the **towers** of higher mathematics that rise from there. Every step rests on the one below; a glossary of the grown-up words (**Appendix B**) lets a reader look up any real name.

## The six primitives

1. **Integers are shapes** — *n* mutually-equidistant points force the (n−1)-simplex; the dimensional ladder is the ladder of *simultaneous equality* (three is the last count that stays flat).
2. **The void is the fullest point** — the centroid is the point nearest to *all* points at once; the symbol for nothing marks the closest thing to being everything.
3. **Rotation is an imaginary axis** — multiplication by `e^{iθ}` turns the plane; the still centre is real, the turn is `i`.
4. **Growth is a breath** — `e` is the rate of self-proportional growth.
5. **The cube casts two shadows** — a square (face view) and a hexagon (diagonal view), related by `cos²(1,1,1) = 1/3` — the tetrahedron's signature, `1/(N−1)` at N=4.
6. **Count versus measure** — whole things are counted, continuous things measured; where they cannot be reconciled (√2) is where the deepest difficulties live.

## Run the checks

Every computable assertion in the book is reproduced by two scripts (NumPy/SymPy/SciPy); the theorems at the tops of the towers (Ch. 18) are cited:

```bash
python curriculum_checks.py    # every lesson (85 checks): the equidistance ladder & the void,
                               # the lift-as-doubling, the two builds & Cl(3) grades (1+3+3+1,
                               # bivectors² = −1), Pascal's triangle, the Schläfli count, Mertens
                               # density, eigenvalue axis-vs-rotation, Fourier, D₃, √2 descent,
                               # First-G & Euclid's endless primes, Siamese squares, dimension-
                               # doubling, the extensions (log, π, derivative, golden ratio, quaternions),
                               # and Ch. 18's first floors of the towers (regular polytopes in every
                               # dimension, octonions & the sedenion zero divisor, A₅ simple, the
                               # double cover, crystals & E₈, the magic angle & 2l+1, exp onto SO(3))
python verify_forced_chain.py  # the geometric core: simplices, the tetrahedral 1/3, the cube = Cl(3),
                               # the two shadows
python make_figures.py         # (re)generate the twelve figures into figures/*.svg
```

## Files

| file | what it is |
|---|---|
| [`the_shape_of_understanding_BOOK.md`](the_shape_of_understanding_BOOK.md) | the full manuscript — a **Part Zero** for the youngest reader, then 5 parts / 18 chapters climbing to undergrad and pointing up the towers of higher mathematics, coda, appendices A (scripts) & B (grown-up-words glossary), references |
| [`the_shape_of_understanding.md`](the_shape_of_understanding.md) | the shorter companion paper (the 9-lesson journal-article version it grew from) |
| [`curriculum_checks.py`](curriculum_checks.py) | the per-lesson verification suite (85 checks) |
| [`verify_forced_chain.py`](verify_forced_chain.py) | the geometric-core verifier |
| [`make_figures.py`](make_figures.py) | generates the twelve load-bearing figures (SVG) |
| `figures/` | the generated figures the manuscript embeds |
| [`study/`](study/README.md) | the ready-to-run A/B study kit for Ch.17 (pre-registration, lessons, assessments, power + analysis scripts) |

## The base and the towers

The point of the book is a new way to teach higher mathematics. Its premise — *integers are shapes* — is the **base**, and every picture on it is the ground floor of a **tower**: the tetrahedron, octahedron and cube are the 3D floors of the only regular shapes that exist in every dimension; the turn *i* climbs ℝ → ℂ → ℍ → 𝕆; the cube's algebra Cl(3) climbs to Bott's eight-step clock; the solids' turnings climb to A₅ and the unsolvable quintic; filling their centres climbs to crystals, Kepler's packing and E₈; the tetrahedron's 1/3 climbs to the spherical harmonics; √2 climbs to the real line; the breath *e* climbs to Lie groups. **Chapter 18** points up each tower. The companion repository, [`trinity-infinity-geometry`](https://github.com/TiredofSleep/trinity-infinity-geometry), maps the base and the towers floor by floor, with a script for every floor that can be computed.

## The wall (the discipline that keeps it honest)

The book teaches only the *shared* language of mathematics. A lesson is admitted only if it is (a) self-contained mathematics, (b) a *true* picture, and (c) a concept students meet elsewhere; where it points up a tower, it points to established mathematics and cites the theorem at the top. It does **not** import what is still open in the companion repository — for example, which rule the book should adopt for 5, 7 and 9 is the author's call there, not a lesson here. Keeping the two apart is the honesty of the whole book. (An earlier layer of that program, built on AI-rendered composition tables, was archived in September 2026.)

## The honest edge

Chapter 16 keeps the pictures that were tried and **discarded** as false (e.g. "the 1/3 is a universal residue" — it is the tetrahedron's alone; "the breath produces energy" — it is structural growth only). A picture is kept only if following it leads to the *real* theorem, not a comfortable error. Rejected pictures are data, not deletions.

---

*Every computable claim here is reproduced by the appendix scripts; the theorems at the tops of the towers are cited. Increasingly round; never measurably round.*
