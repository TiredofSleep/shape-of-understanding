# Treatment lesson — the eigenvalue as axis-and-rotation (~15 min)

*The picture under test. Deliver verbatim in tone; the instructor may answer
questions but must not import the control's characteristic-polynomial framing.*

## 1. The idea (3 min)

A matrix *moves* the plane — it stretches it, shears it, spins it. Watch what
happens to directions. **Most directions get knocked off their line.** But some
special directions don't: the matrix only makes them **longer or shorter**,
without turning them off their own line. Such a direction is an **eigenvector** —
*an axis the transformation acts along* — and the factor it stretches by is the
**eigenvalue**.

## 2. Two kinds of eigenvalue (5 min, with the picture)

Draw the unit circle; apply the matrix; see where it goes.

- **A stretch**, e.g. `[[2,0],[0,1]]`: the circle becomes an ellipse. The long
  and short axes of the ellipse are directions that only got *scaled* — real
  eigenvectors, with **real eigenvalues** 2 and 1. *A real eigenvalue is a genuine
  stretch-axis.*
- **A rotation**, e.g. turn everything by 60°: the circle maps to itself, and
  **no direction stays on its own line** — every arrow gets turned. There is no
  real stretch-axis. The eigenvalues are **complex**, `e^{±iθ}`. *The complex
  eigenvalue is the rotation itself.* (Recall: multiplying by *i* is a quarter
  turn; a complex number of size 1 is a rotation.)

So the eigenvalue tells you *which of the two things the matrix is doing along
that direction*: **real = stretch along an axis; complex = turn, no axis.**

## 3. Worked example (5 min)

- `[[3,0],[0,-2]]`: eigenvalues 3 and −2 (both real) → two stretch-axes (the −2
  also flips). Draw the axes.
- `[[0,-1],[1,0]]` (90° rotation): eigenvalues `+i, −i` (complex, size 1) → no
  real axis; the whole plane turns a quarter. Draw the circle mapping to itself.
- One mixed: `[[2,-1],[1,2]]` = scale √5 and rotate; eigenvalues `2 ± i` → it
  *both* grows and turns (a spiral). Point at the growth (size) and the turn
  (the imaginary part) separately.

## 4. One-sentence takeaway (give it explicitly)

> An eigenvector is an axis the transformation acts along; a real eigenvalue
> means it stretches there, and a complex eigenvalue means there is no fixed axis
> — the transformation is turning.
