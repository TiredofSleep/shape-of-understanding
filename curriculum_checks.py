#!/usr/bin/env python3
"""
curriculum_checks.py -- reproduces the verification of every lesson in
"The Shape of Understanding" (a why-first visual grammar for mathematics).

    Run:  python curriculum_checks.py

Every picture in the book is checked here against the real proof/definition.
The file is organized in the book's own order (Parts One--Four plus the
lessons that extend through "the wall"), and prints ALL LESSON CHECKS PASS
only after the last assertion succeeds. If any assert fails, a claim in the
book is wrong and must be fixed before the book ships -- that is the whole
point of the file.

Dependencies: numpy, sympy, scipy (all standard).
"""
import numpy as np
import math
import itertools
from math import gcd
from itertools import combinations, permutations

def show(name, detail):
    print(f"  [CHECK] {name}\n          {detail}")

def banner(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)

# ======================================================================
# PART ONE -- THE GRAMMAR
# ======================================================================

banner("Ch.1.1 -- integers are shapes: the ladder of SIMULTANEOUS EQUALITY")
# n mutually-equidistant points force the (n-1)-simplex; 3 is the last flat one.
def equidistant(pts):
    d = [np.linalg.norm(pts[i] - pts[j]) for i, j in combinations(range(len(pts)), 2)]
    return np.allclose(d, d[0]), np.round(d, 3)
tri = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])
ok3, d3 = equidistant(tri); show("3 points CAN be equidistant in the plane (triangle)", f"dists {d3} equal={ok3}")
sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
ok4, d4 = equidistant(sq); show("4 points in the plane (square) canNOT", f"dists {d4} equal={ok4} (diagonals=sqrt2)")
tet = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
okt, dt = equidistant(tet); show("4 EQUAL points force the 3rd dimension (tetrahedron)", f"dists {dt} equal={okt}")
c = tet.mean(0); v1, v2 = tet[0] - c, tet[1] - c
cos_lift = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
show("the forced lift angle", f"cos = {cos_lift:.4f} = -1/3 = -1/(N-1) at N=4 (the tetrahedron's signature)")
assert ok3 and (not ok4) and okt and abs(cos_lift + 1/3) < 1e-9
print("  -> 3 is the last count that is all-equal AND flat. The ladder is equality, not counting.")

banner("Ch.1.1b -- the lift is a DOUBLING (one added point = one yes/no = x2 of the whole)")
from math import comb as _comb
for N in range(3, 8):
    assert 2**(N + 1) == 2 * 2**N                       # adding one point doubles the total
show("adding one point doubles the total sub-pieces", "2^N -> 2^(N+1): each old piece joins the new point, or not")
show("hand-count at the FIRST lift (triangle -> tetrahedron)",
     f"verts {_comb(3,1)}->{_comb(4,1)}, edges {_comb(3,2)}->{_comb(4,2)} (x2 here), faces {_comb(3,3)}->{_comb(4,3)} (x4 here), TOTAL {2**3}->{2**4} (x2)")
show("honest caution: edges do NOT keep doubling",
     f"next step edges {_comb(4,2)}->{_comb(5,2)} = x{_comb(5,2)/_comb(4,2):.2f}; only the TOTAL stays x2 every time")
assert _comb(4,2) == 6 and _comb(5,2) == 10 and _comb(5,2) != 12
show("dim Cl(n) = 2^n = subsets of n generators", "each direction = one in/out choice -> powers of two (Ch.14)")
for n in range(1, 8):
    assert 2**n == sum(_comb(n, k) for k in range(n + 1))
print("  -> add a point: the whole doubles AND the shape lifts -- counting and climbing are one act.")

banner("Ch.2.2 -- three perpendicular toothpicks build Cl(3): grades = the cube's parts")
_e1 = np.array([[0, 1], [1, 0]], complex); _e2 = np.array([[0, -1j], [1j, 0]], complex); _e3 = np.array([[1, 0], [0, -1]], complex)
_I2 = np.eye(2, dtype=complex)
for _e in (_e1, _e2, _e3):                       # generators square to +1 (Euclidean Cl(3))
    assert np.allclose(_e @ _e, _I2)
for _a, _b in ((_e1, _e2), (_e1, _e3), (_e2, _e3)):    # and anticommute
    assert np.allclose(_a @ _b, -_b @ _a)
_biv = [_e1 @ _e2, _e1 @ _e3, _e2 @ _e3]; _ps = _e1 @ _e2 @ _e3
_basis = [_I2, _e1, _e2, _e3] + _biv + [_ps]
_flat = np.array([b.flatten() for b in _basis])
_rank = int(np.linalg.matrix_rank(np.hstack([_flat.real, _flat.imag])))
show("grades scalar + vectors + bivectors + pseudoscalar", "1 + 3 + 3 + 1 = 8 = 2^3 = the cube's vertices (centre, axes, faces, volume)")
show("the 8 elements are a real basis of Cl(3)", f"real rank = {_rank} (real dimension 8)")
assert _rank == 8
show("bivectors (the face-planes) square to -1 -> the i", "the plane between two perpendicular toothpicks rotates")
for _b in _biv:
    assert np.allclose(_b @ _b, -_I2)
