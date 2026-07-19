from math import sqrt


def edge_count(parts):
    total = sum(parts)
    return (total * total - sum(p * p for p in parts)) // 2


def normalized_norm(parts):
    total = sum(parts)
    return 2 * sum(sqrt(p) for p in parts) / sqrt(total)


examples = {
    "G_parts_1_1_4_4": [1, 1, 4, 4],
    "H_parts_1_2_2_5": [1, 2, 2, 5],
}

for name, parts in examples.items():
    print(name)
    print("  vertices:", sum(parts))
    print("  clique_number:", len(parts))
    print("  edges:", edge_count(parts))
    print("  norm:", normalized_norm(parts))

g = normalized_norm(examples["G_parts_1_1_4_4"])
h = normalized_norm(examples["H_parts_1_2_2_5"])
print("norm_difference_H_minus_G:", h - g)
