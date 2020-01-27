# coding: utf-8

from gng import GrowingNeuralGas
from sklearn import datasets, metrics
import networkx as nx
import pandas as pd
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt


def evaluate(e_b, e_n, a_max, l, a, d, passes):
    ds = pd.read_csv("Sales_Transactions_Dataset_Weekly.csv")
    data = ds[
        ["W0", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10", "W11", "W12", "W13", "W14", "W15",
         "W16", "W17", "W18",
         "W19", "W20", "W21", "W22", "W23", "W24", "W25", "W26", "W27", "W28", "W29", "W30", "W31", "W32", "W33",
         "W34", "W35",
         "W36", "W37", "W38", "W39", "W40", "W41", "W42", "W43",
         "W44", "W45", "W46", "W47", "W48", "W49", "W51"
         ]]
    # plt.plot(data, label='Data')
    # plt.show()
    gng = GrowingNeuralGas(data.as_matrix(), output_folder="visualization")
    gng.fit_network(e_b=e_b, e_n=e_n, a_max=a_max, l=l, a=a, d=d, passes=passes, plot_evolution=True)
    clustered_data = gng.cluster_data()
    print('Found %d clusters.' % nx.number_connected_components(gng.network))
    target_infered = []
    for observation, cluster in clustered_data:
        target_infered.append(cluster)
    # homogeneity = metrics.homogeneity_score(data, target_infered)
    # print(homogeneity)
    gng.plot_clusters(gng.cluster_data())
    clusters = [[]]
    len = 1
    for elem in gng.cluster_data():
        if (clusters.__len__() <= elem[1]):
            for i in range(int(elem[1] + 1)):
                clusters.append([])
        clusters[int(elem[1])].append(len)
        len += 1
    ind = 0
    for clust in clusters:
        if clust.__len__() != 0:
            print('Cluster №' + str(ind) + ' size: (' + str(clust.__len__()) + ') contains data:')
            ind += 1
            print(clust)
    print('Global error all network(on euclidean distance): ' + str(gng.compute_global_error()))
    return clusters


# if __name__ == '__main__':
#     tk._test()

if __name__ == '__main__':
    evaluate()
