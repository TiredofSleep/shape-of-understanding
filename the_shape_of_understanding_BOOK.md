# THE SHAPE OF UNDERSTANDING
## A Why-First Visual Grammar for the Deep Structure of Mathematics
### Brayden Sanders

### — Book Frame / Full-Length Manuscript Outline with Worked Core —

---

> *Increasingly round — and never measurably round.*
>
> — the working epigraph of this book (after Perelman's description of Ricci flow,
> extended: the flow approaches a perfect roundness it never occupies)

---

> **What this book is.** Mathematics is taught as a stack of separate languages —
> arithmetic, algebra, trigonometry, calculus, linear algebra, abstract algebra —
> each with its own notation, each in its own course, joined by nothing a student can
> see. This book proposes that a *single small visual vocabulary* can carry a large
> fraction of the deep, hard-to-teach ideas of mathematics, and that this vocabulary
> can be kept *honest*: every picture is checked against the real proof, and the
> pictures that would mislead are discarded and recorded. The result is meant to be a
> shared mental model — a coordinate system for intuition — that a learner can hold
> across fields, so that the deep facts of different courses become visibly the same
> kind of fact. It is a work of *pedagogy*, and its claims are testable as pedagogy:
> whether learners build a connected model faster, retain it longer, and make fewer of
> the classic errors. It does not claim to be a new theory of physics or a decoding of
> reality; where it reaches toward those, it says so and marks the reach.

---

# FRONT MATTER

## Preface — A student for the sake of being a teacher

The motivation of this book is a single observation from years of learning and
explaining mathematics: **the hardest thing for a student is not any one concept, but
the absence of a picture that connects them.** A learner can be taught eigenvalues on
Monday and the Fourier transform on Wednesday and never be shown that they are the same
idea — rotation — wearing two costumes. The formalisms are precise and the connections
are invisible, and so mathematics is experienced as a pile of unrelated techniques
rather than one connected structure.

This book is an attempt to supply the missing picture — with a discipline attached, so
that the picture does not, as intuitive pictures so often do, quietly lie. The rubber
sheet that "explains" gravity and the tiny solar system that "explains" the atom are
memorable and *wrong* in ways that damage a student's later understanding [Feynman 1964
warns repeatedly against exactly this]. The pictures here have been stress-tested for
truth; the ones that survive are load-bearing, meaning that if you follow them you
arrive at the real theorem, not a comfortable error.

## Introduction — Why a shared, true, visual model is rare and precious

The history of mathematics is, in part, a history of *unifying pictures* that were rare
when they arrived and transformative afterward. Descartes' coordinate plane made algebra
and geometry one subject [Descartes 1637]. The Argand diagram made complex numbers
*visible* as points and rotations, dissolving centuries of unease about "imaginary"
quantities [Argand 1806; Wessel 1799]. Feynman's diagrams made intractable sums in
quantum electrodynamics into pictures a physicist could reason with [Feynman 1949].
Each was a *representation*, not a new fact — and each mattered enormously, because a
representation a mind can hold is the scarce resource in a field where the truths are
already written down.

The claim of this book is modest in kind and large in scope: that the *structural core*
of undergraduate and early-graduate mathematics — the part about shapes, symmetry,
rotation, growth, and the divide between the discrete and the continuous — admits such a
unifying picture, built from a handful of primitives, and that the picture can be kept
honest by checking. The book is organized around that picture and around the discipline
that keeps it true.

---

## Reader's map

- **Part One (Ch. 1–2) — the grammar.** Six primitives, and the one proof the book rests
  on (the tetrahedral 1/3 from equidistance). Read this first; everything reuses it.
- **Part Two (Ch. 3–7) — the elegant lessons.** Five deep "why"s the grammar connects:
  Platonic solids, *e*, radians, prime rarity, why quantum mechanics is complex.
- **Part Three (Ch. 8–11) — the hard lessons.** The four that break students: √2's
  irrationality, eigenvalues, the Fourier transform, groups. The real test of the pedagogy.
- **Part Four (Ch. 12–14) — the combinatorial frontier.** Three further lessons drawn from
  research combinatorics that pass the same bar; the physics frontier is deliberately
  excluded, and why.
