# LN_AlphaMaskDepth

> Holds out the depth channel with the alpha, so depth outside the matte reads as black.

Creates a holdout using the alpha so that **everything in the depth channel outside the
alpha is black**.

Depth passes usually come back filled edge to edge, which makes any depth-driven
operation — defocus, fog, depth-based grades — bleed across the boundary of the element
you actually care about. This restricts `depth.Z` to the alpha and zeroes the rest.

**Unpremulted** tells it whether the incoming image is already unpremultiplied, so the
alpha it derives the holdout from is the right one.

---

**Category:** Edges & mattes

[← back to all tools](../README.md)