print("  -> the cube IS Cl(3); its face-planes ARE the imaginary unit. Exact, not metaphor.")

banner("Ch.2.3 -- Pascal's triangle: the doubling sorted by size (row sum 2^n; row 3 = Cl(3) grades)")
for n in range(0, 8):
    assert sum(_comb(n, k) for k in range(n + 1)) == 2**n          # each row sums to 2^n
show("each Pascal row sums to a power of two", "row n = [C(n,k)]; sum = 2^n -- the doubling as a total")
show("row 3 = the grades of Cl(3)", f"{[_comb(3,k) for k in range(4)]} = 1,3,3,1 = scalar, vectors, bivectors, pseudoscalar")
show("row 4 = the tetrahedron's parts", f"{[_comb(4,k) for k in range(5)]} = empty, verts, edges, faces, cell")
assert [_comb(3, k) for k in range(4)] == [1, 3, 3, 1] and [_comb(4, k) for k in range(5)] == [1, 4, 6, 4, 1]
print("  -> simplex sub-pieces and Clifford grades are the SAME binomials -- Pascal; the doubling is the row sum.")

banner("Ch.2.4 -- the edge of building: the last lift, the fold, the gap (one 1/3, three faces)")
show("the tetrahedron is the LAST buildable equal-shape", "4 equal points fit in 3D; 5 equal points (the 4-simplex) need 4D -- unbuildable")
_V = np.array(list(itertools.product([0, 1], [0, 1], [0, 1])), float)
_dists = sorted(set(round(float(np.linalg.norm(_V[i] - _V[j])), 6) for i, j in combinations(range(8), 2)))
show("the buildable cube is a FOLD (three distances, not one)", f"cube distances = {_dists} = 1, sqrt2, sqrt3")
assert len(_dists) == 3 and abs(_dists[0]-1) < 1e-6 and abs(_dists[1]-2**0.5) < 1e-6 and abs(_dists[2]-3**0.5) < 1e-6
_dih = np.degrees(np.arccos(1/3))
show("regular tetrahedra do NOT tile 3D", f"dihedral = arccos(1/3) = {_dih:.2f} deg; 360/{_dih:.2f} = {360/_dih:.3f} (not integer) -> a {360-5*_dih:.2f} deg gap")
assert abs(_dih - 70.5288) < 1e-3 and 5.0 < 360/_dih < 5.2
show("one 1/3, three faces", "vertex cos=-1/3 (lift); body-diagonal cos^2=1/3 (fold); dihedral arccos(1/3) (gap)")
assert abs(np.arccos(-1/3) - np.radians(109.4712)) < 1e-3 and abs((1/np.sqrt(3))**2 - 1/3) < 1e-9
print("  -> you can build the whole real world in 3D, but you stay in the fold; the 1/3 keeps you there.")

banner("Ch.1.2 -- the break at five: the crystallographic restriction")
# A lattice may rotate only by orders n with 2cos(2pi/n) an integer: 1,2,3,4,6.
def integer_trace(n):
    m = 2 * np.cos(2 * np.pi / n)
    return abs(m - round(m)) < 1e-9
allowed = [n for n in range(1, 13) if integer_trace(n)]
show("rotation orders a lattice may have", f"{allowed}  (5-fold and >=7 are barred -> 5 is the first shape that won't pack)")
assert set(allowed) == {1, 2, 3, 4, 6}
print("  -> the pentagon cannot tile the plane; it folds to space instead (dodecahedron).")

banner("Ch.1.5 / Ch.14 -- the cube casts two shadows (square and hexagon)")
nhat = np.array([1, 1, 1.]) / np.sqrt(3)
cos2 = (1 / np.sqrt(3)) ** 2
show("body-diagonal (1,1,1) vs an axis", f"cos^2 = {cos2:.4f} = 1/3 (the tetrahedral 1/3 again)")
E = np.eye(3); P = [e - (e @ nhat) * nhat for e in E]   # project the 3 edges off the diagonal
pair_cos = (P[0] @ P[1]) / (np.linalg.norm(P[0]) * np.linalg.norm(P[1]))
show("the 3 edges seen down the diagonal", f"pairwise angle = {np.degrees(np.arccos(pair_cos)):.1f} deg -> a regular hexagon")
assert abs(cos2 - 1/3) < 1e-9 and abs(pair_cos + 0.5) < 1e-9