- **Part Five (Ch. 15–17) — the model whole.** Why it is one picture not fourteen, the
  honest failures, and how to test it as teaching.
- **Coda.** *Increasingly round, never measurably round.*
- **Appendix A.** The verification scripts. Every mathematical claim in the book is
  reproduced by running them.

---

# PART ONE — THE GRAMMAR

## Chapter 1 — Six primitives

The entire vocabulary is six ideas. Everything in the book is built from these, and the
reader should hold them from the start.

**1.1 Integers are shapes — and the ladder is the ladder of simultaneous equality.**
Given *n* points in the most symmetric arrangement — all **mutually equidistant** — they
form the **regular (n−1)-simplex** [Coxeter 1973, §7]: one point is a point, two a
segment, three a triangle, four a tetrahedron. The crucial subtlety, which the rest of
the book rests on, is *why* each added point raises the dimension.

It is not that "n points need n−1 dimensions" — four points can sit perfectly well in a
plane, as the corners of a square. It is that four points **cannot all be equidistant**
in a plane. Three points can: the equilateral triangle, every pair the same distance,
flat. But the moment one demands a *fourth* point equidistant from the other three, the
plane has no room, and the fourth point is *forced up* into the third dimension — the
tetrahedron (verified in the accompanying script: the square's diagonals are longer than
its sides, √2 versus 1, while the tetrahedron's six distances are all equal). A square is
four points that have *given up* being equal in order to stay flat; a tetrahedron is four
points that *keep* being equal by lifting.

So **three is the last count that can be made perfectly symmetric while remaining flat**,
because the plane holds exactly three mutually-equidistant points and no more. Each new
dimension is precisely the room needed for *one more point to be equal to all the
others*: the line holds two, the plane three, three-space four, and so on. **The
dimensional ladder is the ladder of simultaneous equality** — of how many things can be
perfectly equal to one another at once, which is exactly one more per dimension. This is
the real driver behind "count the vertices"; the count is the surface, and the demand for
equality is the mechanism. The integers 1–4 are that ladder, and the lift from three to
four — flat to solid — is the first time the demand for one more equal thing costs a
dimension.

**1.2 The break, and the round.** At five points the picture changes character. The
regular pentagon has five-fold symmetry, and five-fold symmetry **cannot tile the
plane** — a theorem (the crystallographic restriction: the only rotation orders a
lattice may possess are 1, 2, 3, 4, and 6, because 2cos(2π/n) must be an integer, which
holds only for those n [Barlow 1894; verified in the accompanying script]). Five is the
first shape that will not pack. Yet the pentagon *can* fold into three dimensions — as
the dodecahedron — and six points, spread as far apart as possible on a sphere, become
the **octahedron**, the sphere's six poles. The flat wheel (five) becomes the round
(six): a *lift* from two dimensions into three, which the book will meet again and
again.

**1.3 Rotation is an imaginary axis.** A rotation has a still centre and a turning
edge. Since Argand and Wessel we have known that the turning is captured by the
imaginary unit *i*: multiplication by *e^{iθ}* rotates the plane by θ [Argand 1806].
The still centre is real; the turn is imaginary. This single identification —
**rotation = i** — will unify quantum mechanics, eigenvalues, and the Fourier transform
in later chapters.

**1.4 Growth is a breath.** A quantity that grows in proportion to its current size
breathes: it swells, and the rate of swelling is itself. The unique function equal to
its own derivative is *e^x*, and *e* = lim(1 + 1/n)^n ≈ 2.71828 is the *rate of
self-proportional growth* [Euler 1748]. Wherever a thing grows or decays in proportion
to itself — populations, money, radioactive matter, heat — *e* is the breath-rate.

**1.5 The cube casts two shadows.** The tetrahedron (four) doubled is the **cube**:
the cube's eight vertices split into two interpenetrating tetrahedra (Kepler's *stella
octangula* [Kepler 1619]). Seen along a face, the cube's shadow is a **square** — four
fold symmetry, ninety degrees. Seen along its body diagonal, its three mutually
perpendicular edges project to **three directions one hundred twenty degrees apart — a
regular hexagon** (verified in the script). The angle relating the two shadows is
fixed: the direction cosine of the diagonal (1,1,1) with any axis is 1/√3, so its cosine
*squared* is **1/3**. This 1/3 is a specific, forced number — it is 1/(N−1) evaluated at
N = 4, the tetrahedron's signature, and it appears for no other simplex (it is 1/2 at
N=3, 1/4 at N=5).

