#!/usr/bin/env python3
"""
ch13_boxes_checks.py -- the checks for the two draft boxes of Chapter 13 (ch13_boxes.md):
13.1 "Lo Shu in four colours" and 13.2 "The odometer ties a knot".

    Run:  python ch13_boxes_checks.py

Written in the style of curriculum_checks.py, and meant to move into it if the boxes go into the
book. Every "(verified)" in the boxes has an assertion here. Dependencies: numpy.
"""
import itertools
import numpy as np
from collections import Counter

def show(name, detail):
    print(f"  [CHECK] {name}\n          {detail}")

def banner(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)

def dihedral(G):
    out, B = [], tuple(map(tuple, G))
    for _ in range(4):
        B = tuple(zip(*B[::-1])); out += [B, tuple(zip(*B))]
    return out

def lines3(G):
    return ([list(r) for r in G] + [[G[i][j] for i in range(3)] for j in range(3)]
            + [[G[i][i] for i in range(3)], [G[i][2 - i] for i in range(3)]])

def latin(M, symbols):
    return all(sorted(r) == symbols for r in M) and all(sorted(c) == symbols for c in zip(*M))

# ======================================================================
banner("13.1 -- Lo Shu in four colours")
lo = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
L0 = [[v - 1 for v in r] for r in lo]
hi3 = [[v // 3 for v in r] for r in L0]; lo3 = [[v % 3 for v in r] for r in L0]
show("Lo Shu minus 1, in base three", f"first digits {hi3}, second digits {lo3}")
assert latin(hi3, [0, 1, 2]) and latin(lo3, [0, 1, 2])
assert len({(hi3[i][j], lo3[i][j]) for i in range(3) for j in range(3)}) == 9
show("two orthogonal Latin squares", "each digit once per row and column in each place; every pair of digits once")
assert all(sum(l) == 12 for l in lines3(L0))
for name, cells in (("main diagonal", [(0, 0), (1, 1), (2, 2)]), ("anti-diagonal", [(0, 2), (1, 1), (2, 0)])):
    places = [[hi3[i][j] for i, j in cells], [lo3[i][j] for i, j in cells]]
    assert [1, 1, 1] in places and sorted(places[1 - places.index([1, 1, 1])]) == [0, 1, 2]
show("the diagonals", "on each one, one digit place holds the middle digit 1 three times; 1+1+1 = 0+1+2")

G = [[11, 13, 6], [5, 10, 15], [14, 7, 9]]
assert all(sum(l) == 30 for l in lines3(G)) and len({v for r in G for v in r}) == 9
hi4 = [[v // 4 for v in r] for r in G]; lo4 = [[v % 4 for v in r] for r in G]
assert latin(hi4, [1, 2, 3]) and latin(lo4, [1, 2, 3])
assert len({(hi4[i][j], lo4[i][j]) for i in range(3) for j in range(3)}) == 9
show("11 13 6 / 5 10 15 / 14 7 9", "magic with sum 30; its base-four digits are two orthogonal Latin squares on {1,2,3}")
assert 1 ^ 2 == 3 and 1 ^ 3 == 2 and 2 ^ 3 == 1
rc = [list(r) for r in G] + [[G[i][j] for i in range(3)] for j in range(3)]
assert all(l[0] ^ l[1] ^ l[2] == 0 for l in rc)
show("XOR", "any two of 01, 10, 11 XOR to the third; every row and column of the square XORs to 0")

# every 3x3 magic square with sum 30 and distinct entries from 0..15 (the centre is forced to be 10)
squares3 = set()
for a, b in itertools.permutations([v for v in range(16) if v != 10], 2):
    c = 30 - a - b; g, h, i_ = 20 - c, 20 - b, 20 - a
    d = 30 - a - g; f = 20 - d
    S = [[a, b, c], [d, 10, f], [g, h, i_]]
    vals = [v for r in S for v in r]
    if all(0 <= v <= 15 for v in vals) and len(set(vals)) == 9 and all(sum(l) == 30 for l in lines3(S)):
        squares3.add(min(dihedral(S)))
xor0 = [S for S in squares3 if all(l[0] ^ l[1] ^ l[2] == 0
        for l in [list(r) for r in S] + [[S[i][j] for i in range(3)] for j in range(3)])]
show(f"all {len(squares3)} magic 3x3 squares with sum 30 (entries 0-15)",
     f"exactly {len(xor0)} has rows and columns that all XOR to 0, and it is this one")
assert len(xor0) == 1 and xor0[0] == min(dihedral(G))

I2 = np.eye(2); X = np.array([[0, 1], [1, 0]]); Z = np.diag([1, -1]); Y = np.array([[0, -1j], [1j, 0]])
P = {0: I2, 1: Z, 2: X, 3: Y}
ops = [[np.kron(P[v // 4], P[v % 4]) for v in r] for r in G]
names = [" ".join("IZXY"[v // 4] + "IZXY"[v % 4] for v in r) for r in G]
show("the four colours 0 = I, 1 = Z, 2 = X, 3 = Y", " / ".join(names))
assert names == ["XY YZ ZX", "ZZ XX YY", "YX ZY XZ"]
signs = []
for line in [[(i, 0), (i, 1), (i, 2)] for i in range(3)] + [[(0, j), (1, j), (2, j)] for j in range(3)]:
    M = [ops[i][j] for i, j in line]
    assert all(np.allclose(A @ B, B @ A) for A in M for B in M)          # can be measured together
    prod = M[0] @ M[1] @ M[2]
    s = int(round(prod[0, 0].real)); assert np.allclose(prod, s * np.eye(4)); signs.append(s)
show("rows and columns", f"each is three measurements that can be made together; products {signs[:3]} (rows), {signs[3:]} (columns)")
assert signs == [-1, -1, -1, 1, 1, 1]
ok_any = False
for vals in itertools.product((1, -1), repeat=9):
    V = [vals[0:3], vals[3:6], vals[6:9]]
    rows_ok = all(np.prod(V[i]) == signs[i] for i in range(3))
    cols_ok = all(np.prod([V[i][j] for i in range(3)]) == signs[3 + j] for j in range(3))
    ok_any |= rows_ok and cols_ok
show("no list of nine answers fixed in advance works", "all 512 lists of +-1 tried: none gives -1 on every row and +1 on every column")
assert not ok_any

# ======================================================================
banner("13.2 -- the odometer ties a knot")
assert 0b0111 + 1 == 0b1000 and all(((7 >> k) & 1) != ((8 >> k) & 1) for k in range(4))
show("the full ripple", "0111 + 1 = 1000: every wheel turns at once")

subs = [frozenset(c) for c in itertools.combinations(range(16), 4) if sum(c) == 30]
parts = []
def rec(rem, chosen):
    if not rem:
        parts.append(tuple(chosen)); return
    m = min(rem)
    for s in subs:
        if m in s and s <= rem:
            rec(rem - s, chosen + [s])
rec(frozenset(range(16)), [])
sq = set()
for R in parts:
    for C in parts:
        if all(len(r & c) == 1 for r in R for c in C):
            cell = [[next(iter(r & c)) for c in C] for r in R]
            for rp in itertools.permutations(range(4)):
                for cp in itertools.permutations(range(4)):
                    A = tuple(tuple(cell[rp[i]][cp[j]] for j in range(4)) for i in range(4))
                    if sum(A[i][i] for i in range(4)) == 30 and sum(A[i][3 - i] for i in range(4)) == 30:
                        sq.add(min(dihedral(A)))
assert len(sq) == 880
show("the 4x4 magic squares on 0-15", f"{len(sq)} up to rotation and reflection (Frenicle 1693; Fitting 1931 proved there are no more)")
durer = tuple(tuple(v - 1 for v in r) for r in [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]])
assert min(dihedral(durer)) in sq

def counts(vals):
    return [sum((v >> k) & 1 for v in vals) for k in range(4)]
assert all(counts(A[i]) == [2] * 4 and counts([A[r][i] for r in range(4)]) == [2] * 4 for A in sq for i in range(4))
show("the layers (Fitting 1931)", "in all 880, each of the four layers has exactly two 1s in every row and every column")

def carries(vals):
    e = [c - 2 for c in counts(vals)]
    t2 = -e[3]; t1 = 2 * t2 - e[2]; t0 = 2 * t1 - e[1]
    assert e[0] == 2 * t0                    # a line summing to 30 always splits into carries
    return (t0, t1, t2)
tally, sign_ok, chain_ok, once_ok, whole = Counter(), True, True, True, []
for A in sq:
    t = carries([A[i][i] for i in range(4)]); u = carries([A[i][3 - i] for i in range(4)])
    assert all(x == -y for x, y in zip(t, u))                     # the other diagonal carries the opposite
    used = [k for k in range(3) if t[k]]
    once_ok &= all(abs(x) <= 1 for x in t)
    chain_ok &= used == list(range(used[0], used[0] + len(used))) if used else True
    sign_ok &= all(t[k] == t[k + 1] for k in range(2) if t[k] and t[k + 1])
    tally[len(used)] += 1
    if len(used) == 3:
        whole.append(A)
show("the carry rules", "no carry used twice; the carries form an unbroken chain; neighbouring carries share a sign")
assert once_ok and chain_ok and sign_ok
sums = sorted({sum(v + b0 + 4 * b2 for v in (0, 2, 8, 10)) for b0 in (0, 1) for b2 in (0, 1)})
show("1s-to-2s with 4s-to-8s, alone", f"freezes the 1s and 4s digits, so the line is one of four sets summing to {sums}: never 30")
assert sums == [20, 24, 36, 40]
show("squares by number of carries", f"{[tally[n] for n in range(4)]} (Fitting's count)")
assert [tally[n] for n in range(4)] == [528, 192, 112, 48]

assert all(all(c != 2 for c in counts([A[i][i] for i in range(4)])) for A in whole)
sig = {tuple(sorted([tuple(counts([A[i][i] for i in range(4)])), tuple(counts([A[i][3 - i] for i in range(4)]))])) for A in whole}
assert sig == {((0, 1, 1, 3), (4, 3, 3, 1))}
show("the 48", "no layer balanced on the diagonals; one diagonal holds (0,1,1,3) ones per layer: short 1+1+2+4 = 8, paid by one extra 8")

# the trefoil: Kauffman bracket over all eight ways of setting its three crossings
PD = [(1, 5, 2, 4), (3, 1, 4, 6), (5, 3, 6, 2)]               # the standard trefoil diagram
def bracket(flips):
    total = Counter()
    for state in itertools.product((0, 1), repeat=3):          # 0 = A-smoothing, 1 = B-smoothing
        parent = {e: e for e in range(1, 7)}
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for (a, b, c, d), s, f in zip(PD, state, flips):
            pairs = [(a, b), (c, d)] if s ^ f == 0 else [(a, d), (b, c)]   # a switched crossing swaps them
            for x, y in pairs:
                parent[find(x)] = find(y)
        loops = len({find(e) for e in range(1, 7)})
        term = Counter({3 - 2 * sum(state): 1})                # A^(#A - #B)
        for _ in range(loops - 1):                             # times d = -A^2 - A^-2 per extra loop
            new = Counter()
            for e, cf in term.items():
                new[e + 2] -= cf; new[e - 2] -= cf
            term = new
        total.update(term)
    return {e: c for e, c in total.items() if c}
knotted = [f for f in itertools.product((0, 1), repeat=3) if len(bracket(f)) > 1]   # unknot: a single term
show("the trefoil picture", f"of 8 ways to set three crossings, {len(knotted)} are knotted: {knotted} (all three agree)")
assert knotted == [(0, 0, 0), (1, 1, 1)]
assert all(len(set(carries([A[i][i] for i in range(4)]))) == 1 for A in whole)
show("exactly the 48 tie a trefoil", "they are the only squares using all three carries, and their three carries always agree")
print("  -> the knot is a drawing of the carry rule; the arithmetic underneath is Fitting's.")

banner("CHAPTER 13 BOX CHECKS PASS")