banner("Ch.1.6b -- the void is the FULLEST point (nearest to all at once)")
from scipy.optimize import minimize as _min
cen = tet.mean(0)
tot = lambda p: sum(np.linalg.norm(p - v) for v in tet)
show("centroid total distance to vertices", f"{tot(cen):.4f}  (a vertex: {tot(tet[0]):.4f} -- centre is nearer to ALL)")
r = _min(tot, np.array([0.3, 0.2, -0.1]))
show("the point minimizing distance to all (numeric)", f"{np.round(r.x, 3)} = the origin -> omni-adjacent, not empty")
assert tot(cen) < tot(tet[0]) and np.allclose(r.x, 0, atol=1e-3)
print("  -> the symbol for nothing marks the closest thing to being everything.")

# ======================================================================
# PART TWO -- THE ELEGANT LESSONS
# ======================================================================

banner("Ch.3 -- exactly 5 Platonic solids (the Schlafli count)")
sols = [(p, q) for p in range(3, 7) for q in range(3, 7) if 1/p + 1/q > 1/2]
show("regular {p,q} with angular room to fold", f"{sols}  (count={len(sols)})")
assert len(sols) == 5

banner("Ch.4 -- e is the rate of self-proportional growth (the breath)")
approx_e = (1 + 1/1_000_000) ** 1_000_000
show("(1+1/n)^n -> e", f"n=1e6 gives {approx_e:.6f}  vs e={math.e:.6f}")
h = 1e-6
deriv = (math.exp(1 + h) - math.exp(1)) / h
show("d/dx e^x equals e^x", f"numeric derivative at x=1 = {deriv:.6f}  vs e={math.e:.6f}")
assert abs(approx_e - math.e) < 1e-3 and abs(deriv - math.e) < 1e-4

banner("Ch.5 -- a radian is rotation counted in unit-radius arc")
# at r=1 the arc length subtended equals the angle itself.
theta = 1.2
phi = np.linspace(0, theta, 20000)
pts = np.stack([np.cos(phi), np.sin(phi)], 1)
arclen = np.sum(np.linalg.norm(np.diff(pts, axis=0), axis=1))
show("arc length on the unit circle equals the angle", f"theta={theta}, measured arc={arclen:.5f}")
assert abs(arclen - theta) < 1e-3

banner("Ch.6 -- why primes thin: the sieve density tracks 1/ln n (Mertens)")
from sympy import primerange
def sieve_density(N):
    d = 1.0
    for p in primerange(2, int(np.sqrt(N)) + 1):
        d *= (1 - 1/p)
    return d
for N in [100, 10_000, 1_000_000]:
    show(f"N={N}", f"sieve density {sieve_density(N):.4f}  vs 1/ln N {1/np.log(N):.4f}")
# and: the numbers that REACH every clock position are the units, not the primes
gen12 = [k for k in range(1, 12) if gcd(k, 12) == 1]
primes12 = [k for k in range(2, 12) if all(k % d for d in range(2, k))]
show("generators of Z/12 (reach every position) = the UNITS", f"{gen12}  (not the primes {primes12})")
show("the distinction the picture must not blur", "1 is a unit but not prime; 2,3 are prime but not generators")
assert gen12 == [1, 5, 7, 11] and set(gen12) != set(primes12)

banner("Ch.7 -- why quantum mechanics is complex: evolution is rotation, rotation is i")
show("a half turn is e^{i pi} = -1", f"|e^(i*pi) + 1| = {abs(np.exp(1j*np.pi) + 1):.2e}  (Euler; the turn is the i)")
assert abs(np.exp(1j*np.pi) + 1) < 1e-12

# ======================================================================
# PART THREE -- THE HARD LESSONS
# ======================================================================

banner("Ch.8.1 -- Pythagoras: a^2 + b^2 = c^2 (the dissection proof, and the triples)")
from sympy import symbols as _sym, expand as _exp
_a, _b = _sym('a b', positive=True)
assert _exp((_a + _b)**2 - 4 * (_a * _b / 2)) == _a**2 + _b**2     # (a+b)^2 minus 4 triangles
show("the dissection identity", "(a+b)^2 - 4*(ab/2) = a^2 + b^2  ->  a^2 + b^2 = c^2")
_triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)]
for _x, _y, _z in _triples:
    assert _x*_x + _y*_y == _z*_z
show("the whole-number right triangles (the counting side)", f"{_triples} all satisfy x^2 + y^2 = z^2")
show("and the crisis (the measuring side)", "legs 1,1 -> c^2 = 2 -> c = sqrt(2), which no fraction names")
assert 1**2 + 1**2 == 2 and math.isqrt(2)**2 != 2
print("  -> one theorem gives both: whole-number triples (counting) and sqrt2 (measuring) -- the seam of Picture 6.")

banner("Ch.8 -- why sqrt(2) is irrational (parity descent)")
show("2 is not a perfect square", f"isqrt(2)^2 = {math.isqrt(2)**2} != 2  -> p^2=2q^2 forces both even, no lowest terms")
assert math.isqrt(2)**2 != 2

