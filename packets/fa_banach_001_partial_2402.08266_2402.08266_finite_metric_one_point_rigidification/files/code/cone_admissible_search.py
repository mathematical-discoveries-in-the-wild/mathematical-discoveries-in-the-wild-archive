"""Finite search for non-spatial admissible symmetries of one-point cones.

This is scratch evidence for the arXiv:2402.08266 Question 3 full-push.
It enumerates small graph-metric spaces M, adds one point p with
    d(p,x) = sqrt(d(o,x)^2 + c^2),
computes preserved-extreme pairs by strict no-betweenness, and searches for
directed edge bijections satisfying the source paper's cycle and ratio axioms.
For candidates passing those cheap tests, it checks the wA3 norm identities
using the finite Kantorovich dual linear program.
"""

from __future__ import annotations

import itertools
import math
from collections import defaultdict

try:
    from scipy.optimize import linprog
except Exception as exc:  # pragma: no cover - scratch script
    raise SystemExit(f"scipy is required for this scratch search: {exc}")


def floyd_warshall(n, edges):
    d = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0.0
    for i, j, w in edges:
        d[i][j] = d[j][i] = min(d[i][j], w)
    for k in range(n):
        for i in range(n):
            dik = d[i][k]
            for j in range(n):
                nd = dik + d[k][j]
                if nd < d[i][j]:
                    d[i][j] = nd
    return d


