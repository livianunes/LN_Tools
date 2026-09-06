# LN_VolumeRays

> Volumetric light rays from luminance, alpha or edges, with optional organic flicker.

God rays generated from whatever you have, rather than requiring a specific pass.

**Volumetric Creation** picks the source:

- `RGB / Luminance` — rays from the bright areas of the image, with a **Luma Tolerance** threshold.
- `Alpha / Edges` — rays from the edge of a matte, with **Edge Size** and **Edge Blur**.
- `Alpha / Solid` — rays from the filled matte.
- `Shadow Making` — inverts the logic to cast volumetric shadows instead.

| Control | What it does |
|---|---|
| **Volumetrics Center** | Where the rays radiate from. |
| **Ray Length** | How far they travel. |
| **Pre-Ray Blur** | Softens the source before rays are generated. |
| **Quality** | `Low` → `Very High`. Raise it once you've stopped iterating. |
| **Add on Top** | Merge over the input, or output the rays alone. |

### Flicker

Real volumetrics breathe. **Use Flickering** drives the rays with animated noise —
**Flicker Speed** and **Flicker Size** shape it. **Transform noise with Volume Center**
moves the noise field with the light source, so a moving source doesn't cause the rays to
boil; the only remaining variation is the flicker itself.

**Inputs:** `img`, `mask`, `negativeVolumeMask`. The **alpha channel is what the mask input
needs.**

---

**Category:** Light & atmosphere

[← back to all tools](../README.md)
