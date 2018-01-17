
import json 
import pprint
import pandas as pd
import operator
from decimal import Decimal
from sklearn import cluster
from sklearn import metrics
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
from collections import Counter
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
import sys


g=100
filename = '/home/smrnmakhija/Desktop/data/grp'+str(g)+'.json'
#Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)
print("Input")
pprint.pprint(datastore)
a=[]
aa=[]
try:
    # Access data
    for x in datastore['obs']:
        aa.append([x['fuv'], x['nuv'], x['y'],x['x'], x['z'],x['id']])
        a.append([x['fuv'], x['nuv']])
except (ValueError, KeyError, TypeError):
    print "JSON format error"

#print a
#data  = json.loads(r_filenameJSON)
#print data['fruits']

#print data
"""
x=1
kmeans=cluster.KMeans(n_clusters=x, n_jobs=-1,verbose=0,n_init=30)

kmeans.fit(a)

results=[]
results.append(list(kmeans.labels_))
silhouette_avg = silhouette_score(a, kmeans.labels_)
"""

range_n_clusters = [x for x in range(2,len(a)-1)]
l=[]
for n_clusters in range_n_clusters:
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(a)
    silhouette_avg = silhouette_score(a, cluster_labels)
    l.append({'silhouette_avg': silhouette_avg,'n':n_clusters})
print range_n_clusters

#print l
maxN = max(l, key=lambda x:x['silhouette_avg'])
number= maxN['n']
clusterer = KMeans(n_clusters=number, random_state=10)
cluster_labels = clusterer.fit_predict(a)

#print cluster_labels
#print a
i=0
for elem in aa:
    k=str(g)+str(cluster_labels[i])
    elem.append(k)
    i=i+1
col=['fuv','nuv','y','x','z','id','subgroup']
df=pd.DataFrame.from_records(aa,columns=col)
#print df
df=df.groupby('subgroup').agg({'fuv':'mean','nuv': 'mean','y': 'mean','x':'mean', 'z':'mean'}) 
print "   "
print("For CSV")
print df
subg=[]
idd={}
for sub in range(len(aa)):
    d = {}
    
    d["fuv"] = aa[sub][0]
    d["nuv"] = aa[sub][1]
    d["y"] =aa[sub][2]
    d["x"] =aa[sub][3]
    d["z"] =aa[sub][4]
    d["id"] =aa[sub][5]
    idd[sub]=d["subgroup"]=aa[sub][6] 
    subg.append(json.dumps(d, ensure_ascii=False))
print("")
print("JSON")
pprint.pprint(subg)
#print idd


"""
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print "centroids : "
print centroids
print "labels : "
print labels
cluster_num=3
color = ["g", "r", "b"]


c = Counter(labels)


fig = figure()
ax = fig.gca(projection='3d')


for i in range(len(a)):
    print("coordinate:",a[i], "label:", labels[i])
    print "i : ",i
    print "color[labels[i]] : ",color[labels[i]]
    ax.scatter(a[i][0], a[i][1], a[i][2], c=color[labels[i]])


for cluster_number in range(cluster_num):
  print("Cluster {} contains {} samples".format(cluster_number, c[cluster_number]))

ax.scatter(centroids[:, 0],centroids[:, 1], centroids[:, 2], marker = "x", s=150, linewidths = 5, zorder = 100, c=color)
plt.show()
"""