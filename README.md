# LN_Tools

A set of Nuke toolsets I've built over the years as a compositor and Comp TD 

DISCLAIMER: Documentation was mostly written by AI (Claude), so if there's something weird or wrong, now you know why. Sorry.

Tools are plain `.nk` groups for the most part, no .gizmo's. Some may have blinkscript and might need a recompile.


<p align="center">
  <img src="LNToolsMenu.jpg" alt="The LN_Tools menu in Nuke's node toolbar">
</p>

---

## Install

Clone (or download) this repo somewhere permanent, then point Nuke at it.

**Option A — add it to your `~/.nuke/init.py`:**

```python
nuke.pluginAddPath('/path/to/LN_Tools')
```
Restart Nuke. The tools appear under **LN_Tools** in the Nodes toolbar.

`init.py` adds the subfolders to Nuke's plugin path and `menu.py` walks `tools/` and builds
the menu automatically — so any `.nk` you drop into `tools/` shows up on the next restart,
no code change needed.

**Option B — just copy the group into nuke:**
Copy the text from the tool code and paste into your nodegraph and save in your toolsets.

---

---

## Adding a new tool

1. Save your toolset into `tools/` as `YourTool.nk`.
2. Write `docs/YourTool.md` — a `# Title`, a `> one-line summary`, then whatever you want.

The menu picks the new tool up on the next Nuke restart on its own.

---

## Credits

Everything here is mine unless noted otherwise on the tool's own page, but a couple of
these exist because of other people:

- **[LN_ConvertPosition](docs/LN_ConvertPosition.md)** is very much based on a tool by
  **Adrian Herr**.
- **[LN_EvenScreen](docs/LN_EvenScreen.md)** and
  **[LN_NormalsRelight](docs/LN_NormalsRelight.md)** exist thanks to **Pedro Andrade**,
  who taught me the knowledge that made them possible.

## Licence

[MIT](LICENSE) — use them, change them, ship them on your shows. Credit is appreciated but
not required.

## Contact

**Livia Nunes** — VFX Compositor | Comp TD
[www.livialivialivia.com](https://www.livialivialivia.com) ·
[LinkedIn](https://www.linkedin.com/in/livialivialivia/) ·
[IMDb](https://www.imdb.com/name/nm8958647/)
