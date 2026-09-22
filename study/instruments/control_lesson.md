# Control lesson — eigenvalues, formalism-first (~15 min)

*The matched control: same content, same length, same number of worked examples,
delivered in the standard order. The instructor must not import the treatment's
axis/rotation picture.*

## 1. Definition (3 min)

For a square matrix *A*, a nonzero vector **v** is an **eigenvector** with
**eigenvalue** λ if *A***v** = λ**v**. Equivalently (*A* − λ*I*)**v** = 0 has a
nonzero solution, which requires **det(*A* − λ*I*) = 0** — the **characteristic
equation**.

## 2. Method (5 min)

To find eigenvalues: form *A* − λ*I*, take its determinant, set it to zero, and
solve the resulting **characteristic polynomial** for λ. To find each eigenvector:
substitute λ back and solve (*A* − λ*I*)**v** = 0.

For a 2×2 matrix `[[a,b],[c,d]]` the characteristic polynomial is
λ² − (a+d)λ + (ad − bc) — trace and determinant. Roots may be real or complex.

## 3. Worked example (5 min)

- `[[3,0],[0,-2]]`: char. poly λ² − λ − 6 = 0 → λ = 3, −2. Eigenvectors (1,0)
  and (0,1).
- `[[0,-1],[1,0]]`: char. poly λ² + 1 = 0 → λ = ±i. Solve for the (complex)
  eigenvectors.
- `[[2,-1],[1,2]]`: char. poly λ² − 4λ + 5 = 0 → λ = 2 ± i.

## 4. One-sentence takeaway (give it explicitly)

> The eigenvalues of a matrix are the roots of its characteristic polynomial
> det(*A* − λ*I*) = 0, and each eigenvector solves (*A* − λ*I*)**v** = 0.
