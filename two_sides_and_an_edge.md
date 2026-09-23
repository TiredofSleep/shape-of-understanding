# TWO SIDES AND AN EDGE
## Flips, fixed points, and the four kinds of paradox
### A companion unit to *The Shape of Understanding*

**Brayden Ross Sanders** · 2026 · CC BY-SA 4.0

> *Every coin has two sides and an edge.*

---

## Before you start

*The Shape of Understanding* climbs. It starts with gumdrops and toothpicks and rises, one checked
step at a time, to the algebra of space. Its last chapter points up the towers of higher
mathematics. This unit uses the same pictures in a different way: instead of climbing, it **turns
things over**.

The whole unit rests on one small idea. A **flip** is a move that, done twice, changes nothing —
like turning a coin over, and then over again. Every flip does two things at once:
- it **swaps** some things with each other, as the coin's two sides are swapped;
- it **leaves** some things exactly where they were, as the coin's edge stays put.

Ask of any flip *what does it leave alone?*, and you find, again and again, the most important
and the strangest place in the picture.

That place is where paradoxes live:
- The oldest shock in mathematics, the diagonal that no fraction can name, is an edge that the
  fractions cannot reach.
- The imaginary numbers are an edge that the real line is missing.
- The liar's sentence — *this sentence is false* — asks for an edge that "true and false" does
  not have.

Mathematics never made these paradoxes go away. It did something better: it named their edges and
sorted them. That is the lesson of this unit: **paradoxes are classified, not resolved.**

Like the book, the unit is a staircase. Its first pages need nothing but a coin. Its last pages
reach undergraduate and early-graduate mathematics. It leans on the book at every step, and every
fact marked *(verified)* is reproduced by the script `two_sides_checks.py`.

---

## Part Zero — The coin

### Picture A — Two sides and an edge

Take a coin out of your pocket. It has two faces, heads and tails. And it has a thin rim all the
way round: its **edge**. Toss it and it lands heads or tails. Once in a very long while it lands on
its edge and stands there, belonging to neither side.

### Picture B — The flip

Turn the coin over. Now turn it over again. It is back exactly as it began. A move like that —
one that, done twice, puts everything back — is called a **flip**. You know lots of them:

- **Turning around.** Face the other way, then face the other way again: you are facing where you
  started.
- **A mirror.** The mirror image of your mirror image is you.
- **A light switch.** Click it, click it again: the light is as it was.

### Picture C — What stays

Every flip does two things. It **swaps** things in pairs: heads with tails, your left hand with
your right. And it **leaves** some things exactly where they are.

- **The mirror.** Hold your hand flat against a mirror. Your fingertips on the glass are exactly
  where their reflection is. The mirror swaps everything in front of it with everything behind it,
  but it leaves the glass itself alone. The glass is the mirror's **edge**.
- **The number line.** Draw a number line and turn it around at 0. Then 3 goes to −3 and −5 goes to
  5, but 0 goes nowhere. **0 is the edge** between the positive numbers and the negative ones.
- **The light switch.** It swaps on and off, and it leaves nothing alone. **A switch has no edge.**
  Remember the switch. It comes back at the end of this unit, as the most famous paradox there is.

### That's the whole vocabulary

Three words:
- a **flip** — done twice, nothing has changed;
- its two **sides** — what it swaps;
- its **edge** — what it leaves alone.

The rest of the unit asks one question, over and over: *what does this flip leave alone?*

---

## Chapter 1 — Flips are everywhere

**1.1 Numbers.** The flip *x* → −*x* swaps each positive number with a negative one. Its edge is the
single number that is its own negative, 0 (verified). The positives and the negatives are the two
sides; zero belongs to neither, and to both.

**1.2 Mirrors, and things that are their own reflection.** A mirror swaps left-handed things with
right-handed ones. Some shapes are their own mirror image: reflect them and you get the same shape
back. All five Platonic solids are like that (verified), so they sit on the mirror's edge. A
lopsided tetrahedron, whose six edges have six different lengths, is not. It cannot be turned to
match its reflection (verified), just as a left glove will never turn into a right one.

