#!/usr/bin/env python3
"""
make_figures.py -- generates the load-bearing figures for
"The Shape of Understanding". Each figure is the picture of a lesson that
curriculum_checks.py / verify_forced_chain.py verifies, so the figures and
the proofs stay in lockstep.

    Run:  python make_figures.py
    Out:  figures/*.svg   (vector, embeddable in the manuscript)
"""
import os, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, ACC2, MUT = "#1a1a1a", "#c0392b", "#2471a3", "#7f8c8d"

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    print("  wrote figures/" + name)

# 1 -- the equidistance ladder: point, segment, triangle, tetrahedron
def fig_ladder():
    fig = plt.figure(figsize=(11, 3))
    ax = fig.add_subplot(1, 4, 1); ax.scatter([0], [0], s=90, c=INK); ax.set_title("1 · point", fontsize=10)
    ax = fig.add_subplot(1, 4, 2); ax.plot([0, 1], [0, 0], "-o", c=INK, mfc=INK); ax.set_title("2 · segment", fontsize=10)
    ax = fig.add_subplot(1, 4, 3)
    t = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2], [0, 0]])
    ax.plot(t[:, 0], t[:, 1], "-o", c=INK, mfc=INK); ax.set_title("3 · triangle (flat)", fontsize=10)
    ax = fig.add_subplot(1, 4, 4, projection="3d")
    v = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
    for i in range(4):
        for j in range(i+1, 4):
            ax.plot(*zip(v[i], v[j]), c=INK, lw=1)
    ax.scatter(v[:, 0], v[:, 1], v[:, 2], s=50, c=ACC)
    ax.set_title("4 · tetrahedron (lifts)", fontsize=10); ax.set_axis_off()
    for a in fig.axes[:3]:
        a.set_aspect("equal"); a.axis("off")
    fig.suptitle("The ladder of simultaneous equality — each dimension holds one more equal point",
                 fontsize=11, y=1.02)
    save(fig, "fig_simplex_ladder.svg")

# 2 -- square gives up equality (diagonal sqrt2); tetrahedron keeps it by lifting
def fig_equidistance():
    fig, (a, b) = plt.subplots(1, 2, figsize=(8, 4))
    s = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    a.plot(s[:, 0], s[:, 1], "-o", c=INK, mfc=INK)
    a.plot([0, 1], [0, 1], "--", c=ACC); a.plot([1, 0], [0, 1], "--", c=ACC)
    a.text(0.5, -0.12, "side = 1", ha="center", color=INK)
    a.text(0.52, 0.5, "diagonal = √2", ha="center", color=ACC, rotation=45)
    a.set_title("Square: 4 points that GAVE UP equality to stay flat", fontsize=9)
    a.set_aspect("equal"); a.axis("off")
    b = fig.add_subplot(1, 2, 2, projection="3d"); fig.axes[1].remove()
    v = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
    for i in range(4):
        for j in range(i+1, 4):
            b.plot(*zip(v[i], v[j]), c=ACC, lw=1.3)
    b.scatter(v[:, 0], v[:, 1], v[:, 2], s=50, c=INK)
    b.set_title("Tetrahedron: 4 points that KEEP equality by lifting\n(all 6 edges equal; cos θ = −1/3)", fontsize=9)
    b.set_axis_off()
    save(fig, "fig_equidistance_square_vs_tetra.svg")

