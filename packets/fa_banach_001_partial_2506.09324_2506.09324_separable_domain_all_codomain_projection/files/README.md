# Partial solution packet: separable domains give all-codomain projections

## Source

- Paper: Anil Kumar Karn and Arindam Mandal, *Position of `L(X, Y)` in `Lip_0(X, Y)`*
- arXiv: `2506.09324`
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `partial_result_likely_valid`
- Target question: Question 1.1 asks whether `L(X,Y)` is complemented in `Lip_0(X,Y)`.
- Packet claim: if the barycenter map `beta_X:F(X)->X` of the usual scalar Lipschitz-free space has a bounded linear right inverse, then `L(X,Y)` is complemented in `Lip_0(X,Y)` for every Banach codomain `Y`. In particular, by the Godefroy-Kalton lifting theorem, this holds with a norm-one projection for every separable Banach domain `X` and every Banach codomain `Y`.

## Relation to the previous packet

The previous packet
`solutions/partial/2506.09324_bidual_complemented_codomain_extendable_quotient/`
proved complementability when `Y` is complemented in a dual space and gave an exact quotient model with an extension norm. This packet gives an orthogonal positive result: no assumption on `Y`, but a lifting-property assumption on `X`.

Together, the current positive territory for Question 1.1 now includes:

- all `X` when `Y` is a dual space, by Karn-Mandal;
- all `X` when `Y` is complemented in a dual space, by the previous packet;
- all `Y` when `X` has the Godefroy-Kalton lifting property, in particular when `X` is separable, by this packet.

This is not a full arbitrary-`X`, arbitrary-`Y` solution.

## Supporting reference

- Ferenczi, Kaufmann, and Pernecka, *Equivariant liftings in Lipschitz-free spaces*, arXiv:`2501.06984`, is copied as `supporting_paper_2501.06984.pdf`. It records the Godefroy-Kalton lifting-property theorem for separable spaces and notes that some Banach spaces fail the lifting property.

## Files

- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original source paper.
- `supporting_paper_2501.06984.pdf`: supporting lifting-property reference.
- `figures/open_problem_crop.png`: source page containing Question 1.1.
- `tmp/`: LaTeX build output.

## Verification notes

The key new observation is that the source paper's generalized space `F_Y(X)` is canonically isometric to the usual scalar Lipschitz-free space `F(X)` whenever `Y` is nonzero. For a molecule `sum a_i delta_{x_i}`, the `F_Y(X)` norm is at most the scalar free norm after testing with `Y*`, and at least the scalar free norm by using functions of the form `g(.) y_0`.

Once `beta_X:F(X)->X` has a right inverse `S`, transport `S` to `F_Y(X)` and project `A in L(F_Y(X),Y)` to `A S beta_X^Y`. Under Karn-Mandal's isometry `L(F_Y(X),Y) ~= Lip_0(X,Y)`, this is the desired projection onto `L(X,Y)`.
