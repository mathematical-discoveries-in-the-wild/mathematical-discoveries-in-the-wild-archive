#!/usr/bin/env sh
set -eu

ROOT="$(cd "$(dirname "$0")/../../../../.." && pwd)"
PACKET="$ROOT/runs/fa_banach_001/solutions/full/1402.0528_ode_lp_norm_constant_two"

/opt/homebrew/bin/gs -dSAFER -dBATCH -dNOPAUSE \
  -sDEVICE=pngalpha -r160 -dFirstPage=11 -dLastPage=11 \
  -sOutputFile="$PACKET/figures/open_problem_crop.png" \
  "$PACKET/source_paper.pdf"