# 3 -- the cube's two shadows: square (down a face) and hexagon (down the diagonal)
def fig_two_shadows():
    fig = plt.figure(figsize=(10, 3.6))
    axc = fig.add_subplot(1, 3, 2, projection="3d")
    r = [-1, 1]; import itertools
    V = np.array(list(itertools.product(r, r, r)), float)
    for i in range(8):
        for j in range(i+1, 8):
            if np.sum(np.abs(V[i]-V[j])) == 2:
                axc.plot(*zip(V[i], V[j]), c=INK, lw=1)
    axc.set_title("the cube", fontsize=10); axc.set_axis_off()
    a1 = fig.add_subplot(1, 3, 1)
    sq = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]])
    a1.plot(sq[:, 0], sq[:, 1], "-o", c=ACC2, mfc=ACC2)
    a1.set_title("shadow down a face:\na SQUARE (90°)", fontsize=9); a1.set_aspect("equal"); a1.axis("off")
    a3 = fig.add_subplot(1, 3, 3)
    ang = np.deg2rad(np.arange(0, 360, 60))
    hx = np.c_[np.cos(ang), np.sin(ang)]; hx = np.vstack([hx, hx[0]])
    a3.plot(hx[:, 0], hx[:, 1], "-o", c=ACC, mfc=ACC)
    for k in range(3):  # the 3 cube edges land 120 deg apart
        a3.plot([0, np.cos(ang[k*2])], [0, np.sin(ang[k*2])], c=MUT, lw=1)
    a3.set_title("shadow down the diagonal:\na HEXAGON (120°, cos²=1/3)", fontsize=9)
    a3.set_aspect("equal"); a3.axis("off")
    save(fig, "fig_cube_two_shadows.svg")

# 4 -- eigenvalue: a stretch has real axes; a rotation has none (complex = the i)
def fig_eigen():
    fig, (a, b) = plt.subplots(1, 2, figsize=(8, 4))
    th = np.linspace(0, 2*np.pi, 60); circ = np.c_[np.cos(th), np.sin(th)]
    S = np.diag([2.0, 1.0]); img = circ @ S.T
    a.plot(circ[:, 0], circ[:, 1], c=MUT, lw=1)
    a.plot(img[:, 0], img[:, 1], c=ACC2, lw=1.6)
    a.arrow(0, 0, 2, 0, color=ACC, width=0.03, length_includes_head=True)
    a.arrow(0, 0, 0, 1, color=ACC, width=0.03, length_includes_head=True)
    a.set_title("stretch diag(2,1): REAL eigenvalues\n= genuine stretch axes (red)", fontsize=9)
    a.set_aspect("equal"); a.axis("off")
    R = np.array([[np.cos(0.6), -np.sin(0.6)], [np.sin(0.6), np.cos(0.6)]]); img2 = circ @ R.T
    b.plot(circ[:, 0], circ[:, 1], c=MUT, lw=1)
    b.plot(img2[:, 0], img2[:, 1], c=ACC2, lw=1.6)
    for k in range(0, 60, 12):
        b.annotate("", xy=img2[k], xytext=circ[k], arrowprops=dict(arrowstyle="->", color=ACC, lw=1))
    b.set_title("rotation: COMPLEX eigenvalues e^{±iθ}\n= no fixed axis; the rotation IS the i", fontsize=9)
    b.set_aspect("equal"); b.axis("off")
    save(fig, "fig_eigen_axis_vs_rotation.svg")

# 5 -- Fourier: spinning circles add up to a square wave
def fig_fourier():
    fig, (a, b) = plt.subplots(1, 2, figsize=(9, 3.6))
    t = np.linspace(0, 2*np.pi, 1000)
    sq = np.sign(np.sin(t)); sq[sq == 0] = 1
    a.plot(t, sq, c=MUT, lw=1, label="target square wave")
    for K, col in [(1, "#f1c40f"), (3, ACC2), (7, ACC)]:
        ap = sum(4/(np.pi*k)*np.sin(k*t) for k in range(1, K+1, 2))
        a.plot(t, ap, c=col, lw=1.4, label=f"{ (K+1)//2 } circle(s)")
    a.set_title("more spinning circles → the wave", fontsize=10); a.legend(fontsize=7, loc="upper right")
    a.set_xticks([]); a.set_yticks([])
    # epicycle picture at one instant
    cx, cy, tt = 0, 0, 1.1; b.plot([], [])
    for k in range(1, 8, 2):
        rad = 4/(np.pi*k)
        ang = np.linspace(0, 2*np.pi, 100)
        b.plot(cx+rad*np.cos(ang), cy+rad*np.sin(ang), c=MUT, lw=0.7)
        nx, ny = cx+rad*np.cos(k*tt), cy+rad*np.sin(k*tt)
        b.plot([cx, nx], [cy, ny], c=ACC, lw=1.2); cx, cy = nx, ny
    b.plot(cx, cy, "o", c=ACC2)
    b.set_title("each frequency = one spinning circle\n(an i-rotation, a breath)", fontsize=9)
    b.set_aspect("equal"); b.axis("off")
    save(fig, "fig_fourier_epicycles.svg")

