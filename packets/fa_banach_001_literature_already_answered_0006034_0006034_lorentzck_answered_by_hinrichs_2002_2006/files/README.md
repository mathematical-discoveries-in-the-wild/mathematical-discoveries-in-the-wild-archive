# Lorentz `lorentzck` conjecture answered in later s-number literature

Status: `literature_already_answered`

Source/open-problem paper: Andreas Defant, Mieczyslaw Mastylo, and Carsten
Michels, "Summing inclusion maps between symmetric sequence spaces",
arXiv:math/0006034. The published version is Transactions of the American
Mathematical Society 354 (2002), 4473--4492, DOI
`10.1090/S0002-9947-02-03056-8`.

Supporting answer papers:

- Aicke Hinrichs, "Approximation Numbers of Identity Operators between
  Symmetric Sequence Spaces", Journal of Approximation Theory 118 (2002),
  305--315, DOI `10.1006/jath.2002.3726`.
- Aicke Hinrichs and Carsten Michels, "Gelfand Numbers of Identity Operators
  Between Symmetric Sequence Spaces", Positivity 10 (2006), 111--133, DOI
  `10.1007/s11117-005-0022-1`.

## Source Conjecture

At the end of the source paper, on page 19 of `source_paper.pdf` and
immediately after the corollary containing the displayed formula labelled
`lorentzck`, the authors conjecture that the same formula holds for all
`1 < u_1 < v_1 < 2` and all `1 <= u_2, v_2 <= infinity`:

```text
c_k(id: ell_{v_1,v_2}^n -> ell_{u_1,u_2}^n)
  asymp a_k(id: ell_{v_1,v_2}^n -> ell_{u_1,u_2}^n)
  asymp (n-k+1)^{1/u_1 - 1/v_1}.
```

The source paper proves only special secondary-parameter ranges before this
conjectural sentence.

## Supporting Answer

The 2006 Hinrichs--Michels paper explicitly identifies the Defant--Mastylo--
Michels conjecture as formula (1.1), involving both approximation numbers
`a_k` and Gelfand numbers `c_k` for finite-dimensional identity maps between
symmetric sequence spaces. It states that it proves this formula under its
interpolation hypotheses and illustrates the result on Lorentz spaces.

For the present target, Example 7.5(ii) in the 2006 paper gives, for
`0 < p_1 < q_1 < infinity` and `0 < p_2, q_2 <= infinity`,

```text
c_k(id: ell_{q_1,q_2}^n -> ell_{p_1,p_2}^n)
  asymp (n-k+1)^{1/p_1 - 1/q_1}.
```

The paper also notes that the same displayed formulas hold for approximation
numbers by replacing the corresponding Gelfand/Kolmogorov symbols with `a_k`;
the 2002 Hinrichs paper separately supplies the approximation-number side and
is cited in the 2006 introduction as earlier confirmation of the DMM
conjectural formula under regularity assumptions.

## Identification

Set

```text
p_1 = u_1,   q_1 = v_1,   p_2 = u_2,   q_2 = v_2.
```

The supporting range `0 < p_1 < q_1 < infinity` and
`0 < p_2, q_2 <= infinity` contains the source conjecture's Banach-space range
`1 < u_1 < v_1 < 2` and `1 <= u_2, v_2 <= infinity`. Under this substitution,
the exponent in the supporting formula becomes exactly
`1/u_1 - 1/v_1`, and the identity map has the same source and target Lorentz
spaces as the source conjecture.

Thus the source conjecture is already answered in the later s-number
literature. This packet is not an original lane proof.

## Search Evidence

Cheap run indexes showed no previous exact `0006034` packet. External bounded
queries for the source arXiv id, `lorentzck`, "Gelfand Numbers of Identity
Operators Between Symmetric Sequence Spaces", and "Approximation Numbers of
Identity Operators between Symmetric Sequence Spaces" located the two decisive
supporting papers above. The 2006 full-text page explicitly names the
Defant--Mastylo--Michels conjecture as formula (1.1); ScienceDirect and the JKU
research portal confirm the 2002 approximation-number article metadata and
abstract.

## Files

- `source_paper.pdf`: locally rendered from the arXiv TeX source.
- `source_tex/`: copied arXiv source files used to render the source paper.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `tmp/`: LaTeX build intermediates.

The decisive supporting papers are cited by DOI. Local supporting PDFs were not
available in the repository cache during this lane loop.

## Scope

The packet records an already-known literature answer to the Lorentz
`lorentzck` conjecture from arXiv:math/0006034. It does not claim a new proof
or address unrelated questions in the source paper.
