# The series: a plan

**Working plan, 2026-09-24.**
- **It is built on the author's own intuitions,** not on the AI's drift. Its source is a ledger of 338
  of his lines from September 2025 to September 2026, each quote checked against its source. The
  ledger is kept privately, in `your_words/`.
- **The [treasure map](TREASURE_MAP.md)** places each intuition, together with the exact mathematics
  that makes it true.

> *"Intuition from me, math and proof from you."* (February 2026)

That line is the method of the whole series. Each book takes directions he has held for a year, gives
them their exact mathematical form, and says plainly where that form stops. Every fact is checked by a
script. Every quote is exact. Nothing the AI invented is presented as his.

## His twelve through-lines

From the ledger, each running from September 2025 to September 2026:

1. Numbers are shapes.
2. Every one is three; every whole is incomplete.
3. The void, the centre and the immeasurable.
4. Two sides and a third: the coin.
5. Paradox: first a friend, then the thing to classify.
6. Boundaries, lenses and the one who measures.
7. Square and round: two lenses on one object.
8. Primes, gaps and counting.
9. Scrutiny, and the call for humans.
10. Dead ends are data; fold, never delete.
11. Teach it from the ground up, and give it away.
12. The floor beneath physics, and the one-third.

## Four books, and one held back

| | book | reader | through-lines | what exists | what to add |
|---|---|---|---|---|---|
| **I** | ***The Shape of Understanding*** | age ten to undergraduate | 1, 3, 7, 8, 11, 12 | the book: Part Zero, 18 chapters and a Coda, about 16,500 words, 13 figures, 91 checks | a few short boxes drawn from his own lines |
| **II** | ***Two Sides and an Edge*** | high school to undergraduate | 2, 4, 5, 6 | the companion unit: 8 chapters, about 5,800 words, 48 checks | a second part of new coins, each anchored in his words |
| **III** | ***The Integers and Their Towers*** | undergraduate to graduate | 1, 3, 12 | the flagship's `base/`, `towers/` and tower coins: about 12,000 words, with 7 verifiers | book prose, figures and exercises |
| **IV** | ***What Survived*** | anyone doing research with AI | 9, 10 | the essay (about 1,600 words), the graveyard, RETIRED.md and the audit notes | the story in his words, the gates, and the toolkit |
| (V) | *held:* an AI whose reasoning you can see | — | his AI themes (ledger §10–11) | the paused CK program | not now |

### Book I: *The Shape of Understanding*

**It is ready to read, and he is reading it now.** Only small, checked boxes are to be added, each
tied to one of his own lines. Each box gets a line in `curriculum_checks.py`.

| chapter | box | his line |
|---|---|---|
| §1.1 | the epigraph, if he wants it | "4 is the forst 3d" (Sep 2025) |
| Ch.2 | the opening story: four pieces of French toast fit in a round pan and a fifth almost fits; five tetrahedra round an edge leave a 7.35° gap | "You can almost fit a 5th…" (Jan 2026) |
| Ch.4 (*e*) | the capstan law: rope wrapped round a post, where the force you hold falls as e^{−μθ}. An *e*-law you can feel | the sled rope (Jan 2026) |
| Ch.5 (the radian) | the triangle's angles make π, and the hexagon's six triangles make 2π round the centre; with an honest note that "3 pi is a circle" does not follow. Also: counting grid squares inside a circle closes in on π | "pi is triangle, 2 pi is a hexagon" (Sep 2025); "a circle measured by squares" (Jun 2026) |
| Part Zero or Ch.5 | string art: straight lines whose envelope is a parabola | "a line measured by a parabolic envelope" (Jun 2026) |
| Ch.6 (primes) | credit his question: about 7.2% of numbers near a million are prime | "is there around 7% primes?" (Jan 2026) |
| Ch.8 (√2) | 5/7 and 3/4 are neighbours: nothing simpler lies between them | "3/4 is the fraction just above 5/7" (Apr 2026) |
| Ch.10 (Fourier) | a measurement lasting Δt resolves frequency only to about 1/Δt | "the amount of time it takes to take the measurement is one of the generators of the lens" (Feb 2026) |
| Ch.12 (what a prime is) | state the fundamental theorem of arithmetic ("a bag of primes"), plus an extension box: Fermat's two squares, 389 = 10² + 17² | "you end up with a bag of primes" (Jan 2026); "is that a study?" (Sep 2026) |

**The wall stays.** The solid faces of 5, 7 and 9, where odd counts fill the centre, belong to
Book III, not Book I.

### Book II: *Two Sides and an Edge*

**Part One is the existing unit:** Chapters 1–8, the coin and the four kinds of paradox.

**Part Two, "Coins in the world", adds new chapters.** Each chapter opens with his line and ends with
checks:

