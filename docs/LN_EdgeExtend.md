# LN_EdgeExtend

> Pushes colour outward from the edge of a premultiplied element to fill the semi-transparent fringe.

Edge extend for premultiplied elements — it drags colour from inside the matte outward so
the soft fringe has something real to sit on, instead of the dark halo you get when
semi-transparent pixels have no colour behind them.

The pipeline is deliberately in stages so you can shape it:

- **Pre** — erode and blur the source before anything is pushed outward.
- **Extension** — how far the colour is dragged out past the edge.
- **Transition** — erode/blur controls that shape the blend between original and extended
  colour, so the join doesn't read as a hard line.
- **Final Adjustment** — a last blur and sharpen on the result.

The **Viewer** dropdown switches the output between `Final Result`, `Pre_Extension` and
`Extension` so you can see each stage in isolation while you dial it in.

It also carries a full **EdgeMatte** tab (the same controls as [`LN_EdgeMatte`](LN_EdgeMatte.md))
for building the matte that drives the extension.

> **Note:** the group inside this file is still named `LN_EdgeMatte` — a copy-paste
> leftover. It doesn't affect behaviour, just the default node name when you create it.

---

**Category:** Edges & mattes  ·  **Version:** v1.0 (2020)

[← back to all tools](../README.md)
