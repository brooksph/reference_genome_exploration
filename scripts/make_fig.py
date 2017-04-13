import pandas as pd
import seaborn as sns
sns.set(font = "monospace")

# Load the brain networks example dataset
# Load the brain networks example dataset
df = pd.read_csv('all_compare_k51.csv', header = None)




# Create a custom colormap for the heatmap values
cmap = sns.cubehelix_palette(as_cmap=True, rot=-.3, light=1)



# Draw the full plot
sns.set_context("paper")
sns.clustermap(df.corr(), linewidths=.5, figsize=(12, 12), standard_scale=1, cmap=cmap)

fig.savefig("output.png")
