import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Create a "large" dataset
np.random.seed(42)
data = np.random.rand(100, 100)

# This will now use imshow internally instead of QuadMesh
g = sns.clustermap(data, figsize=(15, 15))

plt.savefig('fig-orig.svg', format='svg')
