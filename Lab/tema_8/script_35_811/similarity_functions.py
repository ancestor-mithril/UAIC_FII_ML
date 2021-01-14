from typing import List
import numpy as np
from cluster import Cluster
from scipy.spatial import distance


def single_linkage(line_1: np.ndarray, line_2: np.ndarray, column_1: np.ndarray, column_2: np.ndarray) -> List[float]:
    """

    :param line_1:
    :param line_2:
    :param column_1:
    :param column_2:

    :return: the new column to be added to matrix
    """
    new_column = [0]
    i = 0
    while line_1[i] != 0 and line_2[i] != 0:
        new_column.append(min(line_1[i], line_2[i]))
        i += 1
    for j in range(i, len(column_1)):
        if column_1[j] != 0 and column_2[j] != 0:
            new_column.append(min(column_1[j], column_2[j]))
    for i in range(len(column_1) - len(new_column) - 1):
        new_column.append(0)
    return new_column


def complete_linkage(line_1: np.ndarray, line_2: np.ndarray, column_1: np.ndarray, column_2: np.ndarray) -> List[float]:
    """

    :param line_1:
    :param line_2:
    :param column_1:
    :param column_2:
    :return: the new column to be added to matrix
    """
    new_column = [0]
    i = 0
    while line_1[i] != 0 and line_2[i] != 0:
        new_column.append(max(line_1[i], line_2[i]))
        i += 1
    for j in range(i, len(column_1)):
        if column_1[j] != 0 and column_2[j] != 0:
            new_column.append(max(column_1[j], column_2[j]))
    for i in range(len(column_1) - len(new_column) - 1):
        new_column.append(0)
    return new_column


def average_linkage(line_1: np.ndarray, line_2: np.ndarray, column_1: np.ndarray, column_2: np.ndarray) -> List[float]:
    """

    :param line_1:
    :param line_2:
    :param column_1:
    :param column_2:
    :return: the new column to be added to matrix
    """
    raise NotImplementedError("Inca nu e implementata")


def ward_linkage(line_1: np.ndarray, line_2: np.ndarray, column_1: np.ndarray, column_2: np.ndarray) -> List[float]:
    """

    :param line_1:
    :param line_2:
    :param column_1:
    :param column_2:
    :return: the new column to be added to matrix
    """
    raise NotImplementedError("Inca nu e implementata")
