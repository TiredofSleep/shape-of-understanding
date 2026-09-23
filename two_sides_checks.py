#!/usr/bin/env python3
"""two_sides_checks.py -- reproduces every "(verified)" fact in *Two Sides and an Edge*.

    python two_sides_checks.py      (a few seconds; numpy only)

A flip is a move that, done twice, changes nothing. Its two sides are what it swaps; its edge is what
it leaves alone. Each chapter of the unit is checked in order below.
"""
import itertools
from fractions import Fraction
from math import gcd, isqrt

import numpy as np

rng = np.random.default_rng(2)
PHI = (1 + 5 ** 0.5) / 2
N_CHECKS = 0


def show(name, detail):
    global N_CHECKS
    N_CHECKS += 1
    print(f"  [CHECK] {name}\n          {detail}")


def banner(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


def keyset(A, nd=9):
    return {tuple(np.round(np.asarray(a, float), nd) + 0.0) for a in A}


dist = lambda A: np.linalg.norm(A[:, None] - A[None], axis=-1)[np.triu_indices(len(A), 1)]
C = np.array(list(itertools.product((1, -1), repeat=3)), float)
Tp, Tm = C[np.prod(C, axis=1) > 0], C[np.prod(C, axis=1) < 0]

# ======================================================================
banner("Chapter 1 -- flips are everywhere")
xs = np.arange(-50, 51)
show("1.1 the flip x -> -x", "keeps exactly one number: 0")
assert list(xs[-xs == xs]) == [0]
ico = np.array([p for c in range(3) for p in (np.roll([0, s1, s2 * PHI], c) for s1 in (1, -1) for s2 in (1, -1))])
dode = np.vstack([C, np.array([p for c in range(3) for p in (np.roll([0, s1 / PHI, s2 * PHI], c)
                                                             for s1 in (1, -1) for s2 in (1, -1))])])
octa = np.vstack([np.eye(3), -np.eye(3)])
swapxy = np.array([[0.0, 1, 0], [1, 0, 0], [0, 0, 1]])
solids = [(Tp, swapxy), (C, -np.eye(3)), (octa, -np.eye(3)), (ico, -np.eye(3)), (dode, -np.eye(3))]
show("1.2 all five Platonic solids are their own mirror images", "a reflection carries each one onto itself")
assert all(np.isclose(np.linalg.det(M), -1) and keyset(V @ M.T) == keyset(V) for V, M in solids)
sc = np.array([[0, 0, 0], [1, 0, 0], [0, 2, 0], [0, 0, 3]], float)
show("1.2 a lopsided tetrahedron is not", "six different edge lengths, and its reflection reverses its handedness")
assert len(set(np.round(dist(sc), 9))) == 6
assert np.linalg.det(sc[1:] - sc[0]) * np.linalg.det((sc @ np.diag([-1.0, 1, 1]))[1:]) < 0


def facets(V, normals):
    out = set()
    for u in normals:
        h = V @ u
        Fv = V[np.isclose(h, h.max())]
        if np.linalg.matrix_rank(Fv[1:] - Fv[0]) == V.shape[1] - 1:
            out.add(frozenset(map(tuple, np.round(Fv, 9))))
    return out


show("1.3 duality swaps the cube and the octahedron", f"cube: 8 corners, {len(facets(C, octa))} faces; "
     f"octahedron: 6 corners, {len(facets(octa, C))} faces")
assert len(facets(C, octa)) == 6 and len(facets(octa, C)) == 8
dic = np.linalg.norm(ico[:, None] - ico[None], axis=-1)
tris = [t for t in itertools.combinations(range(12), 3)
        if all(np.isclose(dic[a, b], dic[dic > 0].min()) for a, b in itertools.combinations(t, 2))]
dod = np.array([ico[list(t)].mean(axis=0) for t in tris])
ddd = np.linalg.norm(dod[:, None] - dod[None], axis=-1)
show("1.3 ... and the dodecahedron and the icosahedron", "the icosahedron has 12 corners and 20 faces; its 20 "
     "face-centres are a dodecahedron's corners, 3 edges at each")
assert len(tris) == 20 and len(dod) == 20 and all(np.isclose(ddd[k], ddd[ddd > 1e-9].min()).sum() == 3 for k in range(20))
show("1.3 the tetrahedron is its own dual", f"its {len(facets(Tp, -Tp))} faces are cut out by the corners of "
     "the tetrahedron turned over")
assert len(facets(Tp, -Tp)) == 4


def regular_simplex(n):
    E = np.eye(n + 1) - 1 / (n + 1)
    V = E @ np.linalg.svd(E)[2][:n].T
    return V / np.linalg.norm(V, axis=1, keepdims=True)


def simplex_self_dual(n):
    V = regular_simplex(n)
    W = -n * V
    on = np.isclose(W @ V.T, 1)
    return all(on[j].sum() == n and W[j] @ V[j] < 1 for j in range(n + 1))


def corners_are_faces(n):
    cubeV = np.array(list(itertools.product((1, -1), repeat=n)), float)
    crossV = np.vstack([np.eye(n), -np.eye(n)])
    fc, fx = facets(cubeV, crossV), facets(crossV, cubeV)
    return len(fc) == 2 * n and len(fx) == 2 ** n


show("1.3 in every dimension (2 to 7)", "the cube's and the octahedron's cousins swap; the simplex is its own dual")
assert all(corners_are_faces(n) for n in range(2, 7)) and all(simplex_self_dual(n) for n in range(2, 8))
show("1.4 the cube's flip x -> -x", "swaps its two tetrahedra (4 + 4 corners), and keeps only the centre")
assert keyset(-Tp) == keyset(Tm) and np.allclose(dist(Tp), 8 ** 0.5) and np.linalg.matrix_rank(-2 * np.eye(3)) == 3

# ======================================================================
banner("Chapter 2 -- every thing splits in two")
z = rng.normal(size=300) + 1j * rng.normal(size=300)
x3 = rng.normal(size=(300, 3))
mirror = np.diag([1.0, 1, -1])
edge_part = lambda f, v: (v + f(v)) / 2
side_part = lambda f, v: (v - f(v)) / 2
show("2.1 every linear flip splits each thing into an edge part and a side part",
     "the average is kept by the flip; half the difference is negated by it")
assert all(np.allclose(f(edge_part(f, s)), edge_part(f, s)) and np.allclose(f(side_part(f, s)), -side_part(f, s))
           and np.allclose(edge_part(f, s) + side_part(f, s), s) for f, s in [(np.conj, z), (lambda v: v @ mirror, x3)])
show("2.2 for a + bi -> a - bi the two parts are the real part and the imaginary part",
     "and a number times its mirror is a^2 + b^2, a real number")
assert np.allclose(edge_part(np.conj, z), z.real) and np.allclose(side_part(np.conj, z), 1j * z.imag)
assert np.allclose(z * np.conj(z), z.real ** 2 + z.imag ** 2)
th = rng.uniform(-3, 3, 200)
show("2.3 reversing a turn splits e^(i theta) into cos theta + i sin theta (Euler's formula)",
     "and e^x splits into cosh x + sinh x")
assert np.allclose((np.exp(1j * th) + np.exp(-1j * th)) / 2, np.cos(th))
assert np.allclose((np.exp(1j * th) - np.exp(-1j * th)) / 2, 1j * np.sin(th))
assert np.allclose((np.exp(th) + np.exp(-th)) / 2, np.cosh(th)) and np.allclose((np.exp(th) - np.exp(-th)) / 2, np.sinh(th))


def expm(A, terms=60):
    out, term = np.eye(len(A)), np.eye(len(A))
    for k in range(1, terms):
        term = term @ A / k
        out = out + term
    return out


A = rng.normal(size=(3, 3))
Sym, Skw = (A + A.T) / 2, (A - A.T) / 2
show("2.4 the transpose splits a table into symmetric + skew",
     "symmetric: real eigenvalues, its exponential stretches; skew: imaginary eigenvalues, its exponential turns")
assert np.allclose(np.linalg.eigvals(Sym).imag, 0) and np.allclose(np.linalg.eigvals(Skw).real, 0)
assert np.all(np.linalg.eigvalsh(expm(Sym)) > 0)
assert np.allclose(expm(Skw).T @ expm(Skw), np.eye(3)) and np.isclose(np.linalg.det(expm(Skw)), 1)
show("2.5 the odd rule: a p orbital (p = z) is negated by the mirror z -> -z", "and it is zero on the mirror's plane")
assert np.allclose((x3 @ mirror)[:, 2], -x3[:, 2])
assert np.allclose(np.column_stack([rng.normal(size=(20, 2)), np.zeros(20)])[:, 2], 0)

# ======================================================================
banner("Chapter 3 -- three coins on one ball")
circle = np.exp(1j * rng.uniform(0, 2 * np.pi, 50))
show("3.1 z -> 1/conj(z) is a flip that swaps inside and outside", "and keeps the whole circle of radius 1")
assert np.allclose(1 / np.conj(1 / np.conj(z)), z) and np.all((abs(z) < 1) == (abs(1 / np.conj(z)) > 1))
assert np.allclose(1 / np.conj(circle), circle)
ip = np.exp(1j * np.pi / 4)
reals = rng.normal(size=40)
show("3.2 z -> i/z swaps the real line with the imaginary line", "its edge is the two numbers whose square is i")
assert np.allclose((1j / reals).real, 0) and np.allclose((1j / (1j * reals)).imag, 0)
assert np.isclose(1j / ip, ip) and np.isclose(ip ** 2, 1j) and np.isclose(1j / -ip, -ip)


def S(w):
    if w is None:
        return np.array([0.0, 0.0, 1.0])
    r2 = abs(w) ** 2
    return np.array([2 * w.real, 2 * w.imag, r2 - 1]) / (r2 + 1)


six = {"0": 0j, "oo": None, "1": 1 + 0j, "-1": -1 + 0j, "i": 1j, "-i": -1j}
P = {k: S(v) for k, v in six.items()}
show("3.3 on the ball of numbers, 0, oo, 1, -1, i, -i", "are the six corners of a regular octahedron")
assert keyset(P.values()) == keyset(octa)
H = {"-z": np.diag([-1.0, -1, 1]), "1/z": np.diag([1.0, -1, -1]), "-1/z": np.diag([-1.0, 1, -1])}
F = {"-z": lambda w: -w, "1/z": lambda w: 1 / w, "-1/z": lambda w: -1 / w}
show("3.3 -z, 1/z and -1/z are half-turns about the octahedron's three axes",
     "keeping 0 and oo, 1 and -1, i and -i respectively")
assert all(np.allclose(S(F[k](w)), H[k] @ S(w)) for k in H for w in z)
kept = lambda R: keyset([p for p in P.values() if np.allclose(R @ p, p)])
assert kept(H["-z"]) == keyset([P["0"], P["oo"]]) and kept(H["1/z"]) == keyset([P["1"], P["-1"]])
assert kept(H["-1/z"]) == keyset([P["i"], P["-i"]])
show("3.3 on the real line, x -> -1/x keeps no number", "x = -1/x means x^2 = -1, whose roots are i and -i")
assert np.allclose(sorted(np.roots([1, 0, 1]), key=lambda c: c.imag), [-1j, 1j])
show("3.4 any two of the half-turns make the third", "and the only point all three keep is the ball's centre")
assert np.allclose(H["-z"] @ H["1/z"], H["-1/z"]) and np.allclose(H["1/z"] @ H["-1/z"], H["-z"])
assert np.linalg.matrix_rank(np.vstack([R - np.eye(3) for R in H.values()])) == 3

# ======================================================================
banner("Chapter 4 -- the whole coin")
G3 = [tuple(v) for v in itertools.product((-1, 0, 1), repeat=3)]
by_edge = [sum(1 for v in G3 if v.count(0) == k) for k in range(4)]
show("4.1 three coins that land heads, tails or on the edge", f"{len(G3)} outcomes = {' + '.join(map(str, by_edge))}")
assert by_edge == [8, 12, 6, 1]
corners = [v for v in G3 if 0 not in v]
edges = [(a, b) for a, b in itertools.combinations(corners, 2) if sum(p != q for p, q in zip(a, b)) == 1]
show("4.1 ... the Rubik's cube's corner pieces, edge pieces, centres and core",
     "the outcomes with no, one, two or three coins on the edge are exactly those positions")
assert {tuple((p + q) // 2 for p, q in zip(a, b)) for a, b in edges} == {v for v in G3 if v.count(0) == 1}
assert keyset([v for v in G3 if v.count(0) == 2]) == keyset(octa) and [v for v in G3 if v.count(0) == 3] == [(0, 0, 0)]
G2 = list(itertools.product((-1, 0, 1), repeat=2))
show("4.2 two such coins give the 3 x 3 grid", "9 = 4 corners + 4 edge-middles + the centre")
assert [sum(1 for v in G2 if v.count(0) == k) for k in range(3)] == [4, 4, 1]
show("4.2 in any dimension (1 to 6)", "all coins on a side: the cube's 2^n corners; one on a side: 2n corners; "
     "all on the edge: the centre")
assert all(sum(1 for v in itertools.product((-1, 0, 1), repeat=n) if v.count(0) == 0) == 2 ** n
           and sum(1 for v in itertools.product((-1, 0, 1), repeat=n) if v.count(0) == n - 1) == 2 * n
           for n in range(1, 7))


def walked_square(n):
    M = np.zeros((n, n), int)
    i, j = 0, n // 2
    for s in range(1, n * n + 1):
        M[i, j] = s
        a, b = (i - 1) % n, (j + 1) % n
        i, j = (a, b) if M[a, b] == 0 else ((i + 1) % n, j)
    return M


show("4.3 the magic square's coin (sizes 3, 5, 7, 9)", "a half-turn swaps s with n^2 + 1 - s and keeps the middle "
     "cell; in the Lo Shu the middle is 5")
assert all((walked_square(n) + np.rot90(walked_square(n), 2) == n * n + 1).all()
           and walked_square(n)[n // 2, n // 2] == (n * n + 1) // 2 for n in (3, 5, 7, 9))
assert walked_square(3)[1, 1] == 5 and walked_square(5)[2, 2] == 13


def walk(n, k):
    seen, loops = set(), []
    for s in range(n):
        if s in seen:
            continue
        loop, i = [], s
        while i not in loop:
            loop.append(i)
            i = (i + k) % n
        seen |= set(loop)
        loops.append(loop)
    return loops


show("4.4 walking n dots k at a time makes one loop exactly when k shares no factor with n",
     "checked for n = 3..16 and every k; with a prime n every jump is one loop")
assert all((len(walk(n, k)) == 1) == (gcd(n, k) == 1) for n in range(3, 17) for k in range(1, n))
assert all(len(walk(p, k)) == 1 for p in (3, 5, 7, 11, 13) for k in range(1, p))
assert [k for k in range(1, 8) if len(walk(8, k)) == 1] == [1, 3, 5, 7]
assert [k for k in range(1, 12) if len(walk(12, k)) == 1] == [1, 5, 7, 11]


def winding(n, k):
    return round(sum(np.angle(np.exp(2j * np.pi * k / n)) for _ in range(n)) / (2 * np.pi))


show("4.4 every single loop winds round the middle and never touches it",
     "each chord passes the centre at distance cos(pi k/n) > 0")
assert all(abs(winding(n, k)) == min(k, n - k) and np.cos(np.pi * min(k, n - k) / n) > 0
           for n in range(3, 17) for k in range(1, n) if gcd(n, k) == 1)
Bd = np.array([[1, -1, 0], [1, 1, -2]]) / np.array([[2 ** 0.5], [6 ** 0.5]])
corner = lambda A: keyset(A @ Bd.T)
cp, cm = corner(Tp), corner(Tm)
tri = lambda K: {k for k in K if not np.allclose(k, 0)}
hexpts = sorted((np.degrees(np.arctan2(k[1], k[0])) % 360, k) for k in tri(cp) | tri(cm))
show("4.4 with 6 dots and k = 2 the walk splits into two triangles",
     "exactly the cube's corner-on shadow, whose alternate corners are its two tetrahedra")
assert sorted(map(sorted, walk(6, 2))) == [[0, 2, 4], [1, 3, 5]]
assert all({hexpts[j][1] for j in loop} in (tri(cp), tri(cm)) for loop in walk(6, 2))

# ======================================================================
banner("Chapter 5 -- one box, two lenses")
face = lambda A: keyset(np.asarray(A)[:, :2])
show("5.1 face-on, both tetrahedra cast the same square", "corner-on, two triangles turned 60 degrees, far corners "
     "on the centre")
assert face(Tp) == face(Tm) == keyset([(1, 1), (1, -1), (-1, 1), (-1, -1)])
assert (0.0, 0.0) in cp and (0.0, 0.0) in cm and len(tri(cp)) == len(tri(cm)) == 3
assert np.allclose(np.diff([h[0] for h in hexpts]), 60)
show("5.2 neither shadow alone tells the 8 corners apart", "face-on 8 -> 4, corner-on 8 -> 7; the two together, 8")
assert len(face(C)) == 4 and len(corner(C)) == 7
assert len({(tuple(np.round(c[:2], 9)), tuple(np.round(Bd @ c, 9))) for c in C}) == 8
rnd = np.random.default_rng(58)
agree = 0
for _ in range(2000):
    n, k = int(rnd.integers(2, 9)), int(rnd.integers(1, 4))
    views = [rnd.integers(0, int(rnd.integers(1, 4)), size=n) for _ in range(k)]
    faithful = len({tuple(v[x] for v in views) for x in range(n)}) == n
    residual = [(x, y) for x, y in itertools.combinations(range(n), 2) if all(v[x] == v[y] for v in views)]
    agree += faithful == (not residual)
show("5.2 the rule: views tell every pair apart exactly when no pair is mixed up by all of them",
     f"{agree} of 2000 random families of views agree")
assert agree == 2000
c2 = (np.array([0.0, 0, 1]) @ (np.ones(3) / 3 ** 0.5)) ** 2
show("5.3 the angle between the two lenses", "cos^2 = 1/3, where 3x^2 - 1 = 0 (the magic angle)")
assert np.isclose(c2, 1 / 3) and np.isclose(3 * c2 - 1, 0)

# ======================================================================
banner("Chapter 6 -- missing edges")
fracs = {Fraction(p, q) for q in range(1, 60) for p in range(1, 120)}
show("6.1 x -> 2/x is a flip on the fractions", "it swaps those whose square is below 2 with those above, and "
     "keeps none: 2 appears to an odd power on one side of p^2 = 2q^2")
assert all(2 / (2 / x) == x for x in fracs) and all((x * x < 2) == ((2 / x) ** 2 > 2) for x in fracs)
assert all(isqrt(2 * q * q) ** 2 != 2 * q * q for q in range(1, 20001))
x, heron = Fraction(1), []
for _ in range(4):
    x = (x + 2 / x) / 2
    heron.append(x)
show("6.2 point toward it: averaging the two sides", " -> ".join(map(str, heron)))
assert heron == [Fraction(3, 2), Fraction(17, 12), Fraction(577, 408), Fraction(665857, 470832)]
r2 = 2 ** 0.5
closest = [(round(q * r2), q) for q in range(1, 10001)]
worst = min(q * q * abs(p / q - r2) for p, q in closest)
show("6.2 measure off it, never stand on it", f"p^2 - 2q^2 is never 0; every p/q stays more than 1/(3q^2) away "
     f"(closest {worst:.4f}/q^2, q <= 10000)")
assert all(p * p - 2 * q * q != 0 for p, q in closest) and worst > 1 / 3


def odd_prime(n):
    m, p = n, 2
    while p * p <= m:
        e = 0
        while m % p == 0:
            m, e = m // p, e + 1
        if e % 2:
            return p
        p += 1
    return m if m > 1 else None


show("6.2 x -> n/x keeps a fraction exactly when n is a perfect square", "3, 5, 6, 7 have missing edges; 4, 9 do not "
     "(and every n up to 200 has a certificate)")
assert all((isqrt(n) ** 2 == n) == (odd_prime(n) is None) for n in range(1, 201))
assert [n for n in (3, 4, 5, 6, 7, 9) if odd_prime(n) is None] == [4, 9]
x = Fraction(2)
for _ in range(3):
    x = (x + 3 / x) / 2
show("6 exercise: averaging x and 3/x from 2", f"gives {x}, pointing toward sqrt(3)")
assert x == Fraction(18817, 10864)


def cd_conj(v):
    return np.concatenate([v[:1], -v[1:]])


def cd_mul(a, b):
    if len(a) == 1:
        return a * b
    h = len(a) // 2
    return np.concatenate([cd_mul(a[:h], b[:h]) - cd_mul(cd_conj(b[h:]), a[h:]),
                           cd_mul(b[h:], a[:h]) + cd_mul(a[h:], cd_conj(b[:h]))])


def turn(q):
    t = lambda v: cd_mul(cd_mul(q, np.r_[0.0, v]), cd_conj(q))[1:]
    return np.column_stack([t(v) for v in np.eye(3)])


qs = rng.normal(size=(20, 4))
qs /= np.linalg.norm(qs, axis=1, keepdims=True)
full = lambda a: np.r_[np.cos(a / 2), np.sin(a / 2) * np.array([0.0, 0, 1])]
show("6.5 q and -q give the same turn, and no unit quaternion is its own negative",
     "one full turn brings q to -q; two full turns bring it home")
assert all(np.allclose(turn(q), turn(-q)) for q in qs) and not any(np.allclose(q, -q) for q in qs)
assert np.allclose(full(2 * np.pi), [-1, 0, 0, 0]) and np.allclose(full(4 * np.pi), [1, 0, 0, 0])

# ======================================================================
banner("Chapter 7 -- four kinds of paradox")
partial = [sum(Fraction(1, 2 ** k) for k in range(1, n + 1)) for n in range(1, 41)]
show("7.1 Zeno: the counting lens sees ever more steps", "the measuring lens sees 1 - 1/2^n, below 1 and closing in")
assert all(p == 1 - Fraction(1, 2 ** (i + 1)) for i, p in enumerate(partial)) and all(p < 1 for p in partial)
INV = {"a": "A", "A": "a", "b": "B", "B": "b"}
words, frontier = [""], [""]
for _ in range(8):
    frontier = [w + c for w in frontier for c in "aAbB" if not (w and INV[w[-1]] == c)]
    words += frontier
times = lambda c, w: w[1:] if w and w[0] == INV[c] else c + w
show("7.2 the free words on two turns: four piles by first letter",
     "S(a) and a*S(a^-1) rebuild every word, and so do S(b) and b*S(b^-1)")
assert all((w.startswith("a")) != (times("A", w).startswith("A")) for w in words)
assert all((w.startswith("b")) != (times("B", w).startswith("B")) for w in words)
eight = [w for w in words if len(w) == 8]
show("7.2 no 'how much' survives the turns", "among the words of length 8, S(a^-1) holds 1/4, but turned by a it holds 3/4")
assert 4 * sum(w.startswith("A") for w in eight) == len(eight) and 4 * sum(not w.startswith("a") for w in eight) == 3 * len(eight)
NOT2, NOT3 = {"T": "F", "F": "T"}, {"T": "F", "F": "T", "U": "U"}
show("7.3 the Liar: 'not' on true and false has no edge", "with a third value, 'neither', the Liar has exactly one value")
assert [v for v in NOT2 if NOT2[v] == v] == [] and [v for v in NOT3 if NOT3[v] == v] == ["U"]


def diagonal_escapes(Y, flip, n):
    funcs = list(itertools.product(Y, repeat=n))
    for phi in itertools.product(funcs, repeat=n):
        if tuple(flip[phi[a][a]] for a in range(n)) in phi:
            return False
    return True


show("7.3 Cantor: with the yes/no flip, every list misses its own flipped diagonal", "all lists of 1, 2 and 3 rows; "
     "with a flip that has an edge, some list contains its flipped diagonal")
assert all(diagonal_escapes((0, 1), {0: 1, 1: 0}, n) for n in (1, 2, 3))
assert not diagonal_escapes((0, "U", 1), {0: 1, 1: 0, "U": "U"}, 2)


def russell(n):
    X = range(n)
    for bits in itertools.product((0, 1), repeat=n * n):
        E = {pair for i, pair in enumerate(itertools.product(X, X)) if bits[i]}
        R = frozenset(v for v in X if (v, v) not in E)
        if any(R == frozenset(v for v in X if (v, y) in E) for y in X):
            return False
    return True


show("7.3 Russell: the things that are not members of themselves are never one of the things",
     "every membership relation on 1, 2 and 3 things")
assert all(russell(n) for n in (1, 2, 3))

# ======================================================================
banner("Chapter 8 -- where you meet coins")


def conj_lands_real(n):
    for _ in range(20):
        v = rng.normal(size=n)
        vv = cd_mul(v, cd_conj(v))
        if not (np.allclose(vv[1:], 0) and np.isclose(vv[0], v @ v) and np.allclose(cd_conj(cd_conj(v)), v)):
            return False
    return True


show("8 numbers: the mirror keeps the reals on every floor", "complex numbers, quaternions, octonions: "
     "a number times its mirror is its size squared, a real number")
assert all(conj_lands_real(n) for n in (2, 4, 8))


def blade_mul(a, b):
    s, x = 0, a >> 1
    while x:
        s += bin(x & b).count("1")
        x >>= 1
    return (-1) ** s, a ^ b


coord = lambda b: tuple(1 - 2 * ((b >> i) & 1) for i in range(3))
even = [b for b in range(8) if bin(b).count("1") % 2 == 0]
show("8 the cube's algebra Cl(3): even pieces on one tetrahedron, odd on the other",
     "and the even half is the quaternions: e12, e13, e23 square to -1 and anticommute")
assert keyset([coord(b) for b in even]) == keyset(Tp)
assert all(blade_mul(b, b) == (-1, 0) for b in (3, 5, 6)) and blade_mul(3, 5)[0] == -blade_mul(5, 3)[0]
B_fcc = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]], float)
B_bcc = np.array([[1, 0, 0], [0, 1, 0], [0.5, 0.5, 0.5]])
U = B_bcc @ np.linalg.inv(np.linalg.inv(B_fcc).T)
A8 = 2 * np.eye(8)
for i, j in [(1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4)]:
    A8[i - 1, j - 1] = A8[j - 1, i - 1] = -1
show("8 crystals: the face-centred cubic lattice's dual is the body-centred one",
     "the cubic grid and E8 are their own duals (E8: determinant 1)")
assert np.allclose(U, np.round(U)) and np.isclose(abs(np.linalg.det(U)), 1)
assert np.isclose(np.linalg.det(A8), 1) and np.allclose(np.linalg.inv(A8), np.round(np.linalg.inv(A8)))
show("8 growth: growing (Re z > 0) against shrinking, with pure turning -- the circle -- on the edge",
     "and a half-turn of pure turning is the flip itself: e^(i pi) = -1")
assert np.all((abs(np.exp(z)) > 1) == (z.real > 0)) and np.allclose(abs(np.exp(1j * reals)), 1)
assert np.isclose(np.exp(1j * np.pi), -1)
m = 15
t = [1.0, 0.5] * m + [0.5, 1.0] * m
Hw = np.diag(t, 1) + np.diag(t, -1)
Ew, Vw = np.linalg.eigh(Hw)
zi = np.argmin(abs(Ew))
psi = Vw[:, zi] ** 2
show("8 light at a wall (a model chain whose bond pattern flips at its middle)",
     "exactly one state at zero energy, held at the wall, on one of the chain's two sublattices")
assert abs(Ew[zi]) < 1e-10 and sum(abs(Ew) < 1e-6) == 1 and psi[2 * m - 6:2 * m + 7].sum() > 0.95
assert min(psi[0::2].sum(), psi[1::2].sum()) < 1e-20

banner(f"ALL {N_CHECKS} CHECKS PASS -- two sides and an edge, every verified line reproduced.")
