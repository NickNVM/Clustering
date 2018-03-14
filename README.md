# Clustering
## Cluster selection methods
### Single Linkage
![Single Linkage][single_linkage]
### Complete Linkage
![Complete Linkage][complete_linkage]
### Average Linkage
![Average Linkage][average_linkage]
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
<img src="https://imgur.com/ljZTg7E.png" width="300">
[single_linkage]: https://imgur.com/ljZTg7E.png | width = 100 "Single Linkage"
[complete_linkage]: https://imgur.com/LEu6rkA.png "Complete Linkage"
[average_linkage]: https://imgur.com/HOE0XaU.png "Average Linkage"
