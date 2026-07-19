"""Search for non-spatial admissible symmetries of constant-radius cones.

This is scratch work for the 2402.08266 full one-point push.  It reuses the
finite LP check from the promoted finite packet, but replaces the generic
radial lengths by a common radius R > diam(M).
"""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
HELPER = ROOT / "solutions/partial/2402.08266_finite_metric_one_point_rigidification/code/cone_admissible_search.py"

spec = importlib.util.spec_from_file_location("cone_helper", HELPER)
helper = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(helper)


def constant_metric(base_d, radius):
    n = len(base_d)
    p = n
    d = [[0.0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            d[i][j] = base_d[i][j]
    for i in range(n):
        d[p][i] = d[i][p] = radius
    return d, p


def search_case(name, base_edges, n, radius):
    base = helper.floyd_warshall(n, [(a, b, 1.0) for a, b in base_edges])
    d, p = constant_metric(base, radius)
    undirected, directed = helper.preserved_edges(d)
    cycles = helper.simple_cycles_undirected(range(n + 1), undirected)
    edge_list = list(undirected)
    cycle_images = {frozenset(edge_list.index(e) for e in cyc) for cyc in cycles}
    length = [d[a][b] for a, b in edge_list]
    print(f"\n== {name}, R={radius} ==")
    print("E", edge_list)
    print("lengths", length)
    print("cycles", [sorted(c) for c in cycle_images])
    nonspatial_wA3 = 0
    import itertools

    for perm in itertools.permutations(range(len(edge_list))):
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
        spatial, f = helper.is_spatial_on_undirected(edge_list, perm, n + 1)
        dir_index = {e: i for i, e in enumerate(directed)}
        dir_perm = []
        for a, b in directed:
            c, dd = edge_list[perm[edge_list.index(tuple(sorted((a, b))))]]
            if (a, b) == tuple(sorted((a, b))):
                dir_perm.append(dir_index[(c, dd)])
            else:
                dir_perm.append(dir_index[(dd, c)])
        if helper.check_wA3(d, directed, dir_perm):
            print("wA3 candidate", "spatial" if spatial else "NONSPATIAL", perm, f)
            if not spatial:
                nonspatial_wA3 += 1
                break
    print("nonspatial_wA3", nonspatial_wA3)


def main():
    search_case("path3", [(0, 1), (1, 2)], 3, 3.0)
    search_case("path4", [(0, 1), (1, 2), (2, 3)], 4, 4.0)
    search_case("star4", [(0, 1), (0, 2), (0, 3)], 4, 3.0)
    search_case("cycle4", [(0, 1), (1, 2), (2, 3), (3, 0)], 4, 3.0)


if __name__ == "__main__":
    main()
