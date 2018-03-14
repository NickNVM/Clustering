# Clustering

## Cluster selection methods

### Single Linkage
<img src="https://imgur.com/ljZTg7E.png" width="300">

### Complete Linkage
<img src="https://imgur.com/LEu6rkA.png" width="300">

### Average Linkage
<img src="https://imgur.com/HOE0XaU.png" width="300">

## SAHN
- Sequential agglomerative hierarchical non-overlapping clustering
- Pseudocode implementation:
  - ```select_clusters()``` refers to the selected method, e.g. single_linkage, multi_linkage
```
left_over_clusters = n
coordinates: [x, y]
clusters: [[x, y]]

foreach coordinate in coordinates:
  cluster: [x, y]
  append coordinate to cluster
  append cluster to clusters
  
while clusters.size > left_over_clusters
  cluster1, cluster2 = select_clusters()
  
  foreach coordinate in cluster2:
    append coordinate to cluster1
  
  remove cluster2 from clusters

```
## SDHN
