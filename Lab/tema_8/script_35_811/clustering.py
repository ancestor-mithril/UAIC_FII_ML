from typing import List, Tuple
from cluster import Cluster
from functions import get_data, compute_euclidean_distance
import numpy as np

from similarity_functions import single_linkage, complete_linkage, average_linkage, ward_linkage

functions = {
    "-single-linkage": single_linkage,
    "-complete-linkage": complete_linkage,
    "-average-linkage": average_linkage,
    "-ward-linkage": ward_linkage
}


def prepare_clustering(input_file: str, similarity_function: str, all_solutions: bool = False):
    """

    :param input_file: path to the input file
    :param similarity_function: the similarity function to be applied; must be one of the following:
                                -single-linkage, -complete-linkage, -average-linkage or -ward-linkage
    :param all_solutions: True if script is intended to return all possible solutions
    :return: void
    """
    cluster_list = get_data(input_file)
    distance_matrix = compute_distance_matrix(cluster_list)
    matrix_update_function = functions[similarity_function]
    bottom_up(cluster_list, distance_matrix, matrix_update_function, all_solutions)


def compute_distance_matrix(cluster_list: List[Cluster]) -> np.ndarray:
    """

    :param cluster_list: a list of singleton clusters
    :return: the distance matrix
    """
    distance_matrix = np.zeros((len(cluster_list), len(cluster_list) + 2))
    for i in range(len(cluster_list)):
        for j in range(i):
            v_1 = cluster_list[i].get_coordinates()[0]
            v_2 = cluster_list[j].get_coordinates()[0]
            distance_matrix[i, j] = compute_euclidean_distance(v_1, v_2)
        distance_matrix[i, i] = 0
    return distance_matrix


def bottom_up(cluster_list: List[Cluster], distance_matrix: np.ndarray, matrix_update_function: callable,
              all_solutions: bool = False):
    """

    :param cluster_list: a list of clusters
    :param distance_matrix: the distance matrix between clusters
    :param matrix_update_function: the update method to be applied on matrix on each iteration
    :param all_solutions: True, if script is required to print all solutions; False otherwise
    :return: void
    """
    while len(cluster_list) > 1:
        indexes = get_best_indexes(distance_matrix)
        if all_solutions:
            for i, j in indexes:
                c_list, d_matrix = compute_changes(cluster_list, distance_matrix, matrix_update_function, i, j)
                bottom_up(c_list, d_matrix, matrix_update_function, all_solutions)
            return
        else:
            i, j = indexes[0]
            cluster_list, distance_matrix = compute_changes(cluster_list, distance_matrix, matrix_update_function,
                                                            i, j)
    print(cluster_list[0].to_string())


def get_best_indexes(distance_matrix: np.ndarray) -> List[Tuple[int, int]]:
    """

    :param distance_matrix: the distance matrix between clusters
    :return: a list indexes with the least distance
    """
    minimum_indexes = []
    minimum = distance_matrix[1, 0]
    for i in range(distance_matrix.shape[0]):
        for j in range(i):
            if distance_matrix[i, j] < minimum:
                minimum = distance_matrix[i, j]
                minimum_indexes = [(i, j)]
            elif distance_matrix[i, j] == minimum:
                minimum_indexes.append((i, j))
    return minimum_indexes


def compute_changes(cluster_list: List[Cluster], distance_matrix: np.ndarray, matrix_update_function: callable,
                    index_1: int, index_2: int) -> (List[Cluster], np.ndarray):
    """

    :param cluster_list: the cluster list which has to be modified
    :param distance_matrix: the distance matrix which has to be updated
    :param matrix_update_function: the function to be called to update the matrix
    :param index_1: the index of the first cluster to be joined
    :param index_2: the index of the second cluster to be joined
    :return: the new cluster list and distance matrix
    """
    line_1 = distance_matrix[index_1]
    line_2 = distance_matrix[index_2]
    column_1 = distance_matrix[:, index_1]
    column_2 = distance_matrix[:, index_2]

    new_distance = np.delete(np.delete(np.delete(np.delete(distance_matrix, index_1, 0), index_2, 0), index_1, 1),
                             index_2, 1)
    new_column = matrix_update_function(line_1, line_2, column_1, column_2)
    new_distance = np.vstack([[0 for z in range(new_distance.shape[1])], new_distance])
    new_distance = np.hstack([[[x] for x in new_column], new_distance])

    new_cluster = cluster_list[index_1].join_clusters(cluster_list[index_2], height=distance_matrix[index_1, index_2])

    cluster_list.pop(index_1)
    cluster_list.pop(index_2)
    return [new_cluster] + cluster_list, new_distance
