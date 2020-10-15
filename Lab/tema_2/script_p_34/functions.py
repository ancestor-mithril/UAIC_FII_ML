import math
from typing import List
import numpy as np
import scipy.stats as sp
from scipy.special import entr


def get_entropy_of_partition(m: int, partition: np.ndarray) -> float:
    """

    :param m: no. of possible values for each partition
    :param partition: list of partitions
    :return: entropy of parent of count_list
    """
    # partition_values_sum = sum(partition)
    # h_partition = 0
    # for var in partition:
    #     p_var = var / partition_values_sum
    #     h_partition += p_var * math.log2(1/p_var)
    # return h_partition
    return sp.entropy(partition, base=m)


def get_root_of_partitions(n: int, m: int, root_partitions: np.ndarray) -> np.ndarray:
    """

    :param n: number of partitions
    :param m: no. of possible event values for each partition
    :param root_partitions: n partitions of root
    :return: root
    """
    return np.sum(root_partitions, axis=0)


def get_partitions_entropy(n: int, m: int, partitions: np.ndarray) -> np.ndarray:
    """

    :param n: number of partitions
    :param m: no. of possible event values for each partition
    :param partitions: n partitions of root
    :return: list of entropies for all partitions
    """
    return np.array([get_entropy_of_partition(m, x) for x in partitions])


def get_joint_entropy(m: int, x: np.ndarray, y: np.ndarray) -> float:
    """
    :param m: no. of possible event values for each event
    :param x: event X
    :param y: event Y
    :return: H(X, Y)
    """
    return None


def get_specific_conditional_entropy(m: int, x: np.ndarray) -> float:
    """
    :param m: no. of possible event values for each event
    :param x:
    :return:
    """
    return None


def get_average_conditional_entropy(
        m: int, root: np.ndarray, partitions: np.ndarray, partitions_entropy: np.ndarray
) -> float:
    """

    :param m:
    :param root:
    :param partitions:
    :param partitions_entropy: previously calculated partitions entropy
    :return: H(root | partitions)
    """
    sum_root = root.sum()
    conditional_entropy = 0
    for i, x in enumerate(partitions):
        sum_x = x.sum()
        conditional_entropy += sum_x/sum_root * partitions_entropy[i]
    return conditional_entropy




