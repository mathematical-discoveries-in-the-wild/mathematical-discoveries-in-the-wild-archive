# Bounded Uniformly Discrete Metrics Have Positive Beta

status: full_solution_likely_valid (literal existential clause of Question q3)

source_arxiv_id: 1206.3774

source_title: Embeddability of snowflaked metrics with applications to the nonlinear geometry of the spaces \(L_p\) and \(\ell_p\) for \(0<p<\infty\)

source_authors: Fernando Albiac, Florent Baudier

packet_type: full

## Claim

Question q3 asks whether there are metric spaces other than ultrametrics with
\(\beta_{\mathcal M}>0\), where
\[
\beta_{\mathcal M}=\sup\{t\ge 0:(\mathcal M,d)\operatorname{Lip}(\mathcal M,d^{1-t})\}.
\]

On the literal reading of the question, yes: every bounded uniformly discrete
metric space belongs to the complement of \(\mathsf{NS_T}\). In particular,
there are infinite bounded uniformly discrete metric spaces that are not
ultrametric and nevertheless have \(\beta_{\mathcal M}>0\).

The packet gives an explicit infinite example:
\[
M=\{a,b,c\}\cup\{x_n:n\ge 1\},
\]
with distances \(d(a,b)=d(b,c)=1\), \(d(a,c)=3/2\),
\(d(x_n,u)=2\) for \(u\in\{a,b,c\}\), and
\(d(x_m,x_n)=1\) for \(m\ne n\). This is a bounded uniformly discrete metric,
is not ultrametric, and embeds Lipschitzly into every nontrivial snowflake of
itself by the identity map.

## Scope

This is a full answer to the existential half of Question q3. It is not a full
classification of \(\complement{\mathsf{NS_T}}\). If the intended question was
restricted to unbounded spaces, Banach spaces, spaces without isolated points,
or spaces modulo the bounded-uniformly-discrete triviality, that stronger
version remains outside this packet.

## Verification

- Packet: `main.tex`
- Rendered proof packet: `solution_packet.pdf`
- Source paper PDF: `source_paper.pdf`
- Open-problem crop: `figures/open_problem_crop.png`
- Source TeX used for the open-problem transcription:
  `data/parsed/arxiv_sources/1206.3774/source.tex`, lines 1087--1096.
- Local source e-print metadata:
  `data/raw/arxiv/1206.3774/source_metadata.json`.

## Novelty Check

Bounded search performed on 2026-07-18:

- local run indexes:
  `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`,
  `proof_gaps/index.tsv`;
- local source and deterministic scan for `1206.3774`, `beta_M`,
  `beta_{\mathcal M}`, `other than ultrametrics`, `bounded uniformly discrete`,
  and close variants;
- external web queries around `beta_M snowflaked ultrametrics`,
  `metric space embeds into its own snowflake`, and
  `bounded uniformly discrete snowflake Lipschitz equivalent`.

No duplicate packet or exact literature answer was found in this bounded
search. The confidence is limited by the triviality of the observation: a
human reviewer should check whether the source authors intended to exclude
bounded uniformly discrete spaces implicitly.
