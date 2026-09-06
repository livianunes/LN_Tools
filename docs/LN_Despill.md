# LN_Despill

> Despill with control over colour bias, edge colour expansion and screen gain.

A despill built around a screen-colour sample rather than a fixed hue, so it behaves on
screens that aren't a clean primary.

Rather than just knocking the dominant channel down, it lets you decide what colour the
despilled edge should become (**Despill Colour Bias**), how far that replacement colour
is pushed into the edge (**Edge Colour Expand**), and how much of the original screen
brightness is retained (**Screen Gain**). **Screen Colour Balance** and the luminance
maths control how the suppression is weighted across the channels.

Plug the **denoised** plate in — despill on grainy source tends to bloom the noise into
the edge.

---

**Category:** Keying & screens

[← back to all tools](../README.md)