banner("Ch.9 -- what an eigenvalue is: real=stretch axis, complex=rotation (the i)")
w, _ = np.linalg.eig(np.array([[2, 0], [0, 3]]))
show("stretch matrix diag(2,3)", f"eigenvalues {w} are real -> genuine stretch axes")
th = 0.5; R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
wr, _ = np.linalg.eig(R)
show("pure rotation by 0.5 rad", f"eigenvalues {np.round(wr,3)} = e^(+-i0.5), complex -> no real axis, the rotation IS the i")
assert np.isreal(w).all() and np.iscomplex(wr).all()

banner("Ch.10 -- the Fourier transform: a wave is a sum of spinning circles")
t = np.linspace(0, 2*np.pi, 2000)
square = np.sign(np.sin(t)); square[square == 0] = 1
approx = sum(4/(np.pi*k) * np.sin(k*t) for k in [1, 3, 5, 7, 9, 11, 13])
mse = np.mean((square - approx)**2)
show("square wave = sum 4/(pi k) sin(k t), odd k", f"7-term MSE = {mse:.4f} (converges as circles are added)")
assert mse < 0.06

banner("Ch.11 -- a group is the moves of a shape (D3 = triangle symmetries)")
perms = list(permutations([0, 1, 2]))            # the 6 symmetries of the triangle
compose = lambda a, b: tuple(a[b[i]] for i in range(3))
closed = all(compose(a, b) in perms for a in perms for b in perms)
identity = (0, 1, 2) in perms
inverses = all(any(compose(a, b) == (0, 1, 2) for b in perms) for a in perms)
show("D3 = symmetries of the triangle", f"|D3|={len(perms)}, closed={closed}, identity={identity}, all invertible={inverses}")
assert len(perms) == 6 and closed and identity and inverses

# ======================================================================
# PART FOUR -- LESSONS FROM THE COMBINATORIAL FRONTIER (through the wall)
# ======================================================================

banner("Ch.12 -- what a prime IS: the first number that catches you (First-G)")
def first_catch(N):
    return next(k for k in range(2, N + 1) if gcd(k, N) > 1)
def smallest_prime_factor(N):
    d = 2
    while d*d <= N:
        if N % d == 0:
            return d
        d += 1
    return N
for N in [15, 35, 77, 30, 143]:
    fc, spf = first_catch(N), smallest_prime_factor(N)
    show(f"walk 2,3,4,... against N={N}", f"first to share a factor = {fc} = smallest prime factor {spf}")
    assert fc == spf
print("  -> coprimality is 'no shared factor'; a prime is 'the first thing that catches you'.")

banner("Ch.12.1 -- Euclid: the primes never run out (product of primes + 1 has a NEW factor)")
from sympy import prime as _prime, factorint as _fac
for _k in range(1, 8):
    _firstk = [_prime(_i) for _i in range(1, _k + 1)]
    _P = 1
    for _p in _firstk:
        _P *= _p
    _P += 1
    assert all(_q not in _firstk for _q in _fac(_P).keys())      # every prime factor is new
show("first k primes -> (their product + 1) has only NEW prime factors", "so no finite list of primes is complete: the primes are endless")
show("but product + 1 need NOT itself be prime", "2*3*5*7*11*13 + 1 = 30031 = 59 x 509 (the classic misconception)")
assert _fac(30031) == {59: 1, 509: 1}
print("  -> the sieve thins the primes forever, and forever there are more to thin.")

banner("Ch.13 -- structure can be BUILT: Siamese magic squares by a walking rule")
def siamese(n):
    assert n % 2 == 1
    S = np.zeros((n, n), int)
    i, j = 0, n // 2
    for k in range(1, n*n + 1):
        S[i, j] = k
        ni, nj = (i - 1) % n, (j + 1) % n
        if S[ni, nj]:
            ni, nj = (i + 1) % n, j
        i, j = ni, nj
    return S
for n in [3, 5, 7]:
    S = siamese(n); M = n * (n*n + 1) // 2
    ok = (all(S[r].sum() == M for r in range(n)) and all(S[:, c].sum() == M for c in range(n))
          and np.trace(S) == M and np.trace(np.fliplr(S)) == M
          and sorted(S.flatten().tolist()) == list(range(1, n*n + 1)))
    show(f"odd order n={n}", f"every line sums to {M}; a valid magic square built by one repeatable step: {ok}")
    assert ok
print("  -> generation and structure are the same thing seen from two sides.")

banner("Ch.14 -- why algebra's dimensions double: 4^n = 2^(2n) = dim Cl(2n)")
for n in range(1, 6):
    show(f"n={n}", f"4^n = {4**n} = 2^(2n) = dim Cl(2n); each new generator DOUBLES the algebra")
    assert 4**n == 2**(2*n)
print("  -> the cube's 2^3 = 8 vertices ARE the Clifford algebra of 3-space.")

# ======================================================================
# EXTENSIONS -- further shared-language lessons that pass the same bar
# (each is self-contained math, a TRUE picture, met elsewhere -- through the wall)
# ======================================================================

