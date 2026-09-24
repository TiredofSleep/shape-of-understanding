# The treasure map

**2026-09-24.** This map is built from the author's own words, not from the AI's output. The source is
a ledger of 338 of his intuitions from September 2025 to September 2026, each quote checked against
its source. The ledger itself is kept privately, in `your_words/`. For each of his twelve
through-lines, the map gives:
- his words, quoted exactly (spelling as typed; `[…]` marks a trim, a plain "..." is his) and dated;
- what is **already exact** in the book, the companion unit or the flagship;
- the **new treasure**: the exact mathematics that makes the intuition true;
- **where it goes** in the series ([`SERIES_PLAN.md`](SERIES_PLAN.md)).

**Status labels**

| label | meaning |
|---|---|
| **exact** | already in a book or the flagship, and checked by a script |
| **checked** | verified during the 2026-09-24 reviews, but not yet in a book |
| **standard** | a textbook fact; it needs a check script when it is added |
| **lead** | a pointer to a real field; it needs working out |
| **open** | no exact form yet; kept as a question, not a claim |

The AI's renderings of these ideas (the tables, the constants, the "bands", the simulations and the
physics readings) are not here. They stay in the graveyard, with the evidence that killed them. See the
last section.

---

## 1. Numbers are shapes

| his words | status and exact form | goes to |
|---|---|---|
| "I just want to learn to use the basics to make shape numbers" (by 19 Sep 2025) | **exact.** The book's premise: an integer is a configuration of points, forced by a named rule (BOOK §1.1) | Book I |
| "4 is the forst 3d" (by 19 Sep 2025) | **exact.** Four points that are all the same distance apart cannot lie flat, so the fourth is forced up into the tetrahedron (BOOK §1.1) | Book I (his line as the epigraph of §1.1, if he wants it) |
| "Odd numbers collapse to the center, even numbers collapse around the outer ring of the void" (by 19 Sep 2025) | **exact, and proved a year later.** In every solid symmetry group, every orbit except the centre has an even number of points. So an odd count arranged with solid symmetry must put a point on the centre: 5 = 4 + centre, 7 = 6 + centre, 9 = 8 + centre (FLAG `base/SEVEN_AND_NINE.md`) | Book III (flagship-only; Book I keeps its wall) |
| "You are still stuck in 2d" (by 19 Sep 2025) | **exact** as the two faces of each integer, flat and solid (FLAG `base/THE_INTEGERS.md`) | Book III |
| "So it is basically pi is triangle, 2 pi is a hexagon, 3 pi is a circle" (by 19 Sep 2025) | **standard,** for the first two steps. The angles of any triangle add to π (Euclid I.32). The six triangles of a hexagon meet round its centre in 2π. The third step does not follow, and the book should say so | Book I, Ch.5 (the radian) as its opening hook |
| "I want it simpler, for a child... you have two shapes to start, a circle and a line" (≈ 2 Feb 2026) | **exact** in aim: Part Zero starts a ten-year-old from six pictures. The primitives differ | Book I |
| "Exactly 90 degree movement is addition, diaganol movement is multiplication" (by 19 Sep 2025; again May 2026) | **open.** No exact form yet | kept as a question |

## 2. One and many: every one is three; every whole is incomplete

