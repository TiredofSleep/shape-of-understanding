# Draft: two boxes for Chapter 13 (for the author's read)

**Status:** draft, 2026-10-22. These are not in the book. If the author wants them, they go after
Chapter 13's paragraph as 13.1 and 13.2. Their checks are in
[`ch13_boxes_checks.py`](ch13_boxes_checks.py) and would then move into `curriculum_checks.py`, and the
book's "91 checks" would be updated. They come from the handoff of 2026-10-22: the magic-square work in
[`trinity-infinity-geometry/towers/binary_magic`](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/main/towers/binary_magic).

**His lines** (from the ledger; the October line is as quoted in the handoff, not yet checked against
the chat):
- For 13.1: "also need to be moving in discrete trinary and binary across progressive sequences
  depending on the lattice theres your final geometry i think... the map seems to hold a lot of color"
  (≈ 2 Feb 2026).
- For 13.2: "all things are binary, and every one is three" (2 May 2026). Also "a full binary matrix
  assembly for the whole world of possible magic squares built by the cube's corners" (October 2026).

**The wall holds.** Neither box uses the solid faces of 5, 7 or 9. The physics in 13.1 is a fenced
illustration, stated as a known result. The knot in 13.2 is a drawing, and the box says so.

---

**13.1 Lo Shu in four colours (extension).** Take the Lo Shu and subtract 1 from every number, so that
it holds 0 to 8. Then write each number in base three, with two digits: 3 is 10, 8 is 22, and 4 is 11.
- **The first digits alone** form a *Latin square*: each of 0, 1 and 2 appears once in every row and
  once in every column.
- **The second digits alone** form another.
- **Laid one over the other**, every pair of digits appears exactly once. Two Latin squares that fit
  together like this are called *orthogonal*. Magic squares have been built this way for three
  centuries [de La Hire 1705; Euler 1782].

That is why the Lo Shu is magic. Each row holds every digit once in each place, so every row adds up
the same (verified). On each diagonal, one digit place holds the middle digit, 1, three times, and
1 + 1 + 1 is the same as 0 + 1 + 2.

Now use four symbols instead of three: base four, with the digits 1, 2 and 3. The square

    11 13  6
     5 10 15
    14  7  9

is magic, with every line summing to 30, and its base-four digits again make two orthogonal Latin
squares (verified). In binary, 1, 2 and 3 are 01, 10 and 11. Any two of them XOR to the third, and
every row and every column of this square XORs to zero (verified). It is the only 3×3 magic square
with sum 30 that does that (verified).

**The four colours.** Give the four base-four digits four names: 0 = I, 1 = Z, 2 = X, 3 = Y. These are
the names of the basic measurements on a *qubit*, a quantum bit. A two-digit number is then a
measurement on two qubits: 11 is XY, 13 is YZ, and 6 is ZX. Read this way, the square is the
**Mermin–Peres square** of quantum physics [Mermin 1990; Peres 1990].
- The three measurements in a row can be made together, and so can the three in a column.
- Multiply the three results in a row and you always get −1. Do the same for a column and you
  always get +1.
- No list of nine answers fixed in advance, each +1 or −1, can do both. Multiplying all nine answers
  row by row gives −1, and column by column gives +1 (verified).

Quantum mechanics does both, and experiments agree. **The fence:** this is a picture of a known
result in physics, not physics derived from a magic square. The numbers line up because XOR is how
these measurements combine. The paradox needs +1 and −1 to meet, and in binary they do: 1 ⊕ 1 = 0.

---

**13.2 The odometer ties a knot (extension).** An odometer with only the digits 0 and 1 counts 000,
001, 010, 011, 100, and so on. Usually one wheel turns. From 0111 to 1000 every wheel turns at once:
the full ripple. Number the cube's eight corners 000 to 111, and the four-dimensional cube's sixteen
corners 0000 to 1111. Those are the sixteen numbers that fill a 4×4 magic square: subtract 1 from
every number in Dürer's.

**Split a square into layers.** Write every number in the square in binary, and split the square into
four layers of 0s and 1s: the 8s digits, the 4s, the 2s and the 1s. In 1931, F. Fitting, building on an
idea of his son Hans, then a mathematics student, proved that in every one of the 880 squares each
layer has exactly two 1s in every row and every column [Fitting 1931] (verified). So along the rows and
columns the magic is shared out evenly, layer by layer, and adding up never needs a carry.

**Only the diagonals carry.** On a diagonal, two 1s can stand in for one 2. The carries follow rules
you can check with pencil and paper:
- no carry is used twice;
- the carries a square uses form an unbroken chain;
- "1s to 2s" together with "4s to 8s", without "2s to 4s" between them, never happens. The four
  lines that try it sum to 20, 24, 36 or 40, never 30 (verified).

Counted by how many carries their diagonals use, the squares number 528, 192, 112 and 48 [Fitting
1931] (verified).

**The 48.** In these, not one layer is balanced on its own: the balance exists only in the whole.
Their diagonals hold the full ripple. The low layers fall short by 1 + 1 + 2 + 4 = 8, and that is paid
as one extra 8, which is 0111 + 1 = 1000 again (verified).

**The knot.** Now draw the three carries as the three crossings of the simplest knot picture, the
trefoil. Each crossing goes over or under according to the sign of its carry.
- Of the eight ways to set three crossings, only the two in which all three agree make a real knot.
  The other six pull apart into a plain loop (verified).
- The carry rules say that carries next to each other always share a sign. So whenever all three
  are used, they agree, and **exactly the 48 tie a trefoil** (verified).

**The fence:** the knot is our drawing of a rule about carries, not a property of magic squares.
Change the drawing and the knot changes with it. The arithmetic underneath does not.

---

**References to add** (if the boxes go in):
- P. de La Hire, "Nouvelles constructions et considérations sur les quarrés magiques", *Mémoires de
  l'Académie Royale des Sciences* (1705).
- L. Euler, "Recherches sur une nouvelle espèce de quarrés magiques" (1782).
- F. Fitting, "Rein mathematische Behandlung des Problems der magischen Quadrate von 16 und von 64
  Feldern", *Jahresbericht der DMV* 40 (1931) 177–199.
- N. D. Mermin, "Simple unified form for the major no-hidden-variables theorems", *Phys. Rev. Lett.*
  65 (1990) 3373.
- A. Peres, "Incompatible results of quantum measurements", *Phys. Lett. A* 151 (1990) 107.