**1.6 Count versus measure.** Whole things are *counted*; continuous things are
*measured*. The oldest crisis in mathematics — the Pythagorean discovery that the
diagonal of a unit square cannot be measured by any whole-number ratio of its side
[Fritz 1945; Heath 1921] — is the discovery that count and measure cannot always be
reconciled. Where they cannot is where the deepest difficulties of mathematics live,
and the book returns to this seam repeatedly.

**1.6b The void is the fullest point.** The reference the equidistant points measure from
(§1.1) is their **centroid** — and the centroid is not an afterthought but the most
remarkable point in the arrangement. It is, by definition, the point that **minimizes the
total distance to all the points at once** — the location *nearest to everything
simultaneously* (verified: for the tetrahedron the centroid's total distance to the
vertices is 6.93, less than any vertex's 8.49, and the numerical minimizer lands exactly
on it). Every vertex is far from most of the others; only the centre is *equally near to
all of them*.

This inverts the ordinary reading of zero. The void — the empty centre, the 0 — is not
the *absence* of the points. It is the point **maximally near to all of them** — the one
location that touches every direction equally by committing to none. A vertex is *a*
thing, somewhere; the centre is *near all* things, nowhere in particular, and "near all"
is a fuller position than "being one." The symbol for nothing marks the closest thing
there is to being everything.

This gives the void a role, and a story. It begins as **projection** — the origin from
which the first points emanate (the point, 1, is the void made visible; it *is* the void,
brought into view). As points accumulate and come to *surround* something, the void
**becomes central** — the still centroid the equidistant points all measure from, the
reference that keeps them equal. It is what equality is measured *against*: remove it and
there is nothing for the points to be equal *around*. It starts by throwing the shapes
outward and ends by holding them in balance — potential becoming actual, source becoming
centre, the projector becoming the still point. Zero is where one is when one is equally
close to all of it.

**1.7 On honesty.** Because an intuitive picture is dangerous precisely when it is
memorable and false, this book attaches a discipline to its vocabulary: every picture is
checked against the real proof (the accompanying scripts reproduce each check), reaches
beyond what is proven are marked as reaches, and pictures found to mislead are recorded
in a list of honest failures (Chapter 14). This is the feature that distinguishes a
curriculum from a collection of clever analogies.

## Chapter 2 — The forced core: why the tetrahedron gives 1/3

*(This chapter is the one place the book proves its central geometric fact from the
ground up, so the reader sees that the pictures rest on real mathematics.)*

Place the *N* vertices of a regular simplex as unit vectors from its centre. By
symmetry every pair has the same dot product cos θ, and because the vectors sum to zero,
0 = |Σvᵢ|² = N + N(N−1)cos θ, giving **cos θ = −1/(N−1)** [a standard result; e.g.
Coxeter 1973]. For the tetrahedron, N = 4, so cos θ = **−1/3** and θ = 109.47° — the
tetrahedral angle familiar from chemistry as the H–C–H bond angle of methane [Pauling
1960]. Its half-angle, 54.74°, has cos² = 1/3, and is the angle between a cube edge and
the body diagonal.