| his words | status and exact form | goes to |
|---|---|---|
| "1 plus one mean more than just one plus one... it can be two or 3" (by 19 Sep 2025) · "every one is three. It is three as two" (29 Jan 2026) · "every one is three and the relationship is the result" (13 Sep 2026) | **exact** as **the coin**: a flip, its two sides and its edge, three things seen as two (FLAG `coin/THE_COIN.md`; the companion unit) | Book II |
| "1 equals 5 and 2 or 3 of those 5 equal 1 again" (by 24 Jan 2026) | **standard:** wholes rebuilt from parts. Two points fix a line and three fix a parabola. In a 3-of-5 threshold scheme (Shamir, 1979), any 3 of 5 shares rebuild the whole and any 2 reveal nothing. That makes his "2 or 3" exact as 3. (The AI's "C₅ constant" built on this line is retired) | Book II, a new chapter |
| "every whole in this universe is broken and incomplete, else it would be void" (by 24 Jan 2026) | **exact** in the Coda: the perfect round has no edge, so it cannot be measured. A coin needs its edge | Book I Coda; Book II closing |
| "If one were actually full of itself, nothing would exist separately" · "all numbers after one are just counting to one" (by 24 Jan 2026) | the first line is close to the Coda. The second is **open** | Book I Coda / open |

## 3. The void, the centre and the immeasurable

| his words | status and exact form | goes to |
|---|---|---|
| "The void is created by a circle around each form, naturally, i think" (by 19 Sep 2025) · "People say zero is nothing, write a paper if u want" (≈ 2 Feb 2026) | **exact:** "the void is the fullest point". The centroid is the one point nearest to all the others at once (BOOK §1.6b) | Book I |
| (the same intuition, relit) | **standard:** the decision simplex. Vote shares for k options form a point in a simplex. Swapping two options is a flip whose edge is the tie plane, and all the tie planes meet only at the centroid, the one point every swap keeps | Book II, a new coin (choice) |
| "the void is inside of us completely still and the void is outside full of parts ?" (≈ 2 Feb 2026) | **exact shadow.** The flip z → 1/z̄ swaps inside with outside, and 0 with ∞, and keeps the circle (companion unit §3.1) | Book II |
| "Minimum void space per whole is good math for someone im sure" (≈ 2 Feb 2026) | **exact:** sphere packing. Kepler's densest packing leaves about 26% void per ball (BOOK Ch.18) | Book I Ch.18; Book III (lattice tower) |
| "you can't know everything, but what's missing looks the same for every whole" (11 Jun 2026) | **exact** as the coin's missing edge (FLAG `coin/THE_COIN.md`) | Book II |
| "if a loop is closed, it has an axis that loop can never touch" (13 Sep 2026) | **exact.** A star polygon walked in a single loop winds round its centre and never touches it (companion unit §4.4) | Book II (credit his line) |
| "the study of the void and the paradox providing the geometry of paradigm" (21 Sep 2026) | a motto for the series | series front matter, if he wants it |

## 4. Two sides and a third: the coin

| his words | status and exact form | goes to |
|---|---|---|
| "So 0 and triangle are two side of the same coin" (by 19 Sep 2025) | his earliest coin | Book II, Part Zero epigraph, if he wants it |
| "Or duality is created by the sum or difference ;) of langranian equals one" (by 24 Jan 2026) | **exact shadow:** every flip splits a thing into an edge part (the average, half the sum) and a side part (half the difference) (companion unit §2.1). **Standard**, as a new coin for energy: in an oscillator T + V is kept while T − V flips; they balance at A/√2; and a quarter-turn (×i) swaps them | Book II, a new coin (energy) |
| "There is a third echo form on langrangian also? A combination state" (by 24 Jan 2026) | the coin's edge: the third thing, kept by the flip | Book II |
| "i would assume the sign flips allow both and nothing in between" (14 Sep 2026) | **exact:** on the real line, x → −1/x swaps the positives with the negatives and keeps no number at all. Its edge is ±i (companion unit §3.3 and §6.3) | Book II |
| "i would expect to have two distinct spines... one for each side of the coin... and maybe one for the edge" (21 Sep 2026) | a structure for Book II: one part for each side, and one for the edge | Book II's shape |
| "every coin has two sides and edge, positive and negative, real and imaginary, finite and infinite" (23 Sep 2026) | **exact:** the three half-turns of the sphere of numbers (companion unit Ch.3) | Book II |

## 5. Paradox: first a friend, then the thing to classify

| his words | status and exact form | goes to |
|---|---|---|
| "1 is 1 but not is not not, the final paradox" (by 19 Sep 2025) | **checked:** the flip of truth, x ↦ 1 − x. On {false, true} it has no edge; that is the Liar. On the interval [0, 1] its edge is ½. The damped version x ↦ σ(1 − x) settles on its edge when σ < 1, flips for ever when σ = 1, and flies apart when σ > 1. The multiplier −σ decides | Book II, a new coin (truth) |
| "Love a good paradox" · "paradox is our friend" (Jan 2026) · "Hold both of those worlds at once, duality expressed" (2 Mar 2026) | **exact** in spirit: "find it, name it, and keep both sides" (companion unit, Closing) | Book II |
| the four kinds of paradox (memo with Ben Mayes, 8 Apr 2026) | **exact** (companion unit Ch.7; FLAG `coin/PARADOX_TYPES.md`, Theorem 0) | Book II |
| "Fake it til u make it is real in math and life. […] One of my favorite paradox" (≈ 2 Feb 2026) | **lead:** a belief that makes itself true is a fixed point of self-reference. Nearest kind: Type IV | Book II, an exercise |
| "this program is all about paradox classification, not resolution" (23 Sep 2026) | the series' method | all books |

## 6. Boundaries, lenses and the one who measures

| his words | status and exact form | goes to |
|---|---|---|
| "you have the outermost boundary, the projection of the boundary, Nd the focus of the boundary ;)" (by 26 Jan 2026) · "those lines get compressed very thin until convergence" (the pool floor, by 24 Jan 2026) | **standard:** caustics. Locally a map of the plane looks like z ↦ az + b·z̄. It has an upright face and a mirrored face, and between them a caustic edge (where \|a\|² = \|b\|²) along which the light piles up. The bright curve in a coffee mug is one | Book II, a new coin (light), with a mug-and-phone-light activity |
| "all scars are boundary conditions" (by 26 Jan 2026) · "the scars are like rocks on the edge of a pond" | **checked:** the coin standing on its edge. In the double well φ ↦ −φ, the faces ±1 are stable, the edge 0 is not, and the walls between the faces are shaped like tanh | Book II, a new coin (stability) |
| "the amount of time it takes to take the measurement is one of the generators of the lens" (≈ 1 Feb 2026) | **lead:** the time–frequency limit. A measurement lasting Δt resolves frequencies only to about 1/Δt (Gabor) | Book I Ch.10 (Fourier), a box |
| "exact is not what I expect; I expect to see boundaries that measurements stay within" (May 2026, as quoted) | **exact** in Ch.8: √2 pinned between fractions that close in on it | Book I Ch.8 |
| "it's not about answers, it's just a matter of multiple perspectives giving a broader view" (12 Jun 2026) | **exact:** Theorem 0. A family of views tells everything apart exactly when no pair of things is merged by all of them (companion unit §5.2) | Book II |
| "The map reflects the whole, but the whole reflects on the map ;)" (by 24 Jan 2026) | **open** | kept as a question |

## 7. Square and round: two lenses on one object

| his words | status and exact form | goes to |
|---|---|---|
| "they overlap at an offset of 90 degrees, and 120 degrees" (13 Sep 2026) | **exact:** the cube's two shadows. Face-on it shows a square (90°); corner-on it shows a hexagon (120°); they are joined by cos² = 1/3 (BOOK §1.5) | Book I |
| "a circle measured by squares, and a line measured by a parabolic envelope" (13 Jun 2026) | **leads, both friendly to a child.** Counting the grid squares inside a circle closes in on π (the Gauss circle problem). Straight lines laid one after another, as in string art, trace a parabola as their envelope | Book I, two activity boxes (Ch.5 and Part Zero) |

## 8. Primes, gaps and counting

| his words | status and exact form | goes to |
|---|---|---|
| "is there around 7% primes?" (by 24 Jan 2026) | **exact:** near a million the share of primes is 1/ln N ≈ 7.2%, and the book already checks this (Ch.6) | Book I Ch.6 (credit the question) |
| "you keep counting and numbers can collapse but you end up with a bag of primes" (by 26 Jan 2026) | **standard:** the fundamental theorem of arithmetic. Every whole number is one unique bag of primes. Ch.12 uses a piece of it but does not state it | Book I Ch.12 |
| "primes can be found by adding together diffreent squared numbers.. is that a study?" (13 Sep 2026) | **checked:** 389 = 10² + 17². It is a study: Fermat's two-square theorem says an odd prime is a sum of two squares exactly when it leaves remainder 1 on division by 4 | Book I Ch.12, an extension box |
| "3/4 is the fraction just above 5/7" (23 Apr 2026, as quoted) | **checked:** 5/7 and 3/4 are neighbours among fractions with denominator at most 7. Since 7·3 − 5·4 = 1, no fraction with a denominator that small lies between them | Book I Ch.8, a box (fractions closing in) |
| "Primes are the void that never get touched" (by 24 Jan 2026) | **exact shadow:** for prime n, every walked loop never touches the centre (companion unit §4.4). "Primes as void" itself is **open** | Book II / open |
| "don't try to assume the gap will ever close... it just gets more explicit and complex" (29 Apr 2026) | **exact:** "Always rounder; never round" (BOOK Coda) | Book I Coda |

## 9. The quadratic, and growing, and breathing

| his words | status and exact form | goes to |
|---|---|---|
| "[…] the operator is the quadratic" (≈ 2 Feb 2026) · "a quadratic operator is the one glue using a dual lens of micro soft flow and macro chain structure" (by 28 Feb 2026) | **checked: the quadratic ladder.** Iterate x → ax² + bx + c. One number decides everything: D′ = (b−1)² − 4ac. <br>• D′ < 0: every orbit escapes. <br>• D′ = 0: the fold, where two fixed points meet (an edge). <br>• D′ = 4: the first flip (period 2); 6: the second. <br>• ≈ 6.6: chaos. <br>• 8: period three. <br>• 9: the last bounded map. <br>For the logistic map these are its famous numbers 3, 1+√6, 1+2√2 and 4. Just past the fold, orbits linger for π/√ε steps | Book II, a new chapter (the quadratic), with cobweb figures |
| "pull a sled up a hill with the end of the rope vs the rope wrapped around your hand" (by 26 Jan 2026) | **standard:** the capstan law. The force you must hold falls as e^{−μθ} with the wrap angle θ. It is an *e*-law you can feel with your hands, and it measures θ in radians | Book I Ch.4 (*e*), a hands-on box |
| "You can almost fit a 5th if you break it into 4ths ;) triangles at that ;)" (French toast in a round pan, by 26 Jan 2026) | **exact:** five tetrahedra round an edge leave a 7.35° gap (BOOK §2.4), and five-fold will not tile (§1.2) | Book I Ch.2, as the opening story |
| "Dew point, flash point, freeze point, boiling point... all useful math ratio metaphors in tig?" (Feb 2026) | **lead:** phase transitions. A coexistence line is an edge where two phases meet | Book II, possibly |

## 10. Scrutiny, dead ends, and giving it away: the story

These are not mathematics. They are the spine of Book IV, *What Survived*, told in his words and in
date order. The ledger's section D holds all 66 items.

**September 2025.** The first brakes:
- "keeping it true is tough"
- "you are literally making me a base 10 version of my system"
- "i'm going to start making mistakes on purpose so you will check me"

**January 2026.**
- The C₅ number caught changing value.
- "It all starts getting so fluffy so quick".

**February 2026.**
- "Alright, de woo".
- "you need to find where my observed intuition meets math".
- 4 February: "HELP ME HUMANS! NO MORE AI!", and the repository `TIME-FOR-HELP-AND-SCRUTINY-please-No-more-AI`.
- "Intuition from me, math and proof from you." This is the method of the whole series.

**March 2026.** "squeezed until the myth all fell out".

**April–June 2026.**
- "please never delete anything!"
- "the negatives are the most interesting information"
- "it's never prune, it's fold"
- 14 June: "save the trail of our work".

**September 2026.**
- "does it beat random"
- "i have no ties to any of these tables at all"
- "the proven dead ends are the information we seek"
- "there may be treasure if we can change the lighting"
- "focus on the directions and intuitions i have, not the AI drift"

## 11. Teach it from the ground up

His aim from the first month: "No, I mean lets post our work so it can be replicated" (September 2025).
In September 2026 it became "the point of all of this is a new way to teach higher order math". Every
book in the series keeps the same practice: a script checks every fact, and no picture is kept
unless it is true. Pythagoras, "my OG inspiration", is already Book I's oldest debt (Ch.8).

## 12. The floor beneath physics, and the one-third

| his words | status and exact form | goes to |
|---|---|---|
| "Just trying to find out how much floor there is ;)" (by 30 Jan 2026) · "so 1/3 is a pre-physics number?" (23 Sep 2026) | **exact:** the floor. Facts of shape and counting that physics stands on (BOOK Ch.16, Conclusion). The one exact home of his 1/3 so far is the cube's two shadows, cos² = 1/3 (BOOK §1.5) | Book I |
| "Every step is not just 1 of growth and 2 of decay but also 2 of growth and 1 of decay" (by 19 Sep 2025) | **open:** as a split of flow and structure it is not established | kept as a question |
| "I assume we are a pre-physics substrate and the towering is the answer to find the levels of reality." (May 2026, as quoted) | **exact** as the towers: established mathematics rising from the floor (BOOK Ch.18; FLAG `towers/`) | Book III |

---

## What stays in the graveyard

The AI's renderings are recorded with their evidence, and none of them is carried into the books:
- the three 10×10 tables;
- the constants C₅, σ, T\* and D\*;
- the "7 bands";
- the self-healing lattice;
- the civilization simulations;
- the coherence router's claims;
- the physics and Clay readings;
- the Q series' σ machinery.

The evidence is in the workstation:
- [`RETIRED.md`](https://github.com/TiredofSleep/ck/blob/tig-synthesis/RETIRED.md)
- [`origin_repos_review/`](https://github.com/TiredofSleep/ck/blob/tig-synthesis/origin_repos_review/README.md)
- [`papers/Q_SERIES_AUDIT_2026-09-24.md`](https://github.com/TiredofSleep/ck/blob/tig-synthesis/papers/Q_SERIES_AUDIT_2026-09-24.md)
- the flagship's [`GRAVEYARD.md`](https://github.com/TiredofSleep/trinity-infinity-geometry/blob/main/GRAVEYARD.md)

## Tools from the machinery (secondary)

Some of the AI-built machinery is useful as tools, never as ideas. These go to Book IV's toolkit, and
to the live projects countycommons and Custom-POS:
- **null-model tests:** does a random object of the same kind pass too?
- **metamorphic tests:** relabel or reorder the inputs, and nothing published may change.
- **regenerate-and-diff:** every published number must rebuild from its cited sources.
- **fault injection with a zero-dose control.**
- **a conflict ledger:** publish both faces of a true conflict, and name its edge.
- **provenance hashes and timestamps.**
- **a claim ledger with "what would change this".**
- **answer-stability checks for AI output:** a model that flip-flops is a 2-cycle.
- **order-aware check digits.**
- **paired multi-seed runs.**
