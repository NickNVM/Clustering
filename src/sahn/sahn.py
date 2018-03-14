import matplotlib
import complete_linkage as linkage

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv


def main():
    x = []
    y = []
    c = []

    with open('../../data/smallset.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in spamreader:
            y.append(int(row[0]))
            x.append(int(row[1]))
            c.append([i])
            i += 1

    execute(x, y, c, 3, True)


def execute(x, y, c, count_cluster, save):
    cache = [{}] * len(c)

    for i in range(len(c)):
        cache[i] = {}

    for i in range(len(c) - count_cluster):
        print(str(i + 1) + " / " + str(len(c) - count_cluster))
        cluster_iteration(c, x, y, cache)

        if save:
            display(x, y, c, "../../out/" + str(i) + ".png", True)

    display(x, y, c, "../../out/" + str(i) + ".png", False)
    plt.show()


def display(x, y, c, name, save):
    color = 0
    colors = [None] * len(x)
    for cluster in c:
        if len(cluster) > 1:
            color += 1
            current = color
        else:
            current = 0
        for index in cluster:
            colors[index] = current

    fig = plt.figure(num=None, figsize=(5, 5))
    plt.scatter(x, y, c=colors, s=200)
    if save:
        plt.savefig(name)
    else:
        plt.show(name)
    plt.close(fig)


def cluster_iteration(cluster, x_coord, y_coord, cache):
    smallest_distance_pair = [-1, -1]
    smallest_dist = -1

    for i1 in range(0, len(cluster)):
        if len(cluster[i1]) != 0:
            for i2 in range(i1, len(cluster)):
                if len(cluster[i2]) != 0 and i1 != i2:
                    dist = linkage.cluster_distance(cluster, i1, i2, x_coord, y_coord, cache)
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


if __name__ == "__main__":
    main()
