import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import AffinityPropagation

print('Beginning')
df = pd.read_csv("../data/subsample_specter.csv")
X_embedded = TSNE(n_components=2, perplexity=50.0,
                    early_exaggeration=50.0).fit_transform(df)

print(X_embedded)
#print(X_embedded)

#plt.scatter(X_embedded[:,0], X_embedded[:,1])
#plt.show()

af = AffinityPropagation(preference=-50).fit(X_embedded)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

print("Number of cluster centers:", len(cluster_centers_indices))
print(len(cluster_centers_indices))
