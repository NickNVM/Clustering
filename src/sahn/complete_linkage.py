import util


def cluster_distance(cluster, ind1, ind2, x_coord, y_coord, cache):
    if ind2 in cache[ind1]:
        return cache[ind1][ind2]

    c1 = cluster[ind1]
    c2 = cluster[ind2]
    highest_linkage = -1

    for i1 in c1:
        for i2 in c2:
            dist = util.distance(x_coord[i1], y_coord[i1], x_coord[i2], y_coord[i2])
            if highest_linkage == -1 or dist > highest_linkage:
                highest_linkage = dist

    cache[ind1][ind2] = highest_linkage
    return highest_linkage