# 6 -- the void: the centre is nearest to ALL points at once
def fig_void():
    fig, ax = plt.subplots(figsize=(4.4, 4.4))
    ang = np.deg2rad([90, 210, 330]); P = np.c_[np.cos(ang), np.sin(ang)]
    tri = np.vstack([P, P[0]])
    ax.plot(tri[:, 0], tri[:, 1], "-o", c=INK, mfc=INK)
    for p in P:
        ax.plot([0, p[0]], [0, p[1]], "--", c=ACC, lw=1)
    ax.plot(0, 0, "o", c=ACC, ms=9)
    ax.text(0.06, 0.05, "0", color=ACC, fontsize=12, fontweight="bold")
    ax.set_title("The void is the FULLEST point\n(equally near to all at once, nowhere in particular)", fontsize=9)
    ax.set_aspect("equal"); ax.axis("off")
    save(fig, "fig_void_nearest.svg")

# 7 -- the pentagon's number: diagonal / side = phi
def fig_golden():
    fig, ax = plt.subplots(figsize=(4.6, 4.6))
    ang = np.deg2rad(90 + np.arange(5)*72); P = np.c_[np.cos(ang), np.sin(ang)]
    pent = np.vstack([P, P[0]])
    ax.plot(pent[:, 0], pent[:, 1], "-o", c=INK, mfc=INK, lw=1.6)
    ax.plot([P[0, 0], P[2, 0]], [P[0, 1], P[2, 1]], c=ACC, lw=2)   # a diagonal
    ax.plot([P[0, 0], P[1, 0]], [P[0, 1], P[1, 1]], c=ACC2, lw=2)  # a side
    ax.text(0, 0.15, "diagonal", color=ACC, ha="center", fontsize=9)
    ax.text(0.75, 0.75, "side", color=ACC2, fontsize=9)
    ax.set_title("Pentagon: diagonal / side = 2cos36° = φ = 1.618…\nthe break-at-five carries the golden ratio", fontsize=9)
    ax.set_aspect("equal"); ax.axis("off")
    save(fig, "fig_golden_pentagon.svg")

# 8 -- crystallographic restriction: which rotation orders can tile the plane
def fig_crystallographic():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ns = np.arange(1, 13)
    m = 2*np.cos(2*np.pi/ns)
    allowed = np.abs(m - np.round(m)) < 1e-9
    cols = [ACC2 if a else MUT for a in allowed]
    ax.bar(ns, m, color=cols)
    ax.axhline(0, color=INK, lw=0.6)
    for n, mv, a in zip(ns, m, allowed):
        ax.text(n, mv + (0.08 if mv >= 0 else -0.2), f"{n}", ha="center", fontsize=8,
                color=(INK if a else MUT), fontweight=("bold" if a else "normal"))
    ax.set_title("2·cos(2π/n): integer (blue) only for n = 1,2,3,4,6\n— five and ≥7 cannot tile; five is the break", fontsize=9)
    ax.set_xlabel("rotation order n"); ax.set_yticks([-2, -1, 0, 1, 2]); ax.set_xticks(ns)
    save(fig, "fig_crystallographic.svg")

if __name__ == "__main__":
    print("generating figures ->", OUT)
    for f in (fig_ladder, fig_equidistance, fig_two_shadows, fig_eigen,
              fig_fourier, fig_void, fig_golden, fig_crystallographic):
        try:
            f()
        except Exception as e:  # keep going; report which failed
            print(f"  [FAIL] {f.__name__}: {e}")
    print("done.")
