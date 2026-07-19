#!/usr/bin/env python3
"""Heuristic search for large finite-dimensional linear-KS ratios in S_1.

The signs and coordinate selections are enumerated exactly. Only the search
over the matrix array is heuristic.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
import torch


def sign_vectors(n: int, *, device: torch.device) -> torch.Tensor:
    return torch.tensor(
        list(itertools.product((-1.0, 1.0), repeat=n)),
        dtype=torch.float64,
        device=device,
    )


def selections(n: int, *, device: torch.device) -> torch.Tensor:
    return torch.tensor(
        list(itertools.product(range(n), repeat=n)),
        dtype=torch.long,
        device=device,
    )


def nuclear_norm(batch: torch.Tensor) -> torch.Tensor:
    return torch.linalg.svdvals(batch).sum(dim=-1)


def ks_terms(
    z: torch.Tensor, eps: torch.Tensor, choices: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor]:
    # z has shape (n, n, d, d).
    row_sums = torch.einsum("sk,jkxy->jsxy", eps, z)
    lhs = nuclear_norm(row_sums).mean()

    n = z.shape[0]
    row_index = torch.arange(n, device=z.device)[None, :]
    selected = z[row_index, choices]  # (n**n, n, d, d)
    transversal_sums = torch.einsum("sj,cjxy->csxy", eps, selected)
    rhs = nuclear_norm(transversal_sums).mean()
    return lhs, rhs


def run_search(
    n: int,
    dim: int,
    steps: int,
    restarts: int,
    learning_rate: float,
    seed: int,
    output: Path | None,
) -> dict[str, object]:
    device = torch.device("cpu")
    eps = sign_vectors(n, device=device)
    choices = selections(n, device=device)
    best_ratio = -math.inf
    best_array: np.ndarray | None = None
    traces: list[dict[str, float | int]] = []

    for restart in range(restarts):
        generator = torch.Generator(device=device)
        generator.manual_seed(seed + restart)
        z = torch.randn(
            (n, n, dim, dim),
            dtype=torch.float64,
            generator=generator,
            device=device,
        )
        z /= z.norm()
        z.requires_grad_(True)
        optimizer = torch.optim.Adam([z], lr=learning_rate)

        local_best = -math.inf
        for step in range(steps):
            optimizer.zero_grad(set_to_none=True)
            lhs, rhs = ks_terms(z, eps, choices)
            ratio = lhs / (rhs + 1e-12)
            (-torch.log(ratio + 1e-12)).backward()
            optimizer.step()
            with torch.no_grad():
                z /= z.norm() + 1e-15
                value = float(ratio)
                if value > local_best:
                    local_best = value
                if value > best_ratio:
                    best_ratio = value
                    best_array = z.detach().cpu().numpy().copy()

        traces.append({"restart": restart, "best_ratio": local_best})

    assert best_array is not None
    result: dict[str, object] = {
        "n": n,
        "matrix_dimension": dim,
        "steps": steps,
        "restarts": restarts,
        "learning_rate": learning_rate,
        "seed": seed,
        "best_ratio": best_ratio,
        "restart_traces": traces,
    }
    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        np.save(output.with_suffix(".npy"), best_array)
        output.with_suffix(".json").write_text(
            json.dumps(result, indent=2) + "\n", encoding="utf-8"
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--dim", type=int, required=True)
    parser.add_argument("--steps", type=int, default=500)
    parser.add_argument("--restarts", type=int, default=8)
    parser.add_argument("--learning-rate", type=float, default=0.03)
    parser.add_argument("--seed", type=int, default=150105213)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_search(
        n=args.n,
        dim=args.dim,
        steps=args.steps,
        restarts=args.restarts,
        learning_rate=args.learning_rate,
        seed=args.seed,
        output=args.output,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
