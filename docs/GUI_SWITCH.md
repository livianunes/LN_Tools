# GUI_SWITCH

> A Switch that shows one input in the viewer and renders the other.

A one-node trick rather than a real tool, but it earns its place.

A `Switch` with `disable` set to `!$gui`. In the GUI the switch is active and passes
**input 1**; at render time it's disabled and falls through to **input 0**.

Use it to keep something cheap on screen while you work — a proxy, a frozen frame, a
degraded precomp — while the render always takes the expensive, correct branch. No
remembering to flip it back before you submit.

- **input 0** → what renders
- **input 1** → what you see while working

---

**Category:** Workflow & QC

[← back to all tools](../README.md)