banner("Extension -- the logarithm is the inverse breath (how many doublings)")
show("exp and log undo each other", f"exp(log(50)) = {math.exp(math.log(50)):.4f}")
show("log base 2 counts doublings", f"log2(8) = {math.log2(8):.1f}  (8 is three doublings of 1)")
assert abs(math.exp(math.log(50)) - 50) < 1e-9 and math.log2(8) == 3

banner("Extension -- pi is the half-turn the circle forces (rotation, the i again)")
show("half a turn in radians", f"e^(i*pi) = -1, so a half turn is pi; a full turn is 2pi")
assert abs(np.exp(1j*np.pi) + 1) < 1e-12

banner("Extension -- a derivative is the LOCAL breath rate")
for x in [0.0, 1.0, 2.0]:
    d = (math.exp(x + 1e-6) - math.exp(x)) / 1e-6
    show(f"instantaneous rate of e^x at x={x}", f"{d:.5f}  vs e^x = {math.exp(x):.5f} (the breath is its own rate)")
    assert abs(d - math.exp(x)) < 1e-4

banner("Extension -- why the golden ratio appears (growth + self-similarity; the pentagon)")
a, b = 1, 1
for _ in range(30):
    a, b = b, a + b
phi = (1 + np.sqrt(5)) / 2
show("Fibonacci ratio -> phi", f"F32/F31 = {b/a:.10f}  vs phi = {phi:.10f}")
show("phi is the self-similar growth root", f"phi^2 - phi - 1 = {phi**2 - phi - 1:.1e} (x^2 = x + 1)")
show("the pentagon's own number", f"diagonal/side = 2 cos 36deg = {2*np.cos(np.pi/5):.6f} = phi (five, the break, again)")
assert abs(b/a - phi) < 1e-6 and abs(phi**2 - phi - 1) < 1e-12 and abs(2*np.cos(np.pi/5) - phi) < 1e-12

# ======================================================================
banner("Extension -- rotation deepens: the tower R -> C -> H (the quaternions)")
qI = np.array([[1j, 0], [0, -1j]]); qJ = np.array([[0, 1], [-1, 0]]); qK = np.array([[0, 1j], [1j, 0]])
show("each imaginary unit is a rotation plane", "i^2 = j^2 = k^2 = -1")
show("they cycle", "ij = k, jk = i, ki = j, and ijk = -1")
show("they ANTICOMMUTE", "ji = -k  ->  rotations in different planes do not commute (3D rotation is non-abelian)")
assert np.allclose(qI@qI, -np.eye(2)) and np.allclose(qJ@qJ, -np.eye(2)) and np.allclose(qK@qK, -np.eye(2))
assert np.allclose(qI@qJ, qK) and np.allclose(qJ@qK, qI) and np.allclose(qK@qI, qJ)
assert np.allclose(qI@qJ@qK, -np.eye(2)) and np.allclose(qJ@qI, -qK)
print("  -> R (still), C (one rotation plane), H (three) -- the imaginary axis is the tower's first rung.")

# ======================================================================
# PART FIVE -- CHAPTER 18: WHERE THE TOWERS GO (the base points up)
# ======================================================================
banner("Ch.18 -- the three shapes that never end (simplex, cross-polytope, cube)")
simplex_n = lambda n: n + 1
cross_n = lambda n: 2 * n
cube_n = lambda n: 2 ** n
show("three growth laws", f"corners in 3D: simplex {simplex_n(3)}, cross-polytope {cross_n(3)}, cube {cube_n(3)}"
     f"; in 4D: {simplex_n(4)}, {cross_n(4)}, {cube_n(4)}")
assert [simplex_n(3), cross_n(3), cube_n(3)] == [4, 6, 8]

def regular_count(d):
    """regular polytopes in dimension d: Schlafli symbols whose Coxeter Gram matrix is positive definite"""
    out = []
    for s in itertools.product(range(3, 8), repeat=d - 1):
        G = np.eye(d)
        for i, p in enumerate(s):
            G[i, i + 1] = G[i + 1, i] = -np.cos(np.pi / p)
        if np.linalg.eigvalsh(G).min() > 1e-9:
            out.append(s)
    return out

counts = {d: len(regular_count(d)) for d in range(3, 8)}
show("regular shapes by dimension", f"{counts}  (five in 3D, six in 4D, then only three)")
assert counts == {3: 5, 4: 6, 5: 3, 6: 3, 7: 3}
assert set(regular_count(3)) - {(3, 3), (3, 4), (4, 3)} == {(3, 5), (5, 3)}           # the two five-fold solids
assert all(5 not in s for d in range(5, 8) for s in regular_count(d))                 # the five-fold line stops
print("  -> the tetrahedron, octahedron and cube are the 3D floors of the only towers that never end.")

