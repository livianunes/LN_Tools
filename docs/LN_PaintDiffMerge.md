# LN_PaintDiffMerge

> Merges paint over a plate only where it was actually painted, and outputs a matte of that region.

From the tool itself:

> **Why use this?**
>
> This helps avoid issues when adding back grain that happen when using the paint plate as
> a working plate, as well as facilitating the creation of a matte of the paint region for
> targeted grain replacement. Use this as your main working plate.
>
> **What it does:**
>
> Adds paint on top of plate only in regions that were painted out using a difference mask,
> and creates a `paintMatte` channel with the paint region matte alpha.

The problem: if you use the paint plate as your working plate, you've replaced the whole
frame — so when you add grain back, you're adding it everywhere, including areas that were
never touched. This restricts the paint to where a difference against the original actually
shows a change, and hands you a `paintMatte` channel so you can put grain back on exactly
that region.

**Inputs:** `Denoised_plate`, `Denoised_paint`, `Paint`, `NWB_Plate`.

---

**Category:** Workflow & QC

[← back to all tools](../README.md)
