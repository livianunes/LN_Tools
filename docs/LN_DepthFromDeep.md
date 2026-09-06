# LN_DepthFromDeep

> Derives a normalised depth channel from deep data by sampling a near and a far point.

Turns deep data into a usable depth channel without hand-tuning the normalisation.

You sample two points in the viewer — the **nearest** and **furthest** thing you care
about — press **Set Position**, and it reads the deep samples at those points and sets
the near/far values that normalise the depth between them.

| Control | What it does |
|---|---|
| **Nearest / Far Position** | The two sample points, adjustable in the viewer. |
| **Set Position** | Reads the deep samples at those points and fills in `near` and `far`. |
| **near / far** | The normalisation range — nudge by hand after sampling if needed. |
| **Unpremult** | Whether to unpremultiply before the conversion. |

**Inputs:** `image`, `deep_data`.

---

**Category:** CG & deep

[← back to all tools](../README.md)