def cone_metric(base_d, c=1.0, base=0):
    n = len(base_d)
    p = n
    d = [[0.0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            d[i][j] = base_d[i][j]
    for i in range(n):
        r = math.sqrt(base_d[base][i] ** 2 + c * c)
        d[p][i] = d[i][p] = r
    return d, p


def preserved_edges(d, tol=1e-9):
    n = len(d)
    undirected = []
    for i in range(n):
        for j in range(i + 1, n):
            ok = True
            for k in range(n):
                if k in (i, j):
                    continue
                if abs(d[i][k] + d[k][j] - d[i][j]) <= tol:
                    ok = False
                    break
            if ok:
                undirected.append((i, j))
    directed = []
    for i, j in undirected:
        directed.append((i, j))
        directed.append((j, i))
    return undirected, directed


def simple_cycles_undirected(vertices, edges):
    adj = defaultdict(set)
    edge_set = {tuple(sorted(e)) for e in edges}
    for a, b in edge_set:
        adj[a].add(b)
        adj[b].add(a)
    cycles = set()
    for start in vertices:
        stack = [(start, [start])]
        while stack:
            v, path = stack.pop()
            for w in adj[v]:
                if w == start and len(path) >= 3:
                    cyc = path[:]
                    # canonicalize by vertex cycle rotations and reversal
                    rots = []
                    for seq in (cyc, list(reversed(cyc))):
                        for k in range(len(seq)):
                            rots.append(tuple(seq[k:] + seq[:k]))
                    cverts = min(rots)
                    cedges = []
                    for i in range(len(cverts)):
                        cedges.append(tuple(sorted((cverts[i], cverts[(i + 1) % len(cverts)]))))
                    cycles.add(tuple(sorted(cedges)))
                elif w not in path and w >= start:
                    stack.append((w, path + [w]))
    return {frozenset(c) for c in cycles}


def is_spatial_on_undirected(edges, perm, n_vertices):
    edge_list = list(edges)
    target = {edge_list[i]: edge_list[perm[i]] for i in range(len(edge_list))}
    for f_tuple in itertools.permutations(range(n_vertices)):
        ok = True
        for a, b in edge_list:
            if tuple(sorted((f_tuple[a], f_tuple[b]))) != target[(a, b)]:
                ok = False
                break
        if ok:
            return True, f_tuple
    return False, None


def free_norm(d, coeffs):
    """Dual LP: max sum coeff_i phi_i subject |phi_i-phi_j| <= d_ij."""
    n = len(d)
    c = [-x for x in coeffs]
    a_ub = []
    b_ub = []
    for i in range(n):
        for j in range(i + 1, n):
            row = [0.0] * n
            row[i] = 1.0
            row[j] = -1.0
            a_ub.append(row)
            b_ub.append(d[i][j])
            row = [0.0] * n
            row[i] = -1.0
            row[j] = 1.0
            a_ub.append(row)
            b_ub.append(d[i][j])
    # Fix one potential to remove the translation lineality.
    bounds = [(None, None)] * n
    bounds[-1] = (0.0, 0.0)
    res = linprog(c, A_ub=a_ub, b_ub=b_ub, bounds=bounds, method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    return -res.fun


def directed_paths(edges, n_vertices, max_len=None):
    adj = defaultdict(list)
    for idx, (a, b) in enumerate(edges):
        adj[a].append((b, idx))
    paths = []
    if max_len is None:
        max_len = n_vertices - 1
    for s in range(n_vertices):
        stack = [(s, [], {s})]
        while stack:
            v, path, seen = stack.pop()
            if path:
                paths.append((s, v, tuple(path)))
            if len(path) >= max_len:
                continue
            for w, idx in adj[v]:
                if w in seen:
                    continue
                stack.append((w, path + [idx], seen | {w}))
    return paths


def check_wA3(d, directed, dir_perm, tol=1e-7):
    n = len(d)
    paths = directed_paths(directed, n, max_len=n - 1)
    for s, t, path in paths:
        coeffs = [0.0] * n
        for idx in path:
            a, b = directed[dir_perm[idx]]
            length = d[directed[idx][0]][directed[idx][1]]
            target_length = d[a][b]
            coeffs[a] += length / target_length
            coeffs[b] -= length / target_length
        val = free_norm(d, coeffs)
        if abs(val - d[s][t]) > tol:
            return False
    inv = [0] * len(dir_perm)
    for i, j in enumerate(dir_perm):
        inv[j] = i
    for s, t, path in paths:
        coeffs = [0.0] * n
        for idx in path:
            a, b = directed[inv[idx]]
            length = d[directed[idx][0]][directed[idx][1]]
            target_length = d[a][b]
            coeffs[a] += length / target_length
            coeffs[b] -= length / target_length
        val = free_norm(d, coeffs)
        if abs(val - d[s][t]) > tol:
            return False
    return True


def search_case(name, base_edges, n, max_perms=500000):
    base = floyd_warshall(n, [(a, b, 1.0) for a, b in base_edges])
    d, p = cone_metric(base)
    undirected, directed = preserved_edges(d)
    cycles = simple_cycles_undirected(range(n + 1), undirected)
    edge_list = list(undirected)
    cycle_images = {frozenset(edge_list.index(e) for e in cyc) for cyc in cycles}
    length = [d[a][b] for a, b in edge_list]

    print(f"\n== {name} ==")
    print("vertices", n + 1, "p", p)
    print("undirected E", edge_list)
    print("lengths", [round(x, 6) for x in length])
    print("cycles", [sorted(c) for c in cycle_images])

    nonspatial_cycle = 0
    nonspatial_wA3 = 0
    checked = 0
    for perm in itertools.permutations(range(len(edge_list))):
        checked += 1
        if checked > max_perms:
            print("stopped at max perms", max_perms)
            break
        image_cycles = {frozenset(perm[i] for i in cyc) for cyc in cycle_images}
        if image_cycles != cycle_images:
            continue
        ratio_ok = True
        for cyc in cycle_images:
            ratios = [length[i] / length[perm[i]] for i in cyc]
            if max(ratios) - min(ratios) > 1e-8:
                ratio_ok = False
                break
        if not ratio_ok:
            continue
        spatial, f = is_spatial_on_undirected(edge_list, perm, n + 1)
        if not spatial:
            nonspatial_cycle += 1
            print("nonspatial wA1/wA2 perm", perm)
        # Lift to the orientation-preserving directed map for this quick pass.
        dir_index = {e: i for i, e in enumerate(directed)}
        dir_perm = []
        for a, b in directed:
            c, dd = edge_list[perm[edge_list.index(tuple(sorted((a, b))))]]
            if (a, b) == tuple(sorted((a, b))):
                dir_perm.append(dir_index[(c, dd)])
            else:
                dir_perm.append(dir_index[(dd, c)])
        if check_wA3(d, directed, dir_perm):
            if not spatial:
                nonspatial_wA3 += 1
                print("nonspatial wA3 perm", perm)
            else:
                print("spatial candidate", perm, f)
    print("checked", checked, "nonspatial wA1/wA2", nonspatial_cycle, "nonspatial wA3", nonspatial_wA3)


def main():
    search_case("path3", [(0, 1), (1, 2)], 3)
    search_case("path4", [(0, 1), (1, 2), (2, 3)], 4)
    search_case("star4", [(0, 1), (0, 2), (0, 3)], 4)
    search_case("cycle4", [(0, 1), (1, 2), (2, 3), (3, 0)], 4)


if __name__ == "__main__":
    main()
