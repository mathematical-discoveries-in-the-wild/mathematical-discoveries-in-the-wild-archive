#include <array>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <set>

// Enumerate every proper canonical 4x4 coloring containing one of the nine
// normalized directed lunar-failure incidence types.  For each coordinate the
// two ordered off-diagonal edges are reverse (2 vertices), crossed in either
// orientation (3 vertices), or disjoint (4 vertices).  The deliberately
// redundant 4-by-4 list covers every failed generalized lunar implication
// without silently quotienting the relative orientation of two crossed types.

using Grid = std::array<int, 16>;

constexpr std::array<std::array<int, 4>, 4> TYPES{{
    {{0, 1, 1, 0}},  // reverse: (first,second), (second,first)
    {{0, 1, 2, 0}},  // crossed +: start(edge 1) = end(edge 2)
    {{0, 1, 1, 2}},  // crossed -: end(edge 1) = start(edge 2)
    {{0, 1, 2, 3}},  // disjoint
}};

std::uint64_t union_total = 0;
std::uint64_t canonical_total = 0;
std::uint64_t canonical_nonlunar = 0;
std::array<std::uint64_t, 17> canonical_by_colors{};
std::array<std::uint64_t, 17> canonical_nonlunar_by_colors{};
std::array<std::uint64_t, 17> union_by_colors{};
std::array<std::uint64_t, 16> type_totals{};
std::set<Grid> orbit_representatives;
bool legacy_nine_types = false;

std::array<std::array<int, 4>, 24> permutations() {
  std::array<std::array<int, 4>, 24> out{};
  std::array<int, 4> p{0, 1, 2, 3};
  int index = 0;
  do {
    out[index++] = p;
  } while (std::next_permutation(p.begin(), p.end()));
  return out;
}

const auto PERMS = permutations();

Grid canonical_relabel(const Grid &grid) {
  Grid out{};
  std::array<int, 16> relabel;
  relabel.fill(-1);
  int next = 0;
  for (int i = 0; i < 16; ++i) {
    const int old = grid[i];
    if (relabel[old] < 0) relabel[old] = next++;
    out[i] = relabel[old];
  }
  return out;
}

Grid orbit_key(const Grid &grid) {
  Grid best{};
  best.fill(99);
  for (const auto &rows : PERMS) {
    for (const auto &columns : PERMS) {
      for (int transpose = 0; transpose < 2; ++transpose) {
        Grid transformed{};
        for (int row = 0; row < 4; ++row) {
          for (int column = 0; column < 4; ++column) {
            const int source_row = transpose ? rows[column] : rows[row];
            const int source_column = transpose ? columns[row] : columns[column];
            transformed[4 * row + column] =
                grid[4 * source_row + source_column];
          }
        }
        transformed = canonical_relabel(transformed);
        if (transformed < best) best = transformed;
      }
    }
  }
  return best;
}

bool has_failure(const Grid &grid, int row_type, int column_type) {
  const auto &r = TYPES[row_type];  // a,b,c,d
  const auto &q = TYPES[column_type];  // x,y,z,w
  const auto at = [&](int row, int column) { return grid[4 * row + column]; };
  return at(r[0], q[0]) == at(r[1], q[1]) &&
         at(r[2], q[0]) == at(r[3], q[1]) &&
         at(r[0], q[2]) == at(r[1], q[3]) &&
         at(r[2], q[2]) != at(r[3], q[3]);
}

bool is_lunar(const Grid &grid) {
  std::array<std::uint16_t, 16> solutions{};
  for (int a = 0; a < 4; ++a) {
    for (int b = 0; b < 4; ++b) {
      std::uint16_t mask = 0;
      for (int x = 0; x < 4; ++x) {
        for (int y = 0; y < 4; ++y) {
          if (grid[4 * a + x] == grid[4 * b + y]) {
            mask |= std::uint16_t(1) << (4 * x + y);
          }
        }
      }
      solutions[4 * a + b] = mask;
    }
  }
  for (int first = 0; first < 16; ++first) {
    for (int second = first + 1; second < 16; ++second) {
      if (solutions[first] != solutions[second] &&
          (solutions[first] & solutions[second])) return false;
    }
  }
  return true;
}

