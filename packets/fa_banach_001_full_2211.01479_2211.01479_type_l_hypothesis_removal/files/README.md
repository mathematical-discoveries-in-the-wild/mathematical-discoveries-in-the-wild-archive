# Removing the Type L hypothesis for sub-semihypergroups

Status: **candidate full solution, likely valid; human expert review required**.

Source: Choiti Bandyopadhyay, *Topological Amenability of Semihypergroups*, arXiv:2211.01479; published in *Forum Mathematicum* 36 (2024), no. 4, 943-954.

The final remark on page 16 of the arXiv PDF asks whether the assumption that a sub-semihypergroup `H` be of Type L can be removed from Theorem 3.5. The packet proves that it can: for every closed sub-semihypergroup `H` of a semitopological semihypergroup `K`, the existence of a topological left `H`-invariant mean `m` on `M(K)^*` with `m(chi_H)>0` implies that `H` admits a TLIM.

The key observation is that the defect of the restriction map is exactly the positive mass transported from `H^c` into `H`. Its lattice modulus is dominated by

`L_{nu^e} chi_H - chi_H`,

which is positive and has mean zero by `H`-invariance. This replaces the source proof's Type L set identity.

Files:

- `solution_packet.pdf`: complete review packet.
- `main.tex`: proof source.
- `verification.md`: claim-by-claim adversarial audit.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: source-question evidence.
- `code/make_source_crop.py`: reproducible crop generator.

The first open question in the same final remark—whether ordinary left amenability implies topological left amenability—remains untouched.
