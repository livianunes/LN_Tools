# LN_Reinhard

> Reinhard normalisation and its exact inverse, for working on HDR data in a 0–1 range.

Two expressions and a switch:

- **Reinhard Normalization** — `x / (x + 1)`, which maps `0 → ∞` into `0 → 1`.
- **Revert Normalization** — `-x / (x - 1)`, the exact inverse.

Useful when an operation misbehaves on values above 1 — some blurs, filters and
particularly anything with a clamp inside it. Normalise, do the work, revert. Because the
inverse is exact, you get your highlights back untouched.

---

**Category:** Colour

[← back to all tools](../README.md)
