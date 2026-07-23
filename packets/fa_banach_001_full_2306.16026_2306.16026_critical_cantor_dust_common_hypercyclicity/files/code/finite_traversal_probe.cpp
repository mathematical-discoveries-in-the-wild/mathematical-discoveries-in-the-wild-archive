#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <utility>

// Fast exploratory implementation of the adaptive Hilbert-prefix experiment
// in finite_traversal_probe.py.  This is numerical evidence, not a proof.

static std::pair<std::uint64_t, std::uint64_t> d2xy(
    std::uint64_t grid, std::uint64_t index) {
  std::uint64_t x = 0;
  std::uint64_t y = 0;
  std::uint64_t t = index;
  for (std::uint64_t scale = 1; scale < grid; scale <<= 1) {
    const std::uint64_t rx = 1 & (t / 2);
    const std::uint64_t ry = 1 & (t ^ rx);
    if (ry == 0) {
      if (rx == 1) {
        x = scale - 1 - x;
        y = scale - 1 - y;
      }
      std::swap(x, y);
    }
    x += scale * rx;
    y += scale * ry;
    t /= 4;
  }
  return {x, y};
}

static double cantor_left(std::uint64_t index, int depth) {
  double answer = 0.0;
  double place = 0.25;
  for (int bit = depth - 1; bit >= 0; --bit) {
    answer += 3.0 * static_cast<double>((index >> bit) & 1) * place;
    place *= 0.25;
  }
  return answer;
}

int main(int argc, char** argv) {
  const double tau = argc > 1 ? std::atof(argv[1]) : 0.1;
  const std::uint64_t max_pieces =
      argc > 2 ? std::strtoull(argv[2], nullptr, 10) : 100000000ULL;
  constexpr int virtual_depth = 30;
  constexpr std::uint64_t total_indices = 1ULL << (2 * virtual_depth);

  std::uint64_t index = 0;
  std::uint64_t count = 0;
  std::uint64_t previous_n = 0;
  int max_depth = 0;
  double previous_x = 0.0;
  double previous_y = 0.0;
  long double mass = 0.0L;
  std::uint64_t next_report = 1000000ULL;

  std::cout << "pieces mass order_fraction n max_depth\n";
  while (index < total_indices && count < max_pieces) {
    int depth = 1;
    double side = 0.25;
    while (side > tau / static_cast<double>(std::max(previous_n, 1ULL))) {
      ++depth;
      side *= 0.25;
    }

    std::uint64_t block = 1ULL << (2 * (virtual_depth - depth));
    while (index % block != 0) {
      ++depth;
      if (depth > virtual_depth) {
        throw std::runtime_error("virtual depth exhausted");
      }
      side *= 0.25;
      block >>= 2;
    }

    while (true) {
      const std::uint64_t prefix = index / block;
      const auto [x_prefix, y_prefix] = d2xy(1ULL << depth, prefix);
      const double tag_x = 1.0 + cantor_left(x_prefix, depth) + side;
      const double tag_y = 1.0 + cantor_left(y_prefix, depth) + side;

      std::uint64_t n = 1;
      if (count != 0) {
        n = previous_n + 1;
        n = std::max(
            n, static_cast<std::uint64_t>(
                   std::ceil((previous_n * previous_x + 1.0) / tag_x)));
        n = std::max(
            n, static_cast<std::uint64_t>(
                   std::ceil((previous_n * previous_y + 1.0) / tag_y)));
      }
      if (side <= tau / static_cast<double>(n)) {
        index += block;
        ++count;
        max_depth = std::max(max_depth, depth);
        mass += static_cast<long double>(side);
        previous_x = tag_x;
        previous_y = tag_y;
        previous_n = n;
        break;
      }

      ++depth;
      if (depth > virtual_depth) {
        throw std::runtime_error("virtual depth exhausted");
      }
      side *= 0.25;
      block >>= 2;
    }

    if (count == next_report) {
      std::cout << count << ' ' << std::setprecision(15)
                << static_cast<double>(mass) << ' '
                << static_cast<double>(index) /
                       static_cast<double>(total_indices)
                << ' ' << previous_n << ' ' << max_depth << '\n';
      next_report += 1000000ULL;
    }
  }

  std::cout << "FINAL " << count << ' ' << std::setprecision(15)
            << static_cast<double>(mass) << ' '
            << static_cast<double>(index) / static_cast<double>(total_indices)
            << ' ' << previous_n << ' ' << max_depth << ' '
            << (index == total_indices ? "complete" : "incomplete") << '\n';
}