**1.3 Shapes turned inside out.** Chapter 3 of the book found the five Platonic solids. Here is a flip
that pairs them up. Put a dot at the centre of each face of a solid and join the dots. You get a new
solid, the **dual**, whose corners sit where the old faces were and whose faces sit where the old
corners were. Do it twice and you are back where you started (as a shape), so duality is a flip.
- It swaps the cube (8 corners, 6 faces) with the octahedron (6 corners, 8 faces) (verified).
- It swaps the dodecahedron (20 corners, 12 faces) with the icosahedron (12 corners, 20 faces)
  (verified).
- The tetrahedron — 4 corners, 4 faces — turns into another tetrahedron. It is its own dual, and it
  sits on the edge (verified).

The same flip works in every dimension. The cube's higher cousins always swap with the octahedron's,
and the tetrahedron's cousin, the simplex, is always its own dual (verified, dimensions 2 to 7).

**1.4 The cube's own flip.** Turn the cube inside out through its centre, so that each corner goes to
the opposite corner. The cube's eight corners split into two groups of four. Each group is a regular
tetrahedron, and the two fit into the cube together like a star — Kepler's *stella octangula*. The
flip swaps one tetrahedron with the other (verified). What does it leave alone? Only the centre
(verified). So the book's *full middle* (Picture 2), the point nearest to everything, is the edge of
the cube's flip.

> **Exercises.** (1) What is the edge of the flip *x* → 10 − *x*? (2) Which capital letters are their
> own mirror images in a vertical mirror? Which in a horizontal one? (3) What is the dual of the dual
> of a cube?
>
> **Misconception this fixes.** *"A flip must move everything."* Most flips leave something where it
> was, and what they leave is usually the most interesting thing in the picture. The flips that move
> everything — the light switch — are rare, and they are where the trouble starts (Chapter 7).

## Chapter 2 — Every thing splits in two

**2.1 The plain idea.** Here is a trick that works for every flip that respects adding (such flips
are called *linear*). Take any thing, and take its flip.
- **Their average lies on the edge.** Flipping the average just swaps the two things being averaged,
  so the average doesn't move.
- **Half their difference is turned into its own negative by the flip.**

Add the two parts back together and you have the thing you started with. So every thing is an
**edge part** plus a **side part** (verified).

**2.2 The real part and the imaginary part.** The complex numbers (§1.3 and Chapter 7 of the book)
have a mirror, *a + bi* → *a − bi*, which flips the picture top to bottom across the real line. Its
edge is the real line itself. The split of 2.1 gives exactly the real part and the imaginary part:
*a + bi* = *a* + *bi* (verified). And a number times its own mirror always lands on the edge:
(*a + bi*)(*a − bi*) = *a*² + *b*², a real number — the square of the number's size (verified).

**2.3 The turn, split.** Chapter 5 read *e^{iθ}* as a turn through the angle θ. Reverse the turn, θ →
−θ, and split *e^{iθ}* into its two parts:
- the edge part is cos θ, a real number;
- the side part is *i* sin θ, an imaginary one.

So *e^{iθ}* = cos θ + *i* sin θ. Euler's formula is nothing but the turn split into what reversing
the turn keeps and what it flips (verified). Growth splits the same way: *e^x* = cosh *x* + sinh *x*
(verified).

**2.4 At the top of the staircase: tables of numbers.** Flip a square table of numbers across its
diagonal; this flip is called the *transpose*. The edge part is a **symmetric** table, and the side
part is a **skew** one.
- The symmetric part has only real eigenvalues (Chapter 9). Used as a rate of growth, it stretches.
- The skew part has only imaginary eigenvalues. Used as a rate of growth, it turns (verified).

Stretching and turning are the edge and the side of one flip.

**2.5 The odd rule.** One more fact follows in a single line. Suppose a flip turns some quantity into
its own negative. On the flip's edge, where nothing moves, that quantity must equal its own
negative — so there it is **zero**. That one line is why:
- 0 sits between the positives and the negatives;
- imaginary parts vanish on the real line;
- a *p* orbital of an atom is exactly zero on its *node*. The orbital has a positive lobe and a
  negative lobe, a mirror through the atom swaps them, and the node is the mirror's plane (verified).

> **Exercises.** (1) Split *x*³ + *x*² into its edge part and its side part for the flip *x* → −*x*.
> (2) Use the odd rule to show that sin 0 = 0, without a calculator. (3) Why is (3 + 4*i*)(3 − 4*i*)
> a whole number? Which one?

## Chapter 3 — Three coins on one ball