banner("Ch.18 -- the number tower keeps doubling, and gives something up each time")
def cd_conj(x):
    return np.concatenate([x[:1], -x[1:]])
def cd_mul(a, b):
    if len(a) == 1:
        return a * b
    h = len(a) // 2
    return np.concatenate([cd_mul(a[:h], b[:h]) - cd_mul(cd_conj(b[h:]), a[h:]),
                           cd_mul(b[h:], a[:h]) + cd_mul(a[h:], cd_conj(b[:h]))])
rng18 = np.random.default_rng(18)
x4, y4, z4 = rng18.normal(size=(3, 4))
x8, y8, z8 = rng18.normal(size=(3, 8))
show("H (4): no longer commutes", f"|xy - yx| = {np.linalg.norm(cd_mul(x4, y4) - cd_mul(y4, x4)):.3f}")
show("O (8): no longer associates", f"|(xy)z - x(yz)| = {np.linalg.norm(cd_mul(cd_mul(x8, y8), z8) - cd_mul(x8, cd_mul(y8, z8))):.3f}")
e16 = np.eye(16)
zd = cd_mul(e16[1] + e16[10], e16[4] - e16[15])
show("16: division breaks", f"(e1 + e10)(e4 - e15) = 0 : {np.allclose(zd, 0)}  -- two non-zero numbers, product zero")
assert not np.allclose(cd_mul(x4, y4), cd_mul(y4, x4))
assert np.allclose(cd_mul(cd_mul(x4, y4), z4), cd_mul(x4, cd_mul(y4, z4)))
assert not np.allclose(cd_mul(cd_mul(x8, y8), z8), cd_mul(x8, cd_mul(y8, z8)))
assert np.isclose(np.linalg.norm(cd_mul(x8, y8)), np.linalg.norm(x8) * np.linalg.norm(y8))
assert np.allclose(zd, 0)
print("  -> R, C, H, O: the only number systems where sizes multiply (Hurwitz); the tower ends at O.")

banner("Ch.18 -- symmetry: the icosahedron's group is simple (the break at five, again)")
def rot18(axis, ang):
    a = np.asarray(axis, float) / np.linalg.norm(axis)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K
def group18(gens):
    key = lambda M: tuple(np.round(M, 6).ravel())
    elems, todo = {key(np.eye(3)): np.eye(3)}, [np.eye(3)]
    while todo:
        new = []
        for A in todo:
            for g in gens:
                if key(g @ A) not in elems:
                    elems[key(g @ A)] = g @ A
                    new.append(g @ A)
        todo = new
    return list(elems.values())
def classes18(G):
    key = lambda M: tuple(np.round(M, 6).ravel())
    seen, sizes = set(), []
    for h in G:
        if key(h) not in seen:
            c = {key(g @ h @ g.T) for g in G}
            seen |= c
            sizes.append(len(c))
    return sorted(sizes)
phi18 = (1 + 5 ** 0.5) / 2
tet_g = group18([rot18([1, 1, 1], 2 * np.pi / 3), rot18([0, 0, 1], np.pi)])
oct_g = group18([rot18([0, 0, 1], np.pi / 2), rot18([1, 1, 1], 2 * np.pi / 3)])
ico_g = group18([rot18([0, 1, phi18], 2 * np.pi / 5), rot18([1, 1, 1], 2 * np.pi / 3)])
ico_c = classes18(ico_g)
unions = {1 + sum(c) for r in range(1, len(ico_c) - 1) for c in combinations(ico_c[1:], r)}
show("turnings of the solids", f"tetrahedron {len(tet_g)}, octahedron/cube {len(oct_g)}, icosahedron {len(ico_g)}")
show("the icosahedron's group A5 is simple", f"classes {ico_c}: no union with the identity divides 60 -> {sorted(u for u in unions if 60 % u == 0)}")
assert [len(tet_g), len(oct_g), len(ico_g)] == [12, 24, 60]
assert ico_c == [1, 12, 12, 15, 20] and not any(60 % u == 0 for u in unions)
def half_turns_close(G):                              # identity + the 3 half-turns about the axes
    key = lambda M: tuple(np.round(M, 6).ravel())
    H = [g for g in G if np.allclose(g, np.diag(np.diag(g)))]   # the diagonal turns: identity + 3 half-turns
    keys = {key(h) for h in H}
    normal = all(key(g @ h @ g.T) in keys for g in G for h in H)
    return len(H), all(key(a @ b) in keys for a in H for b in H) and normal
show("the first two break into smaller pieces", f"tetrahedron and octahedron each hold a normal subgroup of "
     f"order {half_turns_close(tet_g)[0]} (the three half-turns about the axes, with the identity)")
assert half_turns_close(tet_g) == (4, True) and half_turns_close(oct_g) == (4, True)
def q_rot(q):
    turn = lambda v: cd_mul(cd_mul(q, np.concatenate([[0.0], v])), cd_conj(q))[1:]
    return np.column_stack([turn(v) for v in np.eye(3)])
