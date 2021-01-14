import os
from typing import List
from cluster import Cluster
from utils import CustomError
from scipy.spatial import distance


def compute_euclidean_distance(c_1: List[float], c_2: List[float]) -> float:
    """

    :param c_1: a vector of coordinates
    :param c_2: a vector of coordinates
    :return: the distance between the two vectors
    """
    return distance.euclidean(c_1, c_2)


def get_data(input_file: str) -> List[Cluster]:
    """

    :param input_file: path to the input file
    :return: a list of clusters consisting of single points
    """
    assert os.path.isfile(input_file), "Given path is not a file"
    clusters = []
    i = 0
    with open(input_file, "r") as fp:
        lines = fp.readlines()
        for line in lines:
            try:
                coordinates = list(map(float, line.split()))
            except ValueError:
                raise CustomError("Input values must be float or integers")
            clusters.append(Cluster(coordinates=coordinates, cluster_name=f"x{i}"))
            i += 1
    return clusters
