# Code Notes

No computational verification was used for this packet.

The key estimates are exact:

- the map lands on the unit sphere because
  `a(r)^2 + b(r)^2 r^2 = 1`;
- on the sphere the map is the Hilbert-space isometry `U`;
- hence `T^n = U^{n-1}T` for all `n>=1`;
- the approximate fixed points are
  `v_N=(e_0+...+e_{N-1})/sqrt(N)`, for which
  `||Uv_N-v_N||=sqrt(2/N)`.

