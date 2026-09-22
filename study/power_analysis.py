#!/usr/bin/env python3
"""power_analysis.py -- sample size per arm for the eigenvalue A/B test.

Two-sample (Welch ~ pooled at equal n) t-test, two-sided. Exact power via the
noncentral t distribution: for per-arm n and true standardized effect d, the
noncentrality is ncp = d * sqrt(n/2) on df = 2n - 2.

    python power_analysis.py
"""
import numpy as np
from scipy.stats import nct, t


def power_two_sample_t(n_per_arm, d, alpha=0.05):
    df = 2 * n_per_arm - 2
    ncp = d * np.sqrt(n_per_arm / 2.0)
    crit = t.ppf(1 - alpha / 2, df)
    # P(|T| > crit) under the noncentral alternative
    return (1 - nct.cdf(crit, df, ncp)) + nct.cdf(-crit, df, ncp)


def n_for_power(d, power=0.80, alpha=0.05, nmax=100000):
    for n in range(4, nmax):
        if power_two_sample_t(n, d, alpha) >= power:
            return n
    return None


if __name__ == "__main__":
    print("Sample size PER ARM, two-sided two-sample t-test, alpha = 0.05\n")
    print(f"  {'effect d':>9} | {'power 0.80':>11} | {'power 0.90':>11}")
    print("  " + "-" * 37)
    for d in (0.3, 0.4, 0.5, 0.6, 0.8):
        n80 = n_for_power(d, 0.80)
        n90 = n_for_power(d, 0.90)
        print(f"  {d:>9.1f} | {n80:>11} | {n90:>11}")
    d0 = 0.5
    n0 = n_for_power(d0, 0.80)
    print(f"\nPre-registered target: d = {d0} at 80% power  ->  n = {n0} per arm "
          f"({2*n0} total).")
    print(f"Check: power at n={n0} is {power_two_sample_t(n0, d0):.3f} (>= 0.80).")