Three famous pairs — positive and negative, finite and infinite, real and imaginary — turn out to be
three flips of a single object.

**3.1 Finite and infinite.** Draw the circle of radius 1 around 0 in the plane of complex numbers. Now
flip the plane *through* the circle. Every point inside goes to a point outside, on the same ray from
0, so that the two distances multiply to 1 (*z* → 1/*z̄*). Points near 0 go far away, and points far
away come near 0. Do it twice and everything is back, so it is a flip. It swaps the inside with the
outside, and 0 with the infinitely far, and it leaves the whole circle in place (verified). **The
round is the edge between the finite and the infinite.**

A word about words. The book's Coda says that the perfect round *has* no edge — no corner or seam to
measure from — and that is still true: the circle has no ends. Here the circle *is* the edge of a
flip, the place the flip keeps. These are two meanings of one word; keep them apart.

**3.2 Real and imaginary.** The mirror of 2.2 keeps the real line and flips the imaginary part. A
different flip, *z* → *i*/*z*, swaps the real line with the imaginary line outright: it sends 1 to
*i*, and *i* to 1. Its edge lies halfway between them, at the two numbers whose square is *i*
(verified).

**3.3 The ball of numbers.** Now wrap the whole plane of complex numbers around a ball, like a map of
the world drawn on a globe. Put 0 at the south pole, and add one extra point, ∞, at the north pole.
This ball is called the *Riemann sphere*. Six special numbers — 0, ∞, 1, −1, *i* and −*i* — land
exactly on the six corners of a regular octahedron (verified), the six-cornered solid of the book's
Chapter 3. And three flips of the numbers become three half-turns of the ball, one about each of the
octahedron's three axes (verified):

| the flip | it keeps (its edge) | the coin |
|---|---|---|
| *z* → −*z* | 0 and ∞ | positive and negative |
| *z* → 1/*z* | 1 and −1 | finite and infinite: it swaps 0 with ∞ |
| *z* → −1/*z* | *i* and −*i* | both at once |

Look at the last row. On the real number line, the flip *x* → −1/*x* swaps the positive numbers with
the negative ones, and it keeps no number at all. To be kept, a number would need *x* = −1/*x*, that
is, *x*² = −1, and no real number does that (verified). The flip's edge is off the line: it is *i*.
The imaginary numbers are exactly **the edge that the real line is missing**.

**3.4 The point every coin shares.** Any two of the three half-turns, done one after the other, make
the third (verified). Is there a point that all three leave alone? No number is: each number on the
ball is kept by at most one of them. The one point that all three half-turns keep is the **centre of
the ball** — which is not on the ball, and so is not a number at all (verified). This is the book's
full middle again: the point nearest to everything, which no number occupies.

> **Exercises.** (1) Where does the flip *z* → 1/*z̄* send the number 2? The number *i*/2? (2) Which
> number does *z* → 1/*z* send to ∞? (3) Check that ((1 + *i*)/√2)² = *i*.

## Chapter 4 — The whole coin

**4.1 Heads, tails and edge.** A tossed coin can land three ways. Write them −1 (tails), +1 (heads) and
0 (on its edge). Toss three such coins and there are 3 × 3 × 3 = 27 outcomes. Sort them by how many
coins landed on their edge (verified):
- 8 with none;
- 12 with one;
- 6 with two;
- 1 with all three.

Now look at a Rubik's cube: 8 corner pieces, 12 edge pieces, 6 centre pieces, and 1 hidden core.
They are the same 27, because the outcomes *are* the positions of the pieces (verified). It is
Pascal's triangle again (the book's §2.3), with the edge added. There, (1 + 1)³ = 1 + 3 + 3 + 1
counted in-or-out choices. Here, (2 + 1)³ = 8 + 12 + 6 + 1 counts heads, tails or edge.

**4.2 Two coins, and every size.** Two such coins give 9 outcomes, which form the 3 × 3 grid: 4
corners, 4 edge-middles and the centre (verified). In any number of dimensions (verified):
- all the coins on a side gives the corners of a cube;
- exactly one coin on a side gives the corners of the octahedron's higher cousin;
- all the coins on their edges gives the centre.

**4.3 The magic square's coin.** Chapter 13 built magic squares by a walking rule. Turn a finished
square halfway round. Every number *s* lands on the cell that held *n*² + 1 − *s*: in the Lo Shu, 1
and 9 swap, 2 and 8, 3 and 7, 4 and 6. The middle cell, which holds 5, stays (verified, for the
walked squares of sizes 3, 5, 7 and 9). The half-turn is a flip; the middle cell is its edge; and 5
is the number that is its own partner. Squares with this property are called *associative*. It is an
old observation, which the author found again.

**4.4 The flat shape, walked.** Put *n* dots evenly round a circle, and walk: start at a dot and keep
jumping *k* dots ahead. You come home having visited every dot, in one loop, exactly when *k* shares
no factor with *n* (verified). That is Chapter 12's question, "does it share a factor with *N*?",
drawn as a picture.
- If *n* is prime, every jump makes a single loop. With 5 dots, *k* = 1 draws the pentagon and
  *k* = 2 draws the five-pointed star (verified).
- Every loop goes round the middle without ever touching it (verified): it points toward its centre,
  and never stands on it.
- With 6 dots and *k* = 2, the walk splits into two triangles. That is exactly the cube's corner-on
  shadow from Picture 5, whose two triangles are the cube's two tetrahedra (verified).

> **Exercises.** (1) With 8 dots, which jumps make a single loop? (2) With 12 dots, how many jumps
> between 1 and 11 make a single loop? Compare with the count of numbers below 12 that share no
> factor with 12. (3) In the 5 × 5 magic square of Chapter 13, which number sits in the middle?

## Chapter 5 — One box, two lenses

**5.1 Two shadows, one coin.** Picture 5 of the book: a cube casts a square face-on, and a hexagon
corner-on. Now look for the cube's two tetrahedra (1.4) in the shadows.
- **Face-on**, both tetrahedra cast the very same square. You cannot tell the two sides apart.
- **Corner-on**, they come apart: two triangles turned against each other in a six-pointed star, with
  each tetrahedron's far corner landing on the centre (verified).

One lens hides the coin. The other shows its two sides, and the edge they share.

**5.2 Neither lens is enough; both are.** Neither shadow tells all eight corners apart. Face-on, the
eight corners cast only four points; corner-on, they cast only seven. But the two shadows together
tell all eight apart (verified).

The rule behind this fits in one line, and the author worked it out with Ben Mayes: *a family of
views tells every pair of things apart exactly when no pair is mixed up by all of the views at once*
(verified, on thousands of random families of views). Face-on mixes up four pairs of corners and
corner-on mixes up one pair, but no pair is mixed up by both.

**5.3 The angle between the lenses.** The direction you look along face-on and the direction you look
along corner-on meet at an angle whose cosine squared is 1/3. That is the tetrahedron's number from
Chapter 1, the "magic angle" where 3*x*² − 1 = 0 (verified).

## Chapter 6 — Missing edges: where the paradoxes live

**6.1 The diagonal again.** Chapter 8 told the oldest shock in mathematics: no fraction is √2. Here it
is as a coin. The flip *x* → 2/*x* sends every fraction to a fraction, and done twice it changes
nothing. It swaps the fractions whose square is below 2 with the fractions whose square is above 2.
And it has **no edge among the fractions**. An edge would be a fraction *x* with *x* = 2/*x*, that
is, *x*² = 2, and there is none (verified). The edge exists; the fractions just cannot reach it. Its
name is √2.

**6.2 Pointing toward it, measuring off it.** The book's Coda put its keystone in one sentence: *you
can only point toward it, and measure off of it.* For √2, each part of that sentence is a theorem
(verified):
- **Point toward it.** Average the two sides: from any fraction *x*, take the average of *x* and
  2/*x*. Starting from 1, this gives 3/2, then 17/12, then 577/408, then 665857/470832, each pair
  of sides closer than the last. This is Heron's method. The Babylonians knew √2 correct to about
  six decimal places, on a clay tablet some 3,700 years old.
- **Measure off it.** Every fraction *p*/*q* stays more than 1/(3*q*²) away from √2. The reason takes
  one line: *p*² − 2*q*² is a whole number that is never 0, so it is at least 1 in size.
- **Never stand on it.** No fraction is √2.

The same flip with 3, 5, 6 or 7 in place of 2 also has a missing edge. With 4 or 9, the perfect
squares, it does not (verified).

**6.3 The imaginary edge.** We met the second missing edge in Chapter 3. On the real line, *x* →
−1/*x* has no edge, and its edge — named, not resolved — is *i* (verified).

**6.4 Naming, not resolving.** Mathematics never made these paradoxes go away. It **named their
edges** and made room for them:
- the real numbers — a real number is exactly the edge between two sides of the fractions
  (Dedekind, 1872);
- the complex numbers, in which *i* is Argand's quarter-turn;
- the ball of numbers, with its point ∞.

Each time the flip stayed, both sides stayed, and the missing edge was given a name. That is what
*classifying* a paradox means.

**6.5 A coin with no edge at all.** The quaternions of Chapter 7 turn space: every unit quaternion
*q* is a turn. But *q* and −*q* give the very same turn, and no unit quaternion is its own negative.
So the flip *q* → −*q* has no edge at all (verified). Turn something once all the way round, through
360°, and its quaternion becomes −*q*; only after two full turns is it *q* again (verified). You can
feel this with a plate held flat on your palm: one full turn twists your arm, and a second full turn
untwists it.

> **Exercises.** (1) Start from *x* = 2 and replace *x* by the average of *x* and 3/*x*, three times.
> Which number are you pointing toward? (2) Is there a fraction *x* with *x* = 9/*x*? With *x* =
> 8/*x*? (3) Which of the three flips of 3.3 swaps 1 with −1 and keeps no real number?
>
> **Misconception this fixes.** *"√2 and i were invented to make awkward equations work."* They were
> named because a flip that mathematics already had — halving against doubling, turning a number
> inside out — was missing its edge. Nothing was made up. A place the flip pointed to was given a
> name.

## Chapter 7 — Four kinds of paradox

In April 2026 the author and Ben Mayes sorted paradoxes not by their subject but by *how they fail*,
and they found four kinds. Read through the coin, each kind is a different relation between a flip
and its edge. The sorting is a way of seeing, not a theorem — their memo says so plainly. But every
example below is real mathematics, checked wherever a finite case can be checked.

**7.1 Type I — not enough lenses: Zeno.** A runner crosses half the track, then half of what's left,
then half of that, forever. *Infinitely many steps — so she never arrives?* Two lenses are looking
at one run:
- the **counting lens** sees infinitely many steps;
- the **measuring lens** sees their lengths, 1/2 + 1/4 + 1/8 + …, which stay below 1 and close in
  on it (verified).

The paradox came from using only one lens. With both, she arrives. This is the book's Picture 6,
*counting and measuring*, meeting a paradox. The fix is to add a lens, and the rule of 5.2 says when
you have enough.

**7.2 Type II — the edge lies outside the family: Banach–Tarski, and Gödel.** Take all the "words" you
can build from two turns, *a* and *b*, and their undoings, *a*⁻¹ and *b*⁻¹ — keeping only the words
that never undo themselves in place. Sort them by their first letter: that gives four piles, plus
the empty word. Then something astonishing happens (verified):
- two of the four piles — one of them turned by *a* — rebuild **all** the words;
- the other two piles — one turned by *b* — rebuild them all again.

Four piles, two whole copies. Now measure "how much" by counting. The pile starting with *a*⁻¹ holds
a quarter of the words of each length, but turned by *a* it holds three quarters (verified). So no
way of measuring "how much" can stay the same under the turns.

Do the same with real rotations of a solid ball, and the ball can be cut into a handful of pieces
and reassembled into two balls, each as big as the first (Banach and Tarski, 1924). The pieces are
too scattered for any volume to be assigned to them. The thing that would forbid the trick — volume
— lies *outside* the family of moves that did the rebuilding.

Gödel's theorem has the same shape. Inside a consistent system strong enough for arithmetic, *proof*
cannot settle a certain sentence; what would settle it lies outside the system. These are **missing
edges**, like √2 for the fractions.

**7.3 Type III — a flip with no edge, and a sentence that demands one: the Liar.** *This sentence is
false.* If it is true, it is false; if it is false, it is true. Read it as a coin: the flip is "not",
which swaps true with false. The Liar asks for a truth value that is its own "not" — a value on the
edge. But with only true and false, "not" is the light switch of Part Zero: **it has no edge**
(verified). There is nowhere for the Liar to land.

The same engine drives the whole type:
- **Cantor.** Make any list of infinite yes/no rows. Go down the diagonal and flip every answer. The
  new row differs from every row in the list, so no list can hold all the rows (verified, for every
  small list). The flip yes ↔ no has no edge.
- **Russell.** "The collection of all things that are not members of themselves" can never be one of
  the things (verified, for every small case).

One theorem covers them all (Lawvere, 1969): whenever a flip has no edge, no list can contain every
row — its own flipped diagonal is always missing.

And here is the most beautiful part: **give "not" an edge.** Add a third truth value, *neither*, which
"not" leaves alone. Now the Liar has exactly one value it can take: *neither* — the edge (verified).
This is what Saul Kripke did in 1975. He did not declare the Liar true, or false; he classified it
as *ungrounded*, landing on the edge. Classification, not resolution. (And once the flip has an edge,
the diagonal argument stops working: some list does contain its own flipped diagonal — verified.)

**7.4 Type IV — the coin changes as you look: the Unexpected Hanging.** A judge tells a prisoner that
he will be hanged on one day next week, and that the day will be a surprise. The prisoner reasons:
- not Friday, because by Thursday night it would be no surprise;
- so not Thursday either;
- and so on, back to Monday — so it cannot happen at all.

On Wednesday the hangman knocks, and the prisoner is surprised. Here the set of possibilities
changes *as the prisoner reasons about it*: each step of the argument changes what the next step can
see. No fixed coin fits this kind. It is still open — left open honestly by its authors, and here.

**7.5 The four kinds at a glance.**

| kind | what fails | examples | the coin |
|---|---|---|---|
| I | not enough lenses | Zeno | add the second lens |
| II | what would settle it lies outside the family | Banach–Tarski; Gödel | a missing edge |
| III | the object cannot exist | the Liar; Russell; Cantor | a flip with no edge, and a demand for one |
| IV | the possibilities change as you look | the Unexpected Hanging | open |

> **Exercises.** (1) "This sentence has five words." True or false — and is it a paradox? (2) Grelling's
> paradox: call an adjective *heterological* if it does not describe itself (*long* is heterological,
> *short* is not). Is *heterological* heterological? Which kind is it? (3) Why does adding more
> counting never fix Zeno, while adding one measuring does?

## Chapter 8 — Where you meet coins

Every tower of the book's Chapter 18 carries a coin. One line each:

- **Shapes.** Duality swaps the cube and the octahedron in every dimension; the simplex is its own
  dual (1.3).
- **Numbers.** The mirror *a + bi* → *a − bi* keeps the real numbers on every floor of the number
  tower — complex numbers, quaternions, octonions — and a number times its mirror always lands there
  (verified).
- **The cube's algebra.** The flip that turns every direction around (*v* → −*v*) splits the cube's
  algebra, Cl(3), into an even half and an odd half, and the two halves sit on the cube's two
  tetrahedra (verified). The even half, which the flip keeps, is the quaternions: where turning
  lives (verified).
- **Crystals.** Every crystal lattice has a dual lattice. The densest way to stack balls (the
  face-centred cubic crystal) and the crystal of iron (body-centred cubic) are each other's duals.
  The plain cubic grid and the remarkable E₈ lattice are their own duals, on the edge (verified).
- **Atoms.** An orbital's positive and negative lobes are two sides, and its node is the edge (2.5).
- **Growth.** The flip that trades growing for shrinking keeps pure turning — the circle — as its
  edge. And a half-turn of pure turning is the flip of positive and negative itself: *e^{iπ}* = −1
  (verified).
- **Light at a wall** (an illustration from physics). In crystals engineered to guide light, a wave's
  "mass" can flip sign across a wall. Exactly one state is then held at the wall, where the mass is
  zero: the odd rule, made of light (verified on a model chain; Jackiw and Rebbi, 1976; Su,
  Schrieffer and Heeger, 1979).

## Closing — Classification, not resolution

The book taught you to see a few shapes clearly, and to climb from them. This unit taught one
question to ask of each of them: *what does the flip leave alone?* There are three kinds of answer:
- Sometimes it is a place everyone knows: 0, the centre, the real line.
- Sometimes it is a place the sides can point toward but never reach: √2, *i*.
- Sometimes there is no answer at all: the switch, *q* and −*q*. When something demands an answer
  anyway, you get a paradox, like the Liar.

That is why the unit ends where it does. A paradox is not a mistake to be hidden, or a knot to be
cut. It is an edge, and the honest thing to do with an edge is to find it, name it, and keep both
sides. Mathematics has been doing that for two and a half thousand years. It is the shape of
understanding, turned over.

**What this unit is, and is not.** It is a way of seeing, built from standard mathematics and
checked. It is not a new theorem: flips and fixed points are among the oldest ideas in mathematics,
and every example here is known. What is new is the arrangement — one question, asked everywhere —
and that is a claim about teaching, to be tested by teaching.

---

## Answers to the exercises

- **Chapter 1.**
  1. 5.
  2. In a vertical mirror: A H I M O T U V W X Y. In a horizontal mirror: B C D E H I K O X.
  3. The cube.
- **Chapter 2.**
  1. Edge part *x*², side part *x*³.
  2. sin(−θ) = −sin θ, so sine is turned into its own negative, and 0 is the edge of θ → −θ.
  3. 3² + 4² = 25.
- **Chapter 3.**
  1. 1/2, and 2*i*.
  2. 0.
  3. (1 + *i*)² = 2*i*, and 2*i*/2 = *i*.
- **Chapter 4.**
  1. 1, 3, 5, 7.
  2. Four: 1, 5, 7, 11 — the same as the count of numbers below 12 sharing no factor with 12.
  3. 13.
- **Chapter 6.**
  1. √3 (2 → 7/4 → 97/56 → 18817/10864).
  2. Yes, *x* = 3; no.
  3. *x* → −1/*x*.
- **Chapter 7.**
  1. True, and no paradox: a sentence may talk about itself if what it says lands on a side.
  2. Neither answer is consistent; it is Type III, the Liar's engine.
  3. Counting only ever sees more steps. The question is the total length, which only a measuring
     lens sees.

## References

- J.-R. Argand, *Essai sur une manière de représenter les quantités imaginaires dans les
  constructions géométriques* (Paris, 1806).
- S. Banach and A. Tarski, "Sur la décomposition des ensembles de points en parties respectivement
  congruentes," *Fund. Math.* 6, 244 (1924).
- G. Cantor, "Über eine elementare Frage der Mannigfaltigkeitslehre," *Jahresber. DMV* 1, 75 (1891).
- H. S. M. Coxeter, *Regular Polytopes*, 3rd ed. (Dover, 1973).
- R. Dedekind, *Stetigkeit und irrationale Zahlen* (1872).
- D. H. Fowler and E. R. Robson, "Square root approximations in Old Babylonian mathematics: YBC 7289
  in context," *Historia Math.* 25, 366 (1998).
- K. Gödel, "Über formal unentscheidbare Sätze der *Principia Mathematica* und verwandter Systeme I,"
  *Monatsh. Math. Phys.* 38, 173 (1931).
- F. Hausdorff, *Grundzüge der Mengenlehre* (Veit, 1914).
- R. Jackiw and C. Rebbi, "Solitons with fermion number ½," *Phys. Rev. D* 13, 3398 (1976).
- J. Kepler, *Harmonices Mundi* (1619).
- S. C. Kleene, *Introduction to Metamathematics* (North-Holland, 1952).
- F. Klein, *Vorlesungen über das Ikosaeder* (Teubner, 1884).
- S. Kripke, "Outline of a theory of truth," *J. Philos.* 72, 690 (1975).
- F. W. Lawvere, "Diagonal arguments and cartesian closed categories," *Lecture Notes in Math.* 92,
  134 (1969).
- D. J. O'Connor, "Pragmatic paradoxes," *Mind* 57, 358 (1948).
- B. Russell, *The Principles of Mathematics* (Cambridge, 1903).
- B. R. Sanders and B. Mayes, "Paradox classification memo" (8 April 2026), unpublished; archived at
  github.com/TiredofSleep/ck.
- W. P. Su, J. R. Schrieffer and A. J. Heeger, "Solitons in polyacetylene," *Phys. Rev. Lett.* 42,
  1698 (1979).
- A. Tarski, "Der Wahrheitsbegriff in den formalisierten Sprachen," *Studia Philos.* 1, 261 (1936;
  Polish original 1933).
- N. S. Yanofsky, "A universal approach to self-referential paradoxes, incompleteness and fixed
  points," *Bull. Symbolic Logic* 9, 362 (2003).
