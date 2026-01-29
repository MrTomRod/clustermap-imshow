import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from clustermap_imshow import apply_patch
import time

# Define output directory using Path
output_dir = Path("docs/images")
output_dir.mkdir(parents=True, exist_ok=True)

# Create a dataset
np.random.seed(42)
data = np.random.rand(100, 100)

# 1. Original Seaborn (QuadMesh)
print("## Generating original (QuadMesh) plot. ##")
start_time = time.time()
g_orig = sns.clustermap(data, figsize=(10, 10))
g_orig.fig.suptitle("Original (QuadMesh)", fontsize=16)
orig_path = output_dir / "fig-orig.svg"
g_orig.savefig(orig_path, format="svg")
plt.close(g_orig.fig)
orig_time = time.time() - start_time

# Print file size and execution time
orig_size = orig_path.stat().st_size / 1024  # Size in KB
print(f"Original plot saved to {orig_path}.")
print(f" - File size: {orig_size:.2f} KB")
print(f" - Time taken: {orig_time:.2f} seconds")

# 2. Patched Seaborn (imshow)
print()
print("## Applying patch and generating new (imshow) plot. ##")
start_time = time.time()
apply_patch()
g_patched = sns.clustermap(data, figsize=(10, 10))
g_patched.fig.suptitle("Patched (imshow)", fontsize=16)
patched_path = output_dir / "fig-patched.svg"
g_patched.savefig(patched_path, format="svg")
plt.close(g_patched.fig)
patched_time = time.time() - start_time

# Print file size and execution time
patched_size = patched_path.stat().st_size / 1024  # Size in KB
print(f"Patched plot saved to {patched_path}.")
print(f" - File size: {patched_size:.2f} KB")
print(f" - Time taken: {patched_time:.2f} seconds")

# Print differences
print()
print("## Differences ##")
size_diff = orig_size - patched_size
time_diff = orig_time - patched_time
size_percent_diff = (size_diff / orig_size) * 100
time_percent_diff = (time_diff / orig_time) * 100
print(f" - Size difference: {size_diff:.2f} KB ({size_percent_diff:.2f}%)")
print(f" - Time difference: {time_diff:.2f} seconds ({time_percent_diff:.2f}%)")