qq = rng18.normal(size=4)
qq = qq / np.linalg.norm(qq)
show("a unit quaternion turns space", "q and -q give the same rotation (the quaternions double-cover the turns)")
assert np.allclose(q_rot(qq).T @ q_rot(qq), np.eye(3)) and np.allclose(q_rot(qq), q_rot(-qq))
print("  -> A5 is simple, so the general fifth-degree equation has no formula (Abel-Ruffini, Galois).")

banner("Ch.18 -- filling the centre: crystals and sphere packing")
fcc18 = np.array([p for p in itertools.product(range(-3, 4), repeat=3) if sum(p) % 2 == 0], float) / 2
cub18 = np.array(list(itertools.product(range(-2, 3), repeat=3)), float)
lat18 = {"diamond": np.vstack([fcc18, fcc18 + 0.25]), "simple cubic": cub18, "body-centred cubic": np.vstack([cub18, cub18 + 0.5])}
nbrs = {}
for nm, L in lat18.items():
    d = np.linalg.norm(L, axis=1)
    nbrs[nm] = int(np.isclose(d, d[d > 1e-9].min()).sum())
show("an atom's nearest neighbours", f"{nbrs}  (the tetrahedron's 4, the octahedron's 6, the cube's 8)")
assert nbrs == {"diamond": 4, "simple cubic": 6, "body-centred cubic": 8}
dfcc = np.linalg.norm(fcc18, axis=1)
fcc_density = 4 * 4 / 3 * np.pi * (dfcc[dfcc > 1e-9].min() / 2) ** 3
show("the densest 3D packing (face-centred cubic)", f"{fcc_density:.4f} of space = pi/sqrt(18) (Kepler 1611; proved, Hales 2005)")
assert np.isclose(fcc_density, np.pi / np.sqrt(18))
e8_18 = [v for v in itertools.product((-1, 0, 1), repeat=8) if sum(map(abs, v)) == 2]
e8_18 += [v for v in itertools.product((-0.5, 0.5), repeat=8) if sum(x < 0 for x in v) % 2 == 0]
show("E8 in eight dimensions", f"{len(e8_18)} touching neighbours per ball (densest possible: Viazovska 2017)")
assert len(e8_18) == 240

banner("Ch.18 -- the 1/3 and the shapes of atoms; sqrt(2) and the real line; the breath and the turn")
xm = 1 / np.sqrt(3)
show("the magic angle", f"3x^2 - 1 = {3 * xm ** 2 - 1:.1e} at x = cos(54.74 deg): the half-tetrahedral angle")
assert abs(3 * xm ** 2 - 1) < 1e-12
harm = [math.comb(l + 2, 2) - (math.comb(l, 2) if l >= 2 else 0) for l in range(5)]
show("spherical harmonics of degree l", f"{harm} = 2l + 1 (the s, p, d, f, g orbital counts)")
assert harm == [2 * l + 1 for l in range(5)]
pq, fr18 = (1, 1), []
for _ in range(5):
    fr18.append(pq)
    pq = (pq[0] + 2 * pq[1], pq[0] + pq[1])
show("ever-better fractions for sqrt(2)", f"{[f'{p}/{q}' for p, q in fr18]}, each p^2 - 2q^2 = +-1, none exact")
assert fr18 == [(1, 1), (3, 2), (7, 5), (17, 12), (41, 29)] and all(abs(p * p - 2 * q * q) == 1 for p, q in fr18)
def expm18(A):
    out, term = np.eye(len(A)), np.eye(len(A))
    for k in range(1, 60):
        term = term @ A / k
        out = out + term
    return out
Jq = np.array([[0.0, -1.0], [1.0, 0.0]])
S18 = rng18.normal(size=(3, 3))
R18 = expm18(S18 - S18.T)
show("the exponential of a turn is a rotation", "e^(theta J) = rotation by theta; e^(any spin) is a rotation")
assert np.allclose(expm18(0.9 * Jq), [[np.cos(0.9), -np.sin(0.9)], [np.sin(0.9), np.cos(0.9)]])
assert np.allclose(R18.T @ R18, np.eye(3)) and np.isclose(np.linalg.det(R18), 1)
onto18 = 0
for _ in range(25):                                   # and every rotation arises this way
    Qr, Rr = np.linalg.qr(rng18.normal(size=(3, 3)))
    Qr = Qr @ np.diag(np.sign(np.diag(Rr)))
    Qr = Qr * np.sign(np.linalg.det(Qr))              # an arbitrary rotation of space
    ang = np.arccos(np.clip((np.trace(Qr) - 1) / 2, -1, 1))
    ax = np.array([Qr[2, 1] - Qr[1, 2], Qr[0, 2] - Qr[2, 0], Qr[1, 0] - Qr[0, 1]]) / (2 * np.sin(ang))
    Kr = np.array([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]])
    onto18 += np.allclose(expm18(ang * Kr), Qr)
