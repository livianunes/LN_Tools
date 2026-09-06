# LN_ColorMatch

> Matches one image's colour to another, with separate hue, saturation and value mix.

Transfers the colour character of a reference onto a plate. It blurs both down to compare
their broad colour rather than their detail, converts to HSV, and dissolves each component
independently — so you can take the *hue* from the reference while keeping your own
saturation, or any combination.

| Control | What it does |
|---|---|
| **Blur** | How much detail is thrown away before matching. Higher = matching overall colour cast rather than local detail. |
| **Mix** | Overall strength of the match. |
| **Hue Mix / Saturation Mix / Value Mix** | Per-component strength. |

**Inputs:** `FINAL_PLATE`, `COLOR` (the reference you're matching to).

---

**Category:** Colour

[← back to all tools](../README.md)
