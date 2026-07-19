"""Finite-block sanity check for the arXiv:0905.0812 counterexample packet.

The proof is analytic. This script only prints the recurrence values used in
the packet and the constant lower bound for the selected block tails.
"""

from __future__ import annotations


def main(blocks: int = 12, c: float = 0.5) -> None:
    a = 1.0
    print(f"c = {c}")
    print("j  r_j  m_j=j^r_j  A_j recurrence value  block_tail_norm")
    for j in range(1, blocks + 1):
        r = j + 1
        m = j**r
        a = (a**r + c**r) ** (1.0 / r)
        print(f"{j:2d} {r:4d} {m:12d} {a:21.15f} {c:16.12f}")


if __name__ == "__main__":
    main()
