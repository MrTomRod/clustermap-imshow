# clustermap-imshow

A monkey patch for `seaborn.clustermap` that uses `imshow` instead of `pcolormesh` (rectangles) for rendering the heatmap.

## Why?

Rendering large heatmaps with `seaborn.clustermap` can be extremely slow in web browsers (e.g., when using `jupyter` or exporting to SVG/HTML) because it creates thousands of individual rectangle objects (QuadMesh). 

By switching to `imshow`, the heatmap is rendered as a single image, which is significantly faster and more memory-efficient for large matrices while maintaining pixel-perfect accuracy.

## Installation

This is a local package. You can install it in your environment using `uv`:

```bash
uv pip install -e .
```

## Usage

Apply the patch at the beginning of your script before calling `sns.clustermap`.

```python
import seaborn as sns
import numpy as np
from clustermap_imshow import apply_patch

# Apply the monkey patch
apply_patch()

# Create a large dataset
data = np.random.rand(100, 100)

# This will now use imshow internally
g = sns.clustermap(data, figsize=(10, 10))
```

## Features

- **Performance**: Dramatically faster rendering for large plots.
- **Compatibility**: Supports `vmin`, `vmax`, `cmap`, `norm`, and `annot=True`.
- **Accuracy**: Uses `interpolation="none"` and careful coordinate alignment to match the original `seaborn` output exactly.
