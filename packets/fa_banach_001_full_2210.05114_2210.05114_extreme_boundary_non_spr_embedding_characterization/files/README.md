# Extreme-boundary characterization of non-SPR embeddings

Status: `candidate_full_solution_human_review_needed`

This packet answers the real-scalar Question 6.6 of Freeman–Oikhberg–Pineau–Taylor, arXiv:2210.05114: which Banach spaces admit an isometric embedding into some `C(K)` whose range is not stable phase retrieval?

For a real Banach space `E`, define

```text
Delta(E) = inf_{x,y in S_E} sup_{e* in ext B_{E*}}
           min(|e*(x)|, |e*(y)|).
```

Then a non-SPR isometric embedding exists exactly when `Delta(E)=0`. The canonical evaluation embedding on the weak-star closure of `ext B_{E*}` realizes the worst possible overlap and has optimal SPR constant `1/Delta(E)`. Thus the criterion is intrinsic and quantitatively sharp.

## Files

- `solution_packet.pdf` — full review packet
- `main.tex` — self-contained LaTeX source
- `verification.md` — explicit adversarial verifier report
- `source_paper.pdf` — arXiv:2210.05114v1
- `figures/open_problem_crop.png` — source Question 6.6
- `figures/source_lemma_6_8.png` — source one-sided extreme-point lemma
- `code/make_source_crops.py` — reproducible crop renderer

## Build

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

Regenerate the evidence crops with:

```sh
conda run --no-capture-output -n sandbox python code/make_source_crops.py
```

## Review priority

Review the fibre-extreme-point argument, canonical weak-star boundary embedding, and the interpretation of the informal phrase “which Banach spaces.” The proof is explicitly real-scalar; no complex analogue is claimed.
