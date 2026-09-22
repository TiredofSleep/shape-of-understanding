# Assessments — four instruments with rubrics

All four are scored **blind to arm**. Give the immediate quiz at the end of the
lesson; the retention quiz (a parallel form) unannounced at two weeks; the
transfer and connection items with the retention session.

---

## §1 Immediate comprehension (0–6) — end of lesson

One point each.

1. Define an eigenvector in your own words. *(Key: a direction/vector the matrix
   maps to a scalar multiple of itself; A·v = λv.)*
2. What does the eigenvalue tell you about that direction? *(Key: the factor it is
   scaled by — how much it stretches/shrinks, sign = flip.)*
3. `[[5,0],[0,2]]` — give its eigenvalues. *(Key: 5 and 2.)*
4. True/false: a pure rotation of the plane (not by 0° or 180°) has real
   eigenvalues. *(Key: false.)*
5. A matrix has eigenvalues 3 and 0.5. Describe what it does. *(Key: stretches ×3
   along one axis, shrinks ×½ along another.)*
6. A matrix has eigenvalues 2 ± i. Name the two things it does. *(Key: scales
   (grows) **and** rotates — a spiral.)*

## §2 Retention (0–6) — parallel form, two weeks later, unannounced

Same six item-types, new numbers (e.g. Q3 `[[4,0],[0,7]]`; Q5 eigenvalues 2 and
0.25; Q6 eigenvalues 1 ± 2i). Same key structure.

## §3 Transfer (0–4) — PRIMARY OUTCOME — taught in neither arm

> **Item.** Consider the shear `S = [[1,1],[0,1]]`. Does it have a real
> stretch-axis — a direction it only scales, without turning off its line? If so,
> which direction and by how much? If not, explain what it does instead. Then say
> what its eigenvalues must be.

Scored 0–4:
- **+1** identifies that a direction fixed up to scaling is what's being asked.
- **+1** finds the direction (the x-axis, (1,0)) is mapped to itself (scale 1).
- **+1** reasons about whether there is a *second* independent such axis (there is
  not — S is not diagonalizable; only the one line is invariant).
- **+1** concludes both eigenvalues equal 1 (real, repeated), consistent with a
  shear that neither uniformly scales nor purely rotates.

*This item rewards reasoning with axes/invariant directions. A student can also
reach it via the characteristic polynomial (λ−1)² = 0; graders score the
reasoning, not the route, blind to arm.*

## §4 Connection prompt (0–2) — secondary

> **Item.** In one or two sentences: what, if anything, does the eigenvalue of a
> rotation have to do with the Fourier transform?

Scored 0–2:
- **+1** mentions rotation / circular motion / `e^{iθ}` / complex phase in either.
- **+1** connects them: a rotation's eigenvalue *is* `e^{iθ}`, and the Fourier
  transform builds a signal from rotations (spinning circles) at different rates —
  the same "complex number = a turn" idea.
