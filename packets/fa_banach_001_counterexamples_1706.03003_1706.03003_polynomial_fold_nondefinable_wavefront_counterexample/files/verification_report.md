# Verification report

verdict: likely valid counterexample

reviewed_at: 2026-07-22

agent_id: agent_lane_10

model: GPT5.6

## Statement checked

For the smooth \(\mathcal C^{\exp}\)-class density
\(h_F(x,y)=q_F^{\operatorname{ord}x}-\operatorname{ord}y\) on
\((\mathcal O_F\setminus\{0\})^2\times\mathcal O_F\), the polynomial fold
\(f(x,y,t)=(x,y,t^2)\) has pushforward wave-front set
\[
\{((x,y,0),(0,0,\eta)):h_F(x,y)\ne0,\ \eta\ne0\},
\]
which is nondefinable.

## Checks

1. **Smoothness:** `ord` is locally constant on \(F^\times\); hence \(h_F\)
   is locally constant on the stated domain.
2. **Class membership:** \(h_F\) is constructible from an integer-valued
   definable function and the allowed generator \(q_F^\alpha\).  Its
   associated B-function is \(\mathcal C^{\exp}\) by parameterized
   integration.
3. **Properness on support:** the preimage of a compact target set, intersected
   with the support, is closed inside
   \(\operatorname{pr}_{X_F}(K)\times\mathcal O_F\), which is compact.
4. **Fold singularity:** the exact identity
   \(\nu_F(B_r(0))=q_F^{-\lceil r/2\rceil}\) contradicts the
   \(c q_F^{-r}\) scaling of a locally constant density near zero.
5. **No other singularities:** for odd residue characteristic the square map
   has nonzero derivative at every nonzero preimage; inverse branches give a
   locally constant pushforward density away from zero.
6. **Exact wave front:** the source pushforward theorem gives
   \(\mathrm{WF}\subset N_f\); direct differentiation gives the vertical
   conormal line.  Projection to singular support and \(F^\times\)-conicity
   give the reverse inclusion.
7. **Nondefinability:** a definable zero locus would give the Presburger graph
   \(n=q_F^m\) in the value group.  Presburger-definable functions are
   eventually affine on residue classes, so this graph is impossible.

## Main review risk

The mathematical calculation is robust.  The main risk is terminological:
the source sentence may have intended an additional unstated requirement that
the smooth density itself have definable zero/nonzero locus.  The example is
smooth and \(\mathcal C^{\exp}\)-class, exactly matching the surrounding
framework, but it is designed so that its coefficient's nonzero locus is not
definable.  The packet states this limitation prominently.

