# LN_Tools

A set of Nuke toolsets I've built over the years as a compositor and Comp TD 

They're plain `.nk` toolsets for the most parts, some may have blinkscript and might need a recompile.
Documentation was mostly written by an LLM (Claude), so if there's something weird or wrong, now you know why. Sorry.

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

**Option B — just copy the group into nuke:**
Copy the text from the tool code and paste into your nodegraph.

Restart Nuke. The tools appear under **LN_Tools** in the Nodes toolbar.

`init.py` adds the subfolders to Nuke's plugin path and `menu.py` walks `tools/` and builds
the menu automatically — so any `.nk` you drop into `tools/` shows up on the next restart,
no code change needed.

---

## The tools

<!-- AUTOGEN:TOOLS -->

### Keying & screens

| Tool | What it does |
| --- | --- |
| **[LN_Despill](docs/LN_Despill.md)** | Despill with control over colour bias, edge colour expansion and screen gain. |
| **[LN_EvenScreen](docs/LN_EvenScreen.md)** | Builds a clean plate and an evened-out screen from a green/blue screen plate, so keys pull far more cleanly. |
| **[LN_LogKeyer](docs/LN_LogKeyer.md)** | A luminance keyer that works in log space, so pulling on highlights and shadows behaves. |

### Edges & mattes

| Tool | What it does |
| --- | --- |
| **[LN_AlphaMaskDepth](docs/LN_AlphaMaskDepth.md)** | Holds out the depth channel with the alpha, so depth outside the matte reads as black. |
| **[LN_EdgeExtend](docs/LN_EdgeExtend.md)** | Pushes colour outward from the edge of a premultiplied element to fill the semi-transparent fringe. |
| **[LN_EdgeMatte](docs/LN_EdgeMatte.md)** | Builds an edge matte from an alpha, with independent control of the inside and outside edge. |

### Lens & distortion

| Tool | What it does |
| --- | --- |
| **[LN_DistortReformatted](docs/LN_DistortReformatted.md)** | Applies a lens-distortion ST-Map shot at the original camera format to a reformatted or cropped plate. |
| **[LN_EasyDistort](docs/LN_EasyDistort.md)** | Lightweight local warping driven by ST-Maps, with a soft falloff you can shape. |
| **[LN_LensEffects](docs/LN_LensEffects.md)** | Lens edge defocus and chromatic aberration in one node, GPU-accelerated where available. |

### CG & deep

| Tool | What it does |
| --- | --- |
| **[LN_ConvertPosition](docs/LN_ConvertPosition.md)** | Transforms position and normal AOVs between spaces using an Axis. |
| **[LN_DepthFromDeep](docs/LN_DepthFromDeep.md)** | Derives a normalised depth channel from deep data by sampling a near and a far point. |
| **[LN_NormalsRelight](docs/LN_NormalsRelight.md)** | Relight an image from a normals AOV, or just rotate the normals into another orientation. |

### Colour

| Tool | What it does |
| --- | --- |
| **[LN_ColorMatch](docs/LN_ColorMatch.md)** | Matches one image's colour to another, with separate hue, saturation and value mix. |
| **[LN_Deflicker](docs/LN_Deflicker.md)** | Evens out exposure flicker across a sequence by normalising each frame to a reference frame. |
| **[LN_Reinhard](docs/LN_Reinhard.md)** | Reinhard normalisation and its exact inverse, for working on HDR data in a 0–1 range. |
| **[Original_sRGB](docs/Original_sRGB.md)** | Makes sRGB elements look the way they do outside ACES — for logos, textures and graphics. |

### Light & atmosphere

| Tool | What it does |
| --- | --- |
| **[LN_Rainbow](docs/LN_Rainbow.md)** | Generates a rainbow ramp, or maps an existing image through the hue wheel. |
| **[LN_VolumeRays](docs/LN_VolumeRays.md)** | Volumetric light rays from luminance, alpha or edges, with optional organic flicker. |

### Workflow & QC

| Tool | What it does |
| --- | --- |
| **[GUI_SWITCH](docs/GUI_SWITCH.md)** | A Switch that shows one input in the viewer and renders the other. |
| **[LN_LoopImage](docs/LN_LoopImage.md)** | Loops an image horizontally or vertically, seamlessly and forever. |
| **[LN_PaintDiffMerge](docs/LN_PaintDiffMerge.md)** | Merges paint over a plate only where it was actually painted, and outputs a matte of that region. |
| **[LN_QualityCheck](docs/LN_QualityCheck.md)** | A full QC pass in one node: eleven checking views plus a checklist that fills itself in. |

<!-- /AUTOGEN:TOOLS -->

---

## Adding a tool

1. Save your toolset into `tools/` as `YourTool.nk`.
2. Write `docs/YourTool.md` — a `# Title`, a `> one-line summary`, then whatever you want.
3. Run `python build_index.py` to refresh the table above.

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
