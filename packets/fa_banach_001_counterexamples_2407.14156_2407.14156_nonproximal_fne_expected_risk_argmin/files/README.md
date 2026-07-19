# Non-Proximal FNE Expected-Risk Argmin

Status: `candidate_counterexample_likely_valid`

Source paper: Kristian Bredies, Jonathan Chirinos-Rodriguez, and Emanuele Naldi,
*Learning Firmly Nonexpansive Operators*, arXiv:2407.14156v3.

Targeted source question: near the end of the "Third experiment: proximity
operators" discussion, the paper asks whether data-driven firmly nonexpansive
operators preferentially converge to proximity operators, or more strongly
whether proximity operators are the only objects in the argmin of the expected
risk problem (CP) for "real" data distributions.

Packet result: the universal version is false under the source paper's stated
expected-risk hypotheses.  If `X` is a standard Gaussian in `R^2` and `Y=R_90 X`,
then the unique minimizer of the source paper's nonexpansive expected-risk
problem (CP) is `N=R_90`.  The associated firmly nonexpansive learned operator
`T=(Id+N)/2=(Id+R_90)/2` is not a proximity operator because its circulation
around the unit circle is `pi`.

Limitations: this does not disprove the empirical observation that the authors'
natural-image experiments produced nearly conservative maps, and it does not
rule out positive theorems under additional image/statistical structure.  It
only rules out a theorem based solely on the expected-risk framework, finite
second moments, and full support.

Verification:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2407.14156_nonproximal_fne_expected_risk_argmin/code/verify_linear_counterexample.py
```

The script checks the firm-nonexpansiveness matrix inequality, the
nonexpansiveness of the associated `(CP)` variable, and the nonzero circulation.

Novelty check: local run indexes were searched for `2407.14156`, `Learning
Firmly Nonexpansive Operators`, `proximal argmin`, `nonproximal`, and close
firmly-nonexpansive/proximity phrases.  Web search on 2026-07-19 for the exact
future-work phrase and close variants found the source paper and general PnP
references, but no existing answer to this exact question.  Novelty confidence
is moderate because the construction is elementary and may be folklore.