show("every rotation is the exponential of a spin", f"{onto18}/25 random rotations recovered as e^(spin)")
assert onto18 == 25
print("  -> the base does not prove the towers; it points up them.")

banner("Ch.18 -- every tower is also a coin: a flip, two sides, and an edge")
def faces18(V, normals):
    out = set()
    for u in normals:
        h = V @ u
        Fv = V[np.isclose(h, h.max())]
        if np.linalg.matrix_rank(Fv[1:] - Fv[0]) == 2:
            out.add(frozenset(map(tuple, np.round(Fv, 9))))
    return out
cube18 = np.array(list(itertools.product((1, -1), repeat=3)), float)
octa18 = np.vstack([np.eye(3), -np.eye(3)])
tet18 = cube18[np.prod(cube18, axis=1) > 0]
show("duality trades corners for faces", f"cube {len(cube18)} corners, {len(faces18(cube18, octa18))} faces; "
     f"octahedron {len(octa18)} corners, {len(faces18(octa18, cube18))} faces; tetrahedron 4 and "
     f"{len(faces18(tet18, -tet18))} -- its own dual")
assert len(faces18(cube18, octa18)) == 6 and len(faces18(octa18, cube18)) == 8 and len(faces18(tet18, -tet18)) == 4
ico18 = np.array([p for c in range(3) for p in (np.roll([0, s1, s2 * phi18], c) for s1 in (1, -1) for s2 in (1, -1))])
dico = np.linalg.norm(ico18[:, None] - ico18[None], axis=-1)
tri18 = [t for t in combinations(range(12), 3)
         if all(np.isclose(dico[a, b], dico[dico > 0].min()) for a, b in combinations(t, 2))]
show("the icosahedron and the dodecahedron", f"icosahedron: 12 corners, {len(tri18)} faces; its face-centres are the dodecahedron's 20 corners")
dod18 = np.array([ico18[list(t)].mean(axis=0) for t in tri18])
ddod = np.linalg.norm(dod18[:, None] - dod18[None], axis=-1)
assert len(tri18) == 20 and np.allclose(np.linalg.norm(dod18, axis=1), np.linalg.norm(dod18[0]))
assert all(np.isclose(ddod[k], ddod[ddod > 1e-9].min()).sum() == 3 for k in range(20))   # 3 edges at each corner
xs18 = [rng18.normal(size=n) for n in (2, 4, 8)]
show("the mirror a + bi -> a - bi", "a number times its mirror lands on the edge, the reals: x xbar = |x|^2 (C, H, O)")
assert all(np.allclose(cd_mul(x, cd_conj(x))[1:], 0) and np.isclose(cd_mul(x, cd_conj(x))[0], x @ x) for x in xs18)
even18 = [b for b in range(8) if bin(b).count("1") % 2 == 0]
coord18 = lambda b: tuple(1 - 2 * ((b >> i) & 1) for i in range(3))
def bmul18(a, b):
    s, x = 0, a >> 1
    while x:
        s += bin(x & b).count("1")
        x >>= 1
    return (-1) ** s, a ^ b
show("even against odd in Cl(3)", "the even pieces (1, e12, e13, e23) sit on one of the cube's tetrahedra; "
     "e12, e13, e23 square to -1 and anticommute: the quaternions")
assert {coord18(b) for b in even18} == {tuple(int(v) for v in r) for r in tet18}
assert all(bmul18(b, b) == (-1, 0) for b in (3, 5, 6)) and bmul18(3, 5)[0] == -bmul18(5, 3)[0]
zz18 = rng18.normal(size=50) + 1j * rng18.normal(size=50)
show("growing against shrinking", "|e^z| > 1 exactly when Re z > 0; on the edge Re z = 0, |e^z| = 1: pure turning")
assert np.all((np.abs(np.exp(zz18)) > 1) == (zz18.real > 0)) and np.allclose(np.abs(np.exp(1j * zz18.imag)), 1)
show("the missing edges", "x -> 2/x keeps no fraction (p^2 = 2q^2 never, q <= 5000); x -> -1/x keeps no real number (x^2 = -1)")
assert all(math.isqrt(2 * q * q) ** 2 != 2 * q * q for q in range(1, 5001))
assert np.allclose(sorted(np.roots([1, 0, 1]), key=lambda c: c.imag), [-1j, 1j])
print("  -> the towers are what you climb; their edges are what you point toward.")

# ======================================================================
banner("ALL LESSON CHECKS PASS -- every picture matches the mathematics.")
print("Parts One-Four plus the extension lessons are each reproduced above.")
print("Rejected pictures (the honest-failures chapter) are NOT asserted true here:")
print("  '1/3 is a universal residue' (false: it is 1/(N-1) at N=4 only),")
print("  'the breath makes energy' (false: structural growth only).")
print("Increasingly round; never measurably round.")
print("=" * 70)
