# LN_LogKeyer

> A luminance keyer that works in log space, so pulling on highlights and shadows behaves.

A `Keyer` sandwiched between `lin → log` and `log → lin` conversions, with a gamma on the
resulting alpha.

Luminance keys pulled in linear are dominated by the highlights — the range you actually
want to key on is squeezed into a tiny slice of the slider. Converting to log first
spreads the tonal range out, so the keyer's range control has useful resolution across
the whole image. The **gamma** shapes the matte's falloff afterwards.

All the exposed knobs are linked straight through to the internal `Keyer`: *output*,
*combine*, *invert*, *operation* and *range*.

---

**Category:** Keying & screens

[← back to all tools](../README.md)
