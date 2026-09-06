# LN_LensEffects

> Lens edge defocus and chromatic aberration in one node, GPU-accelerated where available.

Two lens artefacts that usually get built by hand on every show, packaged together and
driven from a radial vector field so they behave like the optics they're imitating —
strongest at the frame edge, absent in the centre.

### Lens edge defocus

Defocus that increases towards the edge of the frame, shaped by a vignette rather than
applied flat.

| Control | What it does |
|---|---|
| **Defocus Type** / **Defocus Amount** | The blur itself. |
| **Aspect Ratio** | Squeeze the defocus for anamorphic. |
| **Defocus Vignette Size / Shape** | The region that stays sharp. |
| **Falloff** | How abruptly the sharp centre gives way to the defocused edge. |

### Chromatic aberration

Per-channel scaling around the frame centre, with independent **red**, **green** and
**blue** x/y scale so you can match lateral CA that isn't symmetrical.

### Performance

A `BlinkScript` kernel (`RadialVectors`) generates the radial vector field that drives the
defocus. **Use GPU if available** switches that kernel onto the GPU — worth leaving on.

---

**Category:** Lens & distortion

[← back to all tools](../README.md)
