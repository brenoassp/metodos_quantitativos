import matplotlib
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import random

colors = matplotlib.colors.cnames.items()

df = pd.read_csv('ontime-rate-normalized.csv', sep=" ", header=None)

f1 = df[0].values
f2 = df[1].values

cluster_number = 20

X = np.matrix(list(zip(f1, f2)))
kmeans = KMeans(n_clusters=cluster_number).fit(X)
df['cluster'] = kmeans.predict(X)

for cluster in range(cluster_number):
    df_current_cluster = df.loc[df['cluster'] == cluster]
    x = df_current_cluster.iloc[:, 0].values
    y = df_current_cluster.iloc[:,1].values
    lines, = plt.plot(x, y, '^')
    plt.setp(lines, color=random.choice(list(colors))[0])

plt.xlabel('tempo de on')
plt.ylabel('taxa')
plt.savefig('{0}clusters.png'.format(cluster_number))
plt.show()
