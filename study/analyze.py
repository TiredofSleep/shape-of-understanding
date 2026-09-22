#!/usr/bin/env python3
"""analyze.py -- the pre-registered analysis for the eigenvalue A/B test.

Runs today on simulated data so the pipeline is tested before real collection:

    python analyze.py --simulate            # end-to-end on a simulated cohort
    python analyze.py --data results.csv     # real data, same columns

results.csv columns: id, arm, immediate, retention, transfer, connection
  arm in {treatment, control}; immediate/retention 0-6; transfer 0-4; connection 0-2.

Reports each outcome as effect size (Cohen's d) with a 95% CI and a Welch
two-sided t-test. The PRIMARY outcome is transfer at two weeks; everything else
is secondary/exploratory. A null on the primary is a real result (see
PREREGISTRATION.md), not a failure.
"""
import argparse
import csv
import sys
import numpy as np
from scipy.stats import ttest_ind


def cohens_d(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    na, nb = len(a), len(b)
    sp = np.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2))
    if sp == 0:
        return 0.0, (0.0, 0.0)
    d = (a.mean() - b.mean()) / sp
    se = np.sqrt((na + nb) / (na * nb) + d**2 / (2 * (na + nb)))  # Hedges approx SE
    return d, (d - 1.96 * se, d + 1.96 * se)


def simulate(n_per_arm=64, seed=0):
    """A plausible cohort: treatment shifted on transfer/connection, noise elsewhere.
    True effects here are for pipeline-testing only, NOT a claim about reality."""
    rng = np.random.default_rng(seed)
    rows = []
    truth = {  # (control mean, treatment - control) on each outcome
        "immediate": (4.4, 0.2), "retention": (3.6, 0.4),
        "transfer": (1.8, 0.55), "connection": (0.7, 0.5),
    }
    caps = {"immediate": 6, "retention": 6, "transfer": 4, "connection": 2}
    for arm in ("treatment", "control"):
        for i in range(n_per_arm):
            row = {"id": f"{arm[:1]}{i:03d}", "arm": arm}
            for k, (base, delta) in truth.items():
                mu = base + (delta if arm == "treatment" else 0.0)
                val = rng.normal(mu, 1.1)
                row[k] = int(np.clip(round(val), 0, caps[k]))
            rows.append(row)
    return rows


def load_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for k in ("immediate", "retention", "transfer", "connection"):
            r[k] = float(r[k])
    return rows


def analyze(rows):
    t = [r for r in rows if r["arm"] == "treatment"]
    c = [r for r in rows if r["arm"] == "control"]
    print(f"n = {len(t)} treatment, {len(c)} control\n")
    order = [("transfer", "PRIMARY  "), ("immediate", "secondary"),
             ("retention", "secondary"), ("connection", "secondary")]
    print(f"  {'outcome':<11}{'role':<10}{'T mean':>8}{'C mean':>8}{'d':>7}"
          f"{'  95% CI':>16}{'  p':>9}")
    print("  " + "-" * 70)
    primary = None
    for key, role in order:
        tv = [r[key] for r in t]
        cv = [r[key] for r in c]
        d, (lo, hi) = cohens_d(tv, cv)
        stat, p = ttest_ind(tv, cv, equal_var=False)
        print(f"  {key:<11}{role:<10}{np.mean(tv):>8.2f}{np.mean(cv):>8.2f}"
              f"{d:>7.2f}   [{lo:>5.2f},{hi:>5.2f}]{p:>9.4f}")
        if key == "transfer":
            primary = (d, lo, hi, p)
    d, lo, hi, p = primary
    print("\n  PRE-REGISTERED DECISION (primary = transfer at two weeks):")
    if lo > 0 and lo >= 0.3:
        verdict = "supports the claim (d>0, CI excludes small effects)"
    elif hi <= 0:
        verdict = "REFUTES the claim (treatment not above control) -- publish the null"
    elif lo <= 0:
        verdict = "inconclusive (CI includes 0) -- report as null-ish, do not overclaim"
    else:
        verdict = "weak support (d>0 but CI dips below 0.3)"
    print(f"    d = {d:.2f}, 95% CI [{lo:.2f}, {hi:.2f}], p = {p:.4f}  ->  {verdict}")
    print("    (Effect size + interval is the result; the p-value alone is not.)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simulate", action="store_true", help="run on a simulated cohort")
    ap.add_argument("--data", help="path to results.csv")
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    if args.data:
        rows = load_csv(args.data)
    elif args.simulate:
        print("[simulated data -- pipeline test only, not a real result]\n")
        rows = simulate(seed=args.seed)
    else:
        ap.print_help()
        sys.exit(1)
    analyze(rows)


if __name__ == "__main__":
    main()
