# Counterexample: test forms need not be dense in the covariant Sobolev space

Status: `counterexample_likely_valid`.

Source target: Andrea Carbonaro, Luca Tamanini, and Dario Trevisan, *Boundedness of Riesz transforms on `RCD(K, infinity)` spaces*, arXiv:2308.16294.

The source asks whether `TestForm(X)` is dense in the Sobolev spaces
`W_C^{1,2}(T^*X)` and `W_H^{1,2}(T^*X)` associated with the covariant derivative and the Hodge differential/codifferential. The paper then denotes by `H_C^{1,2}` and `H_H^{1,2}` the respective test-form closures.

This packet gives a negative answer for the covariant Sobolev space. Take
`X=[0,1]` with its Euclidean distance and Lebesgue measure, an `RCD(0,infinity)` space. The Cheeger Laplacian on this interval is the Neumann Laplacian. Hence every test function `f` satisfies `f'(0)=f'(1)=0`, so every test 1-form
`sum_i g_i df_i` has coefficient with zero trace at both endpoints. Therefore the `W_C^{1,2}` closure of test forms is contained in `H_0^1([0,1]) dx`.

However, the constant 1-form `dx` belongs to the maximal covariant Sobolev space:
under the standard interval identification,
`W_C^{1,2}(T^*[0,1]) = H^1([0,1]) dx` and `nabla(u dx)=u' dx tensor dx`.
The coefficient `u=1` has nonzero trace, so `dx` cannot be approximated by test forms in the `W_C^{1,2}` norm.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: source page crop containing the open problem.

Scope and limitations:

- The packet disproves density in `W_C^{1,2}(T^*X)` for one compact `RCD(0,infinity)` space with boundary.
- It does not decide density in the Hodge Sobolev space `W_H^{1,2}(T^*X)`, where boundary conditions can enter differently.
- Human review should check the source's intended convention that `W_C^{1,2}` is the maximal covariant Sobolev domain and `H_C^{1,2}` is only the closure of test forms. The source wording and a related 2019 paper both distinguish these two spaces.

Bounded novelty check:

- Searched the run indexes for `2308.16294`, `TestForm`, `test forms dense`, `W_C`, `H_C`, `covariant Sobolev`, and `RCD`.
- Searched the local arXiv source corpus for the exact target sentence and related `W_C/H_C` terminology.
- Web searches for exact phrases around `TestForm` density and `W_C^{1,2}` found the source paper and related background, but no later public solution or existing interval counterexample in the bounded search.
