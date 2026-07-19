# Full solution packet: translated caps break John--Lowner duality for every s

Status: candidate full solution, likely valid

## Source problem

Grigory Ivanov and Igor Tsiutsiurupa, *Functional Lowner Ellipsoids*,
arXiv:2008.09543, Section 9, PDF page 22.  The authors conjecture that for
every positive finite `s` there is a proper log-concave function `f` for which

`(J_s f)^circ != L_s(f^circ)`.

## Result

The conjecture holds already in dimension one.  For arbitrary `s>0` and
`0<a<1`, set

`f_{s,a}(x)=(1-(x-a)^2)_+^(s/2)`.

This is itself an admissible John `s`-ellipsoidal function, so
`J_s(f_{s,a})=f_{s,a}`.  Its polar is

`f_{s,a}^circ(y)=exp(-a y-psi_s(|y|))`.

The negative-log derivative has limits `1+a` at positive infinity and `a-1`
at negative infinity.  Every one-dimensional Lowner `s`-ellipsoidal function
has limits `b` and `-b` for one common `b>0`.  The polar is therefore not in
the Lowner class, proving the desired inequality.

## Files

- `solution_packet.pdf`: review-ready proof.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: complete source conjecture from PDF page 22.
- `tmp/`: build and render intermediates.

## Human review focus

Check the translation formula for log-polarity, the source convention for the
John/Lowner `s`-ellipsoidal classes, and the two tail-derivative limits.  The
argument deliberately does not need to compute the Lowner optimizer itself.

Novelty confidence is moderate: bounded searches found a later general paper
noting that functional John and Lowner optimizers are generally not dual, but
no primary source giving this all-`s` translated-cap family or explicitly
resolving the conjecture.
