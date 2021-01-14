from __future__ import annotations

from typing import List, Tuple


class Cluster:
    def __init__(self, coordinates: List[float] = None, cluster_name: str = None, height: float = 0,
                 components: Tuple[Cluster, Cluster] = (None, None)):
        """

        :param coordinates: singleton cluster coordinates. None if cluster not singleton
        :param cluster_name: variable name, None if cluster is not singleton
        :param height: distance between the two component clusters. 0 for singleton clusters
        :param components: if cluster is not singleton, it's formed from another 2 clusters. None, None if singleton
        """
        self.coordinates = coordinates
        self.cluster_name = cluster_name
        self.height = height
        self.components = components

    def join_clusters(self, another_cluster: Cluster, height: float) -> Cluster:
        """
        joins current cluster with another cluster and

        :param another_cluster:
        :param height:
        :return:
        """
        return Cluster(components=(self, another_cluster), height=height)

    def __str__(self):
        if self.cluster_name is not None:
            return " ".join(map(str, self.coordinates))
        return f"({str(self.components[0])}, {str(self.components[1])})"

    def to_string(self):
        if self.cluster_name is not None:
            return self.cluster_name
        return f"({self.components[0].to_string()}, {self.components[1].to_string()})"

    def get_coordinates(self) -> List[List[float]]:
        """

        :return: all coordinates of cluster components
        """
        if self.coordinates is not None:
            return [self.coordinates]
        return self.components[1].get_coordinates() + self.components[0].get_coordinates()

