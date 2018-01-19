import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from math import sqrt
from calc import standard_deviation, avg

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return sqrt(((point.x - self.x)**2) + ((point.y - self.y)**2))


df = pd.read_csv('ontime-rate-normalized.csv', sep=" ", header=None)

f1 = df[0].values
f2 = df[1].values

for i in range(18):
    cluster_number = i + 3

    X = np.matrix(list(zip(f1, f2)))
    kmeans = KMeans(n_clusters=cluster_number).fit(X)
    df['cluster'] = kmeans.predict(X)

    dists_intra_cluster = []
    for cluster in range(cluster_number):
        df_current_cluster = df.loc[df['cluster'] == cluster]
        cluster_centroid = Point(kmeans.cluster_centers_[cluster][0], kmeans.cluster_centers_[cluster][1])

        for row in df_current_cluster.iterrows():
            p = Point(row[1][0], row[1][1])
            dists_intra_cluster.append(p.dist(cluster_centroid))

    intra_cv = standard_deviation(dists_intra_cluster) / avg(dists_intra_cluster)

    centroids = kmeans.cluster_centers_
    dists_inter_clusters = []
    for i in range(len(centroids)):
        centroid = Point(centroids[i][0], centroids[i][1])
        j = i+1
        while j < len(centroids):
            centroid_n = Point(centroids[j][0], centroids[j][1])
            dists_inter_clusters.append(centroid.dist(centroid_n))
            j += 1
    inter_cv = standard_deviation(dists_inter_clusters) / avg(dists_inter_clusters)

    file = open('numberOfClustersXintraCv.txt', 'a')
    file.write('{0} {1} {2}\n'.format(cluster_number, intra_cv, inter_cv))
    file.close()

#import pdb
#pdb.set_trace()