| chapter | the exact mathematics | his line | status |
|---|---|---|---|
| **The quadratic** | iterate x → ax² + bx + c. The single number D′ = (b−1)² − 4ac decides the fold, the flips, chaos and period three. That is why the logistic map's numbers are 3, 1+√6, 1+2√2 and 4. Includes cobweb figures | "the operator is the quadratic" (Feb 2026) | checked |
| **Truth's coin** | x ↦ 1 − x has no edge on {true, false}; that is the Liar. On [0, 1] its edge is ½. The damped flip x ↦ σ(1−x) settles, flips for ever, or flies apart, depending on its multiplier | "1 is 1 but not is not not, the final paradox" (Sep 2025) | checked |
| **Energy's coin** | T + V is kept and T − V flips. They balance at A/√2, and a quarter-turn (×i) swaps them | "duality is created by the sum or difference ;) of langranian" (Jan 2026) | standard |
| **Light's coin** | caustics: an upright face, a mirrored face, and the bright edge between them. The coffee mug | "the outermost boundary, the projection of the boundary, Nd the focus" (Jan 2026) | standard |
| **The coin on its edge** | the double well: faces ±1, an unstable edge at 0, walls shaped like tanh | "all scars are boundary conditions" (Jan 2026) | checked |
| **Choice's coin** | vote shares in a simplex. A swap is a flip, the tie plane is its edge, and the centroid is the one point every swap keeps | the void as the fullest point (Sep 2025 onward) | standard |
| **Cooperation's coin** | Stag Hunt and Prisoner's Dilemma, with the edge where temptation equals reward | "we teach it game theory early on" (Jan 2026) | checked (the edge at 1/7 in the old simulation's payoffs) |
| **Reading's coin** | an ambiguous expression has two parse trees; the missing convention is the edge | "there is not one correct way, any way works as long as you are consistent" (Jun 2026) | standard |
| **Wholes from parts** | 2 points fix a line and 3 fix a parabola; any 3 of 5 shares rebuild a secret | "1 equals 5 and 2 or 3 of those 5 equal 1 again" (Jan 2026) | standard |
| **Algebra's coin** | reading a table the other way round pairs questions that are really the same question (the J61 closures) | "i never like to pick a side, i like to synthesize" (May 2026) | checked (ck J61) |

**The shape of the book is his:** "two distinct spines... one for each side of the coin... and maybe one
for the edge" (Sep 2026).

### Book III: *The Integers and Their Towers*

**This is the flagship, made into a book.**
- **The base:** the integers 0–9, each with its flat face and its solid face. It includes the theorem
  that odd counts fill the centre, which is his September 2025 line "Odd numbers collapse to the
  center, even numbers collapse around the outer ring of the void", proved in September 2026.
- **The towers:** eight parts, each rising to established mathematics.
- **The coin:** one for each tower.

His framing: "the towering is the answer to find the levels of reality" (May 2026, as quoted). The
mathematics is written and checked. What it needs is book prose, figures and exercises. It comes after
Books I and II.

### Book IV: *What Survived*

**The story, and the method.**

**Part 1: the story in his words, in date order.** Section 10 of the treasure map has the outline, and
the ledger's section D holds all 66 items. It runs:
- from September 2025: "keeping it true is tough", and "i'm going to start making mistakes on purpose
  so you will check me";
- through 4 February 2026: "HELP ME HUMANS! NO MORE AI!";
- to September 2026: "does it beat random", and "focus on the directions and intuitions i have, not
  the AI drift".

**Part 2: the gates.** A claim must be true, specific, not a readout, and it must have provenance.
Each gate is taught through worked cases from his own record:
- the C₅ number used as a simulation's target;
- a "healing time" that was really the sampling interval;
- 4.6% against 0.09%;
- random tables that converge too.

**Part 3: what moved when the lighting changed.** The profile method failed on the tables and then
produced real results on Tao's catalog of equational laws (ck J61), and the Q series' methods were
put to new use.

**Part 4: the toolkit.** These are the AI's machinery, made useful as tools and not as ideas:
- null models;
- metamorphic tests;
- regenerate-and-diff;
- provenance hashes;
- a conflict ledger;
- a claim ledger;
- checks on the stability of AI answers.

**Part 5: keep a graveyard.**

**Personal matters are his call.** The ledger omits them. Faith appears only as he chooses to state it.

### (V) Held back: an AI whose reasoning you can see

His AI vision is recorded in the ledger:
- "an AI based in math reasoning and paradox classification";
- "'white box ai'";
- his rule for answering: speak when confident, hedge in the middle, ask when unsure;
- "it's never prune, it's fold".

The program was paused in June 2026. It is not part of the mathematics series now.

## Order of work

1. **Book I.** He reads it, and his notes are folded in. The boxes above are added one at a time,
   each with its check. It can be shared as soon as he is happy with it.
2. **Book IV.** The essay grows into the story and the method. It is the most timely of the four.
3. **Book II.** The unit grows Part Two, one coin at a time, each coin with its checks.
4. **Book III.** It is written once I and II are stable.

## Rules that carry over

- Every fact is checked by a script, and every quote is exact and sourced.
- Only his intuitions are presented as his. AI-built material appears only as labelled tools.
- Classify, don't resolve: keep both faces and name the edge.
- Book I keeps its wall. Open material, such as 5, 7 and 9 in their solid faces, lives in Book III.
- Never delete. Retired material stays in the graveyard, with the evidence that killed it.
