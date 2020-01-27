# coding: utf-8

from gng import GrowingNeuralGas
from sklearn import datasets, metrics
import networkx as nx
import pandas as pd
import numpy as np


def evaluate():
    ds = pd.read_csv("Sales_Transactions_Dataset_Weekly.csv")
    data = ds[
        ["Normalized 0", "Normalized 1", "Normalized 2", "Normalized 3", "Normalized 4", "Normalized 5", "Normalized 6",
         "Normalized 7", "Normalized 8", "Normalized 9", "Normalized 10", "Normalized 11", "Normalized 12",
         "Normalized 13", "Normalized 14", "Normalized 15",
         "Normalized 16", "Normalized 17", "Normalized 18",
         "Normalized 19", "Normalized 20", "Normalized 21", "Normalized 22", "Normalized 23", "Normalized 24",
         "Normalized 25", "Normalized 26", "Normalized 27", "Normalized 28", "Normalized 29", "Normalized 30",
         "Normalized 31", "Normalized 32", "Normalized 33",
         "Normalized 34", "Normalized 35",
         "Normalized 36", "Normalized 37", "Normalized 38", "Normalized 39", "Normalized 40", "Normalized 41",
         "Normalized 42", "Normalized 43",
         "Normalized 44", "Normalized 45", "Normalized 46", "Normalized 47", "Normalized 48", "Normalized 49",
         "Normalized 51"
         ]]
    gng = GrowingNeuralGas(data.as_matrix(), output_folder="visualization")
    gng.fit_network(e_b=0.05, e_n=0.006, a_max=8, l=100, a=0.5, d=0.995, passes=10, plot_evolution=True)
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
    print(clusters)


if __name__ == '__main__':
    evaluate()