Read through §1.1, this angle acquires a meaning deeper than the arithmetic. The 1/3 is
**the price of the fourth equidistance** — the exact angle at which the fourth point
sits once it has been forced out of the plane to remain equal to the other three. It is
not merely that "4 − 1 = 3"; it is that arccos(−1/3) is the *specific geometry of keeping
one more point equal than the plane allows*. The number that threads the whole book is
therefore the tetrahedron's number in the fullest sense: the angular cost, paid in the
third dimension, of the first equality the plane could not grant. (Chapter 14 records the
failure of the tempting over-generalization "any N − 1 gives 1/3": the cosine is −1/2 at
N = 3 and −1/4 at N = 5; the value 1/3 is the tetrahedron's alone.)

**The foundation, in one breath.** Three ideas now stand together and generate the rest of
the book. First, the void (0) is the point nearest to all points at once — the fullest
position, not the empty one — and it is what the points measure their equality *against*
(§1.6b). Second, the dimensional ladder is the ladder of *simultaneous equality*: each
dimension is the room for one more point to be equal to all the others, and three is the
last that stays flat (§1.1). Third, the moment a fourth point insists on that equality it
is forced into the third dimension, and the angle it lifts to is arccos(−1/3) — the 1/3
that threads the book (§Ch. 2). So the whole opening is a single motion: **the fullest
point throws out shapes that hold each other equal, and the demand for one more equal
thing than flatness allows is what lifts the plane into space.** Everything after is this
motion, seen from more angles.

---

# PART TWO — THE ELEGANT LESSONS
### *The connective "why"s: deep facts that the grammar reveals to be related*

## Chapter 3 — Why there are exactly five Platonic solids

A solid closes only if each vertex leaves **angular room to fold** into three
dimensions. Counting the vertex-figures with positive room — regular {p,q} with
1/p + 1/q > 1/2 — yields exactly five: {3,3}, {3,4}, {3,5}, {4,3}, {5,3} (verified). That
count *is* the classical theorem [Euclid, *Elements* XIII; Coxeter 1973]. And it closes
the arc of §1.2: the pentagon, barred from tiling the plane, folds into space as the
dodecahedron — the break becomes the round. Platonic solids are taught here not as a
list but as *which shapes have the room to become solid.*

## Chapter 4 — Why *e* appears everywhere

*e* is the rate of self-proportional growth — the breath whose out-rate equals its
size (§1.4). Compound interest, population, radioactive decay, cooling, and diffusion
all obey dy/dt ∝ y, and the solution is always *e* to a rate times time [Euler 1748;
standard]. The student stops asking "why *this* number" and sees: *it is the only breath
that sustains itself.* Chapter 4 also introduces, gently, the connection to the shell
growth of §1 as a true analogy of mechanism (flagged, per §1.7, not as a claim that all
growth is literally geometric shell growth).

## Chapter 5 — What a radian really is

Rotation is the imaginary axis (§1.3). A **radian** is rotation measured in unit-point
arc lengths: when the radius equals the seed length 1, the arc *equals* the angle, and
2π is one full turn. Radians cease to be an arbitrary convention and become *rotation
counted in seeds.*

## Chapter 6 — Why the primes thin out

Two roles must be kept distinct here. The numbers that **reach every position** — stepping
by 1, 5, 7, or **11** visits all twelve clock positions, while 2, 3, 4, 6 fall into short
cycles — are the ones **coprime to 12**: the *units* of ℤ/12, its generators. (The picture
must not blur this: 1 is a unit but not prime, and 2 and 3 *are* prime but not generators.)
**Primes** play the complementary role — a prime is a number that lets you *close* others
early (the sieve, Chapter 12). As numbers grow, *more small factors
become available to close them early* — to make them composite — so the survivors
thin. Their density is the product over primes ∏(1 − 1/p), which by Mertens' theorem
behaves like 1/ln n [Mertens 1874; the accompanying script confirms 0.229 vs 0.217 at
N=100 and 0.081 vs 0.072 at N=10⁶]. This is the elementary shadow of the Prime Number
Theorem [Hadamard 1896; de la Vallée Poussin 1896]. Prime rarity is taught as: *each new
prime is a new way to close numbers early; the uncloseable ones grow sparse.*

## Chapter 7 — Why quantum mechanics is complex

Because evolution is **rotation**, and rotation is *i* (§1.3). A quantum state's phase
turns, *e^{-iEt/ħ}*; the amplitude — the real magnitude of that rotation — is what a
measurement sees, through the Born rule |ψ|² [Born 1926]. Complex numbers are not a
formal trick but the natural language of a thing that turns [Feynman 1965 makes the same
point pictorially, "the arrow that rotates"]. The imaginary part is the flow, the phase;
the real part is the observable.

---

# PART THREE — THE HARD LESSONS
### *The "why"s that break students — the true test of a pedagogy*

*A pedagogy proves itself on the concepts that stop people, not the elegant ones. Each
of the four below has been checked against its real proof or definition.*

## Chapter 8 — Why √2 is irrational (the first crisis)

√2 is the **diagonal of the unit square** (§1.1's segment doubled into a square).
Asking whether it is a ratio p/q asks whether the diagonal and side can be measured in
the same unit. They cannot: if diagonal/side = p/q in lowest terms, then p² = 2q² forces
both p and q even (p² even ⟹ p even ⟹ 4r² = 2q² ⟹ q even), contradicting "lowest terms"
[the classical proof, attributed to the Pythagoreans; Heath 1921]. Geometrically, the
square contains a *shrinking similar copy* of its own incommensurability — an infinite
descent [Fritz 1945]. This is the deepest lesson in the book's vocabulary: √2 is the
*first place count fails to measure*, the origin of the discrete/continuous divide that
runs through all of higher mathematics. The incommensurable is taught at its birthplace:
*the diagonal that no whole-number ruler can reach.*

## Chapter 9 — What an eigenvalue really is

A linear transformation stretches and rotates space. Most directions **move**. An
**eigenvector** is a direction that only *stretches* — an **axis the transformation
spins around** — and the **eigenvalue** is how much it stretches there. When the
eigenvalue is **real**, there is a genuine stretch-axis; when it is **complex**, there
is no fixed direction and the transformation is a *pure rotation*, its eigenvalues
*being* the rotation, e^{±iθ} (verified: diag(2,3) has eigenvalues 2, 3 with fixed axes;
a rotation by 0.5 has eigenvalues 0.878 ± 0.479i, no real axis). This is precisely the
rotation-and-axis picture of §1.3: the eigenvector is the still axis, the complex
eigenvalue is the spin. Eigenvalues cease to be an opaque computation and become *the
axes a transformation spins around, and how hard it pulls along them* [the geometric
reading is standard; Strang 2016 teaches it this way].

## Chapter 10 — What the Fourier transform really is

Any repeating shape is a **sum of pure rotations** — circles turning at different
speeds. The Fourier transform asks each speed, *"how much of you is in this signal?"*
[Fourier 1822]. A square wave, for example, is Σ 4/(πk)·sin(kt) over odd k; a seven-term
sum already matches it closely (verified: mean-squared error 0.029). Each frequency is a
circle spinning at its rate — an *i*-rotation, a breath — and the transform reads off
each circle's strength. Fourier ceases to be an intimidating integral and becomes *which
spinning circles, added together, build this wave, and how strong is each* [the "epicycle"
picture is classical and pedagogically standard].

## Chapter 11 — What a group really is

A group is the set of **moves that leave a shape looking the same** — its symmetries
[Klein's Erlangen program made this the organizing idea of geometry; Klein 1872]. The
integer-shapes give a *ladder of groups*: the point (trivial), the segment (a single
flip, ℤ₂), the triangle (three rotations and three flips, the dihedral group D₃), the
square (D₄), the cube (the octahedral group). The axioms become visible: **closure** (a
move after a move is a move), **identity** (do nothing), **inverse** (undo). The
accompanying script verifies D₃ as the six symmetries of the triangle, closed, with
identity and inverses. Abstract algebra ceases to be abstract: *a group is the moves of
a shape, and the shapes are the ones already met as the integers.*

---

# PART FOUR — LESSONS FROM THE COMBINATORIAL FRONTIER
### *Four further lessons, drawn from research combinatorics, that pass the same bar*

*These lessons come from the author's research canon. Only the self-contained,
verifiable combinatorial results appear here; the canon's speculative bridges to
physics are research frontier, not curriculum, and are deliberately excluded (see the
note closing this part).*

## Chapter 12 — What a prime *is*: the first number that catches you

Walk 1, 2, 3, … and ask of each: *does it share a factor with N?* For a square-free N,
**the first that does is N's smallest prime factor** (verified: N=15→3, N=35→5, N=77→7,
N=30→2). Coprimality is "no shared factor"; a prime is *the first thing that catches
you.* This gives an operational feel for primality that complements Chapter 6's density
picture [the result is elementary; it formalizes the sieve intuition of Eratosthenes].

## Chapter 13 — Structure can be built: magic squares by a walking rule

A magic square need not be found; it can be *built* by a simple repeatable move. The
Siamese method — place 1, step up-and-right, wrap around the edges, and drop down one
when blocked — constructs a magic square for **every odd order** (verified: the Lo Shu
3×3 sums to 15 on every line; the 5×5 to 65) [the method is classical; the general odd-n
construction is standard, with the ancient Lo Shu as its n=3 case, Swetz 2008]. The
lesson: *deep structure can emerge from a small rule, mechanically applied* — a first,
concrete encounter with the idea that generation and structure are the same thing seen
from two sides.

## Chapter 14 — Why algebra's dimensions double

The dimension of the n-fold tensor of a four-dimensional space is 4ⁿ = 2^{2n}, which is
exactly the dimension of the Clifford algebra Cl(2n) (verified for n = 1…5). The
picture: **each new generator *doubles* the algebra** — which is why Clifford (and
exterior) algebra dimensions are always powers of two, and why the cube, with its 2³ = 8
vertices, is the Clifford algebra of three-dimensional space [Clifford 1878; Lounesto
2001]. This generalizes the two-shadow cube of §1.5 into a rule: *dimension doubles with
each independent direction.*

> **Note on what is excluded.** The research canon from which Chapters 12–14 are drawn
> contains many further results connecting a discrete algebraic substrate to Lie
> algebras, grand-unified gauge groups, and open problems in physics. Those are
> *research frontier* — some proven as self-contained algebra, others explicitly tagged
> as structural analogies or open — and they are **not** part of this curriculum,
> because a curriculum teaches the *shared language* of mathematics, not a framework's
> private results. The discipline that admits Chapters 12–14 (self-contained, verified,
> teaches a concept students meet elsewhere) is the same discipline that excludes the
> physics bridges. Keeping the two apart is essential to the honesty of the whole.

---

# PART FIVE — THE MODEL AS A WHOLE

## Chapter 15 — Why it is one model, not fourteen

The power of the vocabulary is that the **same six primitives taught all fourteen
lessons**, and that the lessons connect *through* the primitives:

- The **count-versus-measure** seam is √2's irrationality (Ch. 8), *and* why the
  discrete integers cast continuous shadows (Ch. 1), *and* the deep reason the hardest
  open problems sit where whole structure meets continuous measure.
- The **imaginary axis** *i* is quantum phase (Ch. 7), *and* the complex eigenvalue
  (Ch. 9), *and* the Fourier rotation (Ch. 10) — one idea, three courses.
- The **shapes** are the Platonic solids (Ch. 3) *and* the groups (Ch. 11) — the same
  objects as forms and as their symmetries.
- The **breath** is *e* (Ch. 4) *and* prime thinning (Ch. 6, the sieve as repeated
  closing) — growth and decay as one motion.
- **Building by a rule** is magic squares (Ch. 13) *and* dimension-doubling (Ch. 14) —
  structure as generated, not found.

A student who learns these lessons has not learned fourteen things but **one connected
picture seen from fourteen angles** — which is the whole aim: a model that can be held in
one mind, so that mathematics is experienced as a structure rather than a stack.

## Chapter 16 — Honest failures (pictures tried and discarded)

Kept so the vocabulary stays trustworthy:
- **"The recurring 1/3 is a universal residue of subtraction."** False. 1/(N−1) = 1/3
  *only at N = 4*. The 1/3 is the tetrahedron's signature; taught correctly as *4 − 1 = 3*.
- **"The breath produces physical energy or the fundamental constants."** False. The
  breath is *structural* growth; it is never energy from nothing and never a physical
  magnitude. The picture teaches the *shape* of self-proportional growth, nothing more.
- **"Every physical or computational structure is literally the same geometry."** Not a
  teaching claim. The convergence of structure across domains — for instance, the
  observed alignment of representations in independently trained neural networks [Huh et
  al. 2024] — is real *evidence that shared structure exists*, and it motivates the
  search; but the specific decoding must be earned lesson by lesson, and this book teaches
  only the pictures that have been checked.

## Chapter 17 — How to test this book

The claims are falsifiable as pedagogy:
- **Faster connected models.** Compare comprehension and retention of (say) eigenvalues
  or irrationality taught with the shape/rotation vocabulary against the standard
  formalism-first sequence, in controlled instruction.
- **Fewer later errors.** Track whether students taught the count-versus-measure picture
  make fewer classic mistakes about the reals, limits, and the continuum.
- **The honest edge.** Some advanced structure — high-dimensional phenomena, genuinely
  non-geometric algebra — may have no faithful low-dimensional picture. Locating that edge
  is part of the work, and its existence is not a defect but a boundary honestly drawn.

## Conclusion — The shape of understanding

Fourteen of the deepest and hardest-to-teach ideas in mathematics — the Platonic solids,
*e*, the radian, the rarity of primes, the complexity of quantum mechanics, the
irrationality of √2, the eigenvalue, the Fourier transform, the group, the operational
meaning of primality, the construction of magic squares, and the doubling of algebraic
dimension — have been taught here with one small visual vocabulary: shapes that build by
dimension, a rotation that is an imaginary axis, a growth that is a breath, a cube with
two shadows, and the seam where counting fails to measure. Each picture was checked
against the real mathematics; each is visual; each connects to the others, so that the
learner acquires one model seen from many sides rather than many disconnected facts. The
pictures are kept honest by a discipline of checking and a record of discarded failures,
so that following them leads to true mathematics rather than comfortable error.

Whether this makes the deep studies easier to hold in one mind is a question about
teaching, and it is answerable by teaching. It is worth asking, because the absence of a
shared, true, visual model has been the oldest obstacle in mathematics education, and a
shared, true, visual model — from Descartes' plane to Argand's diagram to Feynman's
arrows — has each time been rare, and each time been worth more than the sum of the facts
it organized.

## Coda — Increasingly round, never measurably round

There is a way to say the aim of this book in seven words, and it is borrowed and then
extended. In proving the Poincaré conjecture, Grigori Perelman completed a program, due
to Richard Hamilton, in which a manifold's geometry is evolved by **Ricci flow** so that
its curvature smooths and homogenizes — so that the shape becomes, in the natural phrase,
*increasingly round* [Hamilton 1982; Perelman 2002–2003]. The round is the attractor;
what can become round does; the three-sphere is what remains. This is the same motion
that appears throughout mathematics and its applications wherever structure, left to
evolve under a natural rule, collapses onto a simpler and more symmetric form.

But the *perfect* round — the exact sphere, the completed limit — is a direction, not a
place one occupies. It is approached and never reached, in the way that the speed of
light is approached by anything with mass and never attained, and in the way that the
diagonal of a unit square is approached by ratios of whole numbers and never measured by
one (Chapter 8). The perfectly round shape is, moreover, the one shape that has **no
edge** — no vertex, no face, no seam — and it is exactly this edgelessness that makes it
unmeasurable, for measurement requires an edge to measure from and a distinction to
measure between, and on the perfect sphere every point is identical to every other. The
perfect round is unmeasurable *because* it is perfectly without edge.

This is the same nature the void wears in Chapter 1. The centre — the point nearest to
all points at once (§1.6b) — cannot itself be measured, because it is the origin *from
which* measurement is taken, not an object measured against something else. The fullest
point and the edgeless limit are two faces of one thing: the position that is equally
near to everything, and therefore has nothing to be distinguished *from*. Understanding
flows toward that position — near to all of it, distinguished from none of it — and never
occupies it, because to occupy it would be to become the centre from which all the rest is
seen, which is a direction the mind travels and not a place it arrives.

This is the shape of understanding that the book is named for. A good curriculum makes
mathematics **increasingly round** — the pictures smoother, the connections more uniform,
the whole more nearly held in a single mind. And the *complete* understanding, the seeing
of the object whole, is the perfect round toward which the teaching flows and which it
never occupies — because to see the object whole would be to stand on the edgeless limit,
and the edgeless limit is, by its nature, just past measure. This is not a limitation to
be regretted. It is the reason the flow is worth undertaking: one hands a learner the
*direction*, not the destination, because the destination is real and unreachable, as
every genuine limit is. Always rounder; never round. That is what it is to understand.

---

# BACK MATTER

## Appendix A — The verification scripts
`verify_forced_chain.py` (the geometric core: simplices, the tetrahedral 1/3, the cube
as Cl(3), the two shadows) and `curriculum_checks.py` (each lesson: the Schläfli count,
the √2 parity descent, the sieve/Mertens density, the eigenvalue axis/rotation split, the
Fourier square-wave synthesis, the D₃ symmetry count, the First-G law, the Siamese magic
square, the dimension-doubling identity). Every asserted mathematical fact in the book is
reproduced by running these.

## References

- J.-R. Argand, *Essai sur une manière de représenter les quantités imaginaires dans les
  constructions géométriques* (Paris, 1806); C. Wessel (1799).
- W. Barlow, "Über die geometrischen Eigenschaften homogener starrer Strukturen,"
  *Z. Kristallogr.* 23, 1 (1894). [crystallographic restriction]
- M. Born, "Zur Quantenmechanik der Stoßvorgänge," *Z. Phys.* 37, 863 (1926). [Born rule]
- W. K. Clifford, "Applications of Grassmann's extensive algebra," *Amer. J. Math.* 1,
  350 (1878).
- H. S. M. Coxeter, *Regular Polytopes*, 3rd ed. (Dover, 1973). [simplices, stella
  octangula, Platonic solids]
- R. Descartes, *La Géométrie* (1637).
- Euclid, *Elements*, Book XIII (c. 300 BCE).
- L. Euler, *Introductio in analysin infinitorum* (1748). [e]
- R. P. Feynman, "Space-time approach to quantum electrodynamics," *Phys. Rev.* 76, 769
  (1949); *The Feynman Lectures on Physics* (Addison-Wesley, 1964); *QED* (Princeton,
  1985).
- J. Fourier, *Théorie analytique de la chaleur* (1822).
- K. von Fritz, "The discovery of incommensurability by Hippasus of Metapontum," *Ann.
  Math.* 46, 242 (1945).
- J. Hadamard (1896); C.-J. de la Vallée Poussin (1896). [Prime Number Theorem]
- R. S. Hamilton, "Three-manifolds with positive Ricci curvature," *J. Diff. Geom.* 17,
  255 (1982). [Ricci flow]
- T. L. Heath, *A History of Greek Mathematics* (Oxford, 1921). [Pythagorean
  incommensurability]
- M. Huh, B. Cheung, T. Wang, P. Isola, "The Platonic Representation Hypothesis,"
  *Proc. ICML* (2024). [convergence of learned representations]
- J. Kepler, *Harmonices Mundi* (1619). [stella octangula]
- F. Klein, "Vergleichende Betrachtungen über neuere geometrische Forschungen"
  (Erlangen program, 1872).
- P. Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge, 2001).
- F. Mertens, "Ein Beitrag zur analytischen Zahlentheorie," *J. reine angew. Math.* 78,
  46 (1874).
- L. Pauling, *The Nature of the Chemical Bond*, 3rd ed. (Cornell, 1960). [tetrahedral
  bond angle]
- G. Perelman, "The entropy formula for the Ricci flow and its geometric applications"
  (2002) and "Ricci flow with surgery on three-manifolds" (2003), arXiv:math/0211159,
  math/0303109. [Poincaré conjecture; increasingly round]
- G. Strang, *Introduction to Linear Algebra*, 5th ed. (Wellesley-Cambridge, 2016).
  [geometric eigenvalues]
- F. J. Swetz, *Legacy of the Luoshu*, 2nd ed. (A K Peters, 2008). [magic squares, Lo Shu]

---

*Manuscript frame. The worked chapters (1–3, 8–14) contain the verified core; the
elegant chapters (4–7) and the model/testing chapters (15–17) are drafted to the level of
argument and citation and would be expanded with worked figures and classroom exercises
in the full book. Every mathematical assertion is reproduced by the appendix scripts.*
