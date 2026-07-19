# Literature-Already-Answered: planar bilipschitz extension from separated nets

Status: `literature_already_answered (two-dimensional subproblem)`

Run: `fa_banach_001`

Agent: `agent_lane_01`

## Source/Open-Problem Signal

- Michael Dymond and Vojtech Kaluza, *Extending Bilipschitz Mappings between
  Separated Nets*, arXiv:2507.22007; published as Annales Fennici
  Mathematici 51 (2026), 237--260, DOI `10.54330/afm.181562`.
- Local source PDF: `source_paper.pdf`.

The introduction frames the Alestalo--Trotsenko--Vaisala separated-net
bilipschitz extension problem: whether every bilipschitz map from a separated
net of `R^d` to `R^d` extends to a bilipschitz self-map of `R^d`. The same
paper proves a reduction from arbitrary separated nets to `Z^d` in every
finite dimension, and states that a companion article completes the dimension
two case.

## Supporting Answer

- Michael Dymond and Vojtech Kaluza, *Planar bilipschitz extension from
  separated nets*, Journal of the London Mathematical Society 113 (2026),
  e70540, DOI `10.1112/jlms.70540`.
- The Wiley PDF endpoint was Cloudflare-blocked during packet creation; see
  `supporting_paper_jlms_2026_download_blocked.html`. The DOI page and ISTA
  Research Explorer metadata were checked on 2026-07-18.

The JLMS article explicitly states that every `L`-bilipschitz map
`Z^2 -> R^2` extends to a `C(L)`-bilipschitz map `R^2 -> R^2`, with polynomial
control, and by combining this with the companion reduction obtains the same
extension theorem for every separated net in `R^2`. Its abstract/introduction
state that this answers Navas' 2015 Oberwolfach problem and gives the
two-dimensional positive solution of the Alestalo--Trotsenko--Vaisala problem.

## Scope

This packet records only the planar case. The higher-dimensional problem
`d >= 3` and the source's Conjectures 1 and 2 remain open according to the
source paper.

This is not an original run proof; it is a literature-status consolidation to
prevent lane agents from re-attacking an already answered two-dimensional
subproblem.

## Evidence and Search Bounds

Cheap indexes were searched for `2507.22007`, `Extending Bilipschitz Mappings`,
`separated nets`, `bilipschitz extension`, `Alestalo Trotsenko Vaisala`, and
`Navas Problem 2.6.1`. No prior packet for this exact 2026 planar answer was
found. Adjacent run packets concern Banach-valued Lipschitz extensions from
nets, not bilipschitz self-extension of Euclidean separated nets.

Web checks on 2026-07-18 found the JLMS DOI page and ISTA Research Explorer
record for *Planar bilipschitz extension from separated nets*, both recording
the 2026 publication and the explicit planar answer.

## Human Review Notes

Recommended review focus:

- Confirm that the `2507.22007` reduction theorem is exactly the one used by
  the JLMS paper to pass from `Z^2` to arbitrary separated nets in `R^2`.
- Confirm that Alestalo--Trotsenko--Vaisala item 4.4(a)--(b) and Navas
  Problem 2.6.1 are the intended original questions.
- Confirm that dimensions `d >= 3` are not claimed solved by this packet.
