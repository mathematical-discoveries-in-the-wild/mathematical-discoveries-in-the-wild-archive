# Proof intuition

A multibranching diamond is recursively a parallel composition of `k` arms,
each arm being two smaller diamonds in series.  A pair of vertices has only
one genuinely parallel separation: at the first recursive cell where the
vertices occupy different arms.  Once that arm pair is distinguished, the
distance is determined by their distances to the top and bottom of the cell.

Label the `k` arms by distinct `m`-bit words.  Reading only bit `j` collapses
the `k` arms onto the two arms of a binary diamond and defines a graph map
`pi_j`.  All these maps preserve distances to the two endpoints of every
recursive cell.  If two vertices first split into arms `a` and `b`, any bit
on which the words of `a` and `b` differ makes their images occupy distinct
binary arms, so the endpoint formula for their distance is unchanged.  Thus
for every pair, one of the `m` maps is exactly distance preserving.

The already-known binary map `f_n` is nonexpansive in `ell_1` and has a
uniform inverse estimate in the summing norm.  Average the `ell_1` blocks
`f_n pi_j` by a factor `1/m` and place them consecutively.  Their `ell_1`
distances average to at most the source distance.  Although earlier blocks
may offset the running partial sum of a later block, an offset can shrink the
largest absolute partial sum by at most a factor two: two numbers a distance
`s` apart cannot both have absolute value below `s/2`.  The exactly
distance-preserving block therefore supplies the inverse estimate, with
constant `2 m C_2`.

