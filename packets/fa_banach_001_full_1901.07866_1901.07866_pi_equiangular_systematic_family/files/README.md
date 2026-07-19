# Follow-up packet: spanning equiangular intervals for `Pi(n,d)`

Status: human-requested follow-up to the reviewed packet
`1901.07866_pi_7_3_equiangular_lines`.

Source paper: Giuliano Basso, *Computation of maximal projection constants*,
arXiv:1901.07866.

## Motivation

The human review accepted the previous observation

```text
Pi(7,15) = 7/3
```

as correct but low-novelty, and recommended looking for a systematic pattern
or infinite family using the Koenig--Lewis--Lin equality criterion and known
equiangular-line systems.

## Main upgraded claims

1. Spanning interval principle:

   If `R^n` contains `M` distinct equiangular lines spanning `R^n`, then for
   every `d` with `n <= d <= M`,

   ```text
   Pi(n,d) = n/d + sqrt((d-1)(n/d)(1-n/d)).
   ```

   The spanning/full-dimensional condition is essential; a lower-dimensional
   embedding alone is not a KLL equality certificate.

2. The standard 28-line `E_7` configuration gives the whole interval

   ```text
   Pi(7,d) = 7/d + sqrt((d-1)(7/d)(1-7/d))      for 7 <= d <= 28.
   ```

3. Symmetric conference matrices and Paley matrices give analogous intervals.
   If `q` is an odd prime power with `q == 1 mod 4` and `n=(q+1)/2`, then

   ```text
   Pi(n,d) = n/d + sqrt((d-1)(n/d)(1-n/d))      for n <= d <= q+1.
   ```

4. The KLL upper bound itself equals `7/3` for exactly two integer pairs:

   ```text
   (n,d) = (7,15), (49,51).
   ```

   Both are sharp. The second is realized by Paley `q=97`, which gives 98
   equiangular lines spanning `R^49`; a 51-line spanning subsystem certifies

   ```text
   Pi(49,51) = 7/3.
   ```

5. The classical 276 equiangular lines in `R^23` give the large exact interval

   ```text
   Pi(23,d) = 23/d + sqrt((d-1)(23/d)(1-23/d))  for 23 <= d <= 276.
   ```

This is a systematic extension of the reviewed packet, not a claim of new
equiangular-line theory and not a full classification of all pairs with
`Pi(n,d)=7/3`.

## Packet contents

- `main.tex`: follow-up note with proofs and literature context.
- `solution_packet.pdf`: rendered note.
- `literature_exploration.md`: search notes, tools, and future routes checked
  while improving and auditing the packet.
- `source_paper.pdf`: copied source paper from the reviewed packet.
- `figures/source_definition_kll_page4.png`: source crop with the KLL criterion.
- `figures/source_open_question_page24.png`: source crop with Basso's question.
- `code/verify_systematic_families.py`: verifier for the `E_7` interval, the
  KLL `7/3` candidate calculation, prime Paley conference matrices up to
  `q=100`, and an exact `q=97` rank certificate for the 51-line subsystem in
  `R^49`.

## Verification command

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/human_verified/re_llm_answer/1901.07866_pi_equiangular_systematic_family/code/verify_systematic_families.py
```

The verifier is not the proof of the infinite prime-power theorem; it checks
the finite arithmetic and exercises the finite-field construction in a bounded
prime subfamily.

## Human-review focus

Review should focus on four points:

- the exact full-dimensional/spanning form of the KLL equality criterion;
- the spanning interval principle;
- the `7/3` KLL-bound arithmetic, which leaves only `(7,15)` and `(49,51)`;
- the Paley `q=97` spanning certificate for `Pi(49,51)=7/3`.
