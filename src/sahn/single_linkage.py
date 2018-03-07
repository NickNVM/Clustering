import math
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv


def main():
    x = []
    y = []
    c = []

    with open('../../data/small.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in spamreader:
            y.append(int(row[0]))
            x.append(int(row[1]))
            c.append([i])
            i += 1

    cache = [{}] * len(c)

    for i in range(len(c)):
        cache[i] = {}

    for i in range(len(c) - 3):
        print(i)
        cluster_iteration(c, x, y, cache)

    print(c)
    display(x, y, c, "../../out/" + str(i) + ".png")


def display(x, y, c, name):
    color = 60
    colors = [None] * len(x)
    for cluster in c:
        color += 60;
        if len(cluster) > 1:
            current = color
        else:
            current = 0
        for index in cluster:
            colors[index] = current;

    fig = plt.figure(num=None, figsize=(5, 5))
    plt.scatter(x, y, c=colors)
    plt.show(name)
    plt.close(fig)


def cluster_iteration(cluster, x_coord, y_coord, cache):
    smallest_distance_pair = [-1, -1]
    smallest_dist = -1

    for i1 in range(0, len(cluster)):
        if len(cluster[i1]) != 0:
            for i2 in range(0, len(cluster)):
                if len(cluster[i2]) != 0 and i1 != i2:
                    dist = cluster_distance(cluster, i1, i2, x_coord, y_coord, cache)
                    if smallest_dist == -1 or dist < smallest_dist:
                        smallest_dist = dist
                        smallest_distance_pair[0] = i1
                        smallest_distance_pair[1] = i2

    merge_cluster(cluster, smallest_distance_pair[0], smallest_distance_pair[1], cache)


def merge_cluster(cluster, i1, i2, cache):
    c1 = cluster[i1]
    c2 = cluster[i2]

    for cluster in c2:
        c1.append(cluster)

    if i2 in cache[i1]:
        del cache[i1][i2]

    del c2[:]


def cluster_distance(cluster, ind1, ind2, x_coord, y_coord, cache):
    # if ind2 in cache[ind1]:
    #   return cache[ind1][ind2]

    c1 = cluster[ind1]
    c2 = cluster[ind2]
    smallest_dist = -1

    for i1 in c1:
        for i2 in c2:
            dist = distance(x_coord[i1], y_coord[i1], x_coord[i2], y_coord[i2])
            if smallest_dist == -1 or dist < smallest_dist:
                smallest_dist = dist

    # cache[ind1][ind2] = smallest_dist
    return smallest_dist


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


if __name__ == "__main__":
    main()