void visit(int position, int colors, Grid &grid,
           std::array<unsigned, 16> &rowmask,
           std::array<unsigned, 16> &columnmask) {
  if (position == 16) {
    ++canonical_total;
    ++canonical_by_colors[colors];
    if (!is_lunar(grid)) {
      ++canonical_nonlunar;
      ++canonical_nonlunar_by_colors[colors];
    }
    bool in_union = false;
    for (int row_type = 0; row_type < 4; ++row_type) {
      for (int column_type = 0; column_type < 4; ++column_type) {
        if (legacy_nine_types && (row_type == 2 || column_type == 2)) continue;
        if (has_failure(grid, row_type, column_type)) {
          ++type_totals[4 * row_type + column_type];
          in_union = true;
        }
      }
    }
    if (in_union) {
      ++union_total;
      ++union_by_colors[colors];
      orbit_representatives.insert(orbit_key(grid));
    }
    return;
  }
  const int row = position / 4;
  const int column = position % 4;
  for (int color = 0; color <= colors; ++color) {
    if (color < colors && ((rowmask[color] >> row) & 1u)) continue;
    if (color < colors && ((columnmask[color] >> column) & 1u)) continue;
    grid[position] = color;
    const int next_colors = colors + (color == colors);
    rowmask[color] |= 1u << row;
    columnmask[color] |= 1u << column;
    visit(position + 1, next_colors, grid, rowmask, columnmask);
    rowmask[color] &= ~(1u << row);
    columnmask[color] &= ~(1u << column);
  }
}

int main() {
  legacy_nine_types = std::getenv("LEGACY_NINE_TYPES") != nullptr;
  Grid grid{};
  std::array<unsigned, 16> rowmask{};
  std::array<unsigned, 16> columnmask{};
  visit(0, 0, grid, rowmask, columnmask);
  std::cout << "canonical proper colorings " << canonical_total << "\n";
  std::cout << "canonical nonlunar colorings " << canonical_nonlunar << "\n";
  for (int colors = 4; colors <= 16; ++colors) {
    if (canonical_by_colors[colors]) {
      std::cout << colors << " colors canonical " << canonical_by_colors[colors]
                << " nonlunar " << canonical_nonlunar_by_colors[colors] << "\n";
    }
  }
  std::cout << "normalized-failure union colorings " << union_total << "\n";
  std::cout << "all nonlunar symmetry orbits " << orbit_representatives.size() << "\n";
  for (int row_type = 0; row_type < 4; ++row_type) {
    for (int column_type = 0; column_type < 4; ++column_type) {
      std::cout << "type " << row_type << " " << column_type << " colorings "
                << type_totals[4 * row_type + column_type] << "\n";
    }
  }
  for (int colors = 4; colors <= 16; ++colors) {
    if (union_by_colors[colors]) {
      std::cout << colors << " colors " << union_by_colors[colors] << "\n";
    }
  }
  std::array<std::uint64_t, 17> orbit_by_colors{};
  for (const Grid &representative : orbit_representatives) {
    const int colors =
        *std::max_element(representative.begin(), representative.end()) + 1;
    ++orbit_by_colors[colors];
  }
  for (int colors = 4; colors <= 16; ++colors) {
    if (orbit_by_colors[colors]) {
      std::cout << colors << " colors orbits " << orbit_by_colors[colors] << "\n";
    }
  }
  int index = 0;
  for (const Grid &representative : orbit_representatives) {
    const int colors =
        *std::max_element(representative.begin(), representative.end()) + 1;
    std::cout << "\nrepresentative " << index++ << " colors " << colors << "\n";
    for (int row = 0; row < 4; ++row) {
      for (int column = 0; column < 4; ++column) {
        std::cout << representative[4 * row + column]
                  << (column == 3 ? '\n' : ' ');
      }
    }
  }
}
