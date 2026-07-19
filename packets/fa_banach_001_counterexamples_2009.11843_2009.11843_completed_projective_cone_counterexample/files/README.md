# Counterexample to completed projective-cone semisimplicity

Status: `candidate counterexample -- likely valid` (a full negative answer).

Source: arXiv:2009.11843, Question `q:completed-semisimple` (Question 5.16 in the PDF). The question asks whether, for real Banach spaces with closed proper cones, the completed projective cone must be contained in a closed proper cone.

## Result

The answer is **no**. There exist separable real Banach spaces (E,F) and closed, proper, generating cones (E_+,F_+) for which the closed completed projective cone in (E\widehat\otimes_\pi F) contains a nonzero linear subspace. It is therefore not proper and cannot be contained in any proper cone.

The construction starts with a nonzero element of the kernel of a canonical map (X\widehat\otimes_\pi Y\to X\widehat\otimes_\varepsilon Y), uses bounded injective Hilbert-space maps to define weaker Hilbertian norms (p,q), and equips (\mathbb R\oplus X) and (\mathbb R\oplus Y) with the cones
\[
\{(t,x):t\ge p(x)\},\qquad \{(s,y):s\ge q(y)\}.
\]
Positivity on four boundary pairs forces the (X\times Y) component of every positive bilinear form to factor through the two Hilbert completions. Hence every positive bilinear form annihilates the chosen nonzero kernel tensor. Cone bipolarity then places both signs of that tensor in the closed projective cone.

## Files

- `main.tex`: self-contained proof.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: source paper.
- `figures/source_question.png`: source PDF page containing Question 5.16.
- `verification_report.md`: independent proof audit and scope checks.

## Novelty status

The run's lightweight indexes contained no record for this paper or question. A bounded exact-phrase/current-source search on 2026-07-19 found no advertised resolution; the author's 2023 thesis repeats the question in its open-problems chapter. This is not a global novelty certificate.
