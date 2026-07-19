# Partial Result: Auxiliary Maximal Exponent on the Diagonal `q=p`

- **Source paper:** Spyridon Kakaroumpas and Odi Soler i Gibert, *Vector valued estimates for matrix weighted maximal operators and product BMO*, arXiv:2407.16776.
- **Source target:** The remark before Theorem 6 asks whether the exponent of `[W]_{A_p}` in the vector-valued estimate for the Christ--Goldberg auxiliary maximal operator can be improved.
- **Packet status:** `partial_result_likely_valid`
- **Result type:** solved subcase / exponent improvement.

## Result

For arbitrary matrix `A_p` weights `W`, the extra factor `[W]_{A_p}^{1/p}` in Theorem 6 is removable when the sequence exponent is `q=p`.

Precisely,

```text
|| (sum_n |tilde M_W f_n|^p)^(1/p) ||_Lp
  <= C(n,d,p) [W]_{A_p}^{1/(p-1)}
     || (sum_n |W^{1/p} f_n|^p)^(1/p) ||_Lp.
```

The source theorem gives exponent `1/p + 1/(p-1)` in this diagonal case, so this removes exactly the extra `1/p` loss.

## Proof Idea

When `q=p`, the mixed `L^p(ell^p)` norm splits as a sum of scalar `L^p` norms. Applying the known one-function bound for `tilde M_W` to each coordinate and summing gives the improved vector-valued estimate immediately. The argument does not address the off-diagonal cases `q != p`.

## Files

- `main.tex` - expert-facing proof note.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - source paper.
- `figures/open_problem_crop.png` - source page containing the exponent question and Theorem 6.
