# LN_ConvertPosition

> Transforms position and normal AOVs between spaces using an Axis.

Converts position/normal data between coordinate spaces by running it through a colour
matrix built from an `Axis`. If an object has moved, been re-parented, or your position
pass is in the wrong space to be useful, this puts it back where you need it.

| Control | What it does |
|---|---|
| **data type** | `normal / vectors` or `point / positions` — they transform differently, so this matters. |
| **Transformation** | The `Axis` driving the conversion. |
| **Uniform Scale / Total Scale** | Scaling applied as part of the transform. |

**Inputs:** `src` (the AOV), `objLocatorAxis`.

> You need an `Axis` node carrying the object animation to use this mode.

*Thanks to **Adrian Herr** — this tool is very much based on his.*

---

**Category:** CG & deep  ·  **Version:** v1.0 (2021)

[← back to all tools](../README.md)
