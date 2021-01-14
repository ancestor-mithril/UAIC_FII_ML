import numpy as np
import scipy.stats as sp


def get_entropy_of_partition(m: int, partition: np.ndarray) -> float:
    """

    :param m: no. of possible values for each partition
    :param partition: list of partitions
    :return: entropy of partition
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


def get_average_conditional_entropy(m: int, root: np.ndarray, partitions: np.ndarray,
                                    partitions_entropy: np.ndarray) -> float:
    """

    :param m:
    :param root:
    :param partitions:
    :param partitions_entropy: previously calculated entropies foe each partitions
    :return: H(root | partitions)
    """
    sum_root = root.sum()
    conditional_entropy = 0
    for i, x in enumerate(partitions):
        sum_x = x.sum()
        conditional_entropy += sum_x / sum_root * partitions_entropy[i]
    return conditional_entropy


def get_conditional_entropy(conditional_entropy_parameters: np.ndarray) -> (float, np.ndarray):
    """

    :param conditional_entropy_parameters: array of partitions
    :return: average conditional entropy
    """
    root = get_root_of_partitions(len(conditional_entropy_parameters), len(conditional_entropy_parameters[0]),
                                  conditional_entropy_parameters)
    partitions_entropies = np.array([get_entropy_of_partition(len(x), x) for x in conditional_entropy_parameters])
    return get_average_conditional_entropy(len(conditional_entropy_parameters[0]), root, conditional_entropy_parameters,
                                           partitions_entropies), partitions_entropies
