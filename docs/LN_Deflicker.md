# LN_Deflicker

> Evens out exposure flicker across a sequence by normalising each frame to a reference frame.

An internal `CurveTool` analyses average intensity over a region of interest across the
sequence. A `Grade` then scales every frame so its intensity matches the frame you nominate
as reference — flattening exposure flicker.

| Control | What it does |
|---|---|
| **Type** | `Deflicker` removes the variation. `Flicker` reverses the operation and re-applies it — useful for putting the plate's flicker back onto a clean element. |
| **ROI** | The region the analysis samples. Keep it on something that should be constant. |
| **Analyze** | Runs the `CurveTool` over the sequence. **You must do this before the node does anything.** |
| **Reset** | Clears the analysis. |
| **Reference Frame** | The frame everything is matched to. |
| **mix** | Dissolve back towards the original. |

**Workflow:** set the ROI → press **Analyze** → let it run the range → set the reference frame.

---

**Category:** Colour

[← back to all tools](../README.md)
