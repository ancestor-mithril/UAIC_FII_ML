import numpy as np
import pygraphviz as pgv
from dt import DecisionTree
import subprocess
from PIL import Image


def read_data(file: str) -> (np.ndarray, np.ndarray, np.ndarray):
    """
    reads SSV data from file. First row = attribute names, last value each row = output label for row data

    :param file: str
    :return: array of attribute names, matrix of data, labels for data
    """
    with open(file, "r") as fd:
        lines = fd.readlines()
    data = np.array([x.split() for x in lines[1:]]).T
    return np.array(lines[0].split()), data[:-1], data[-1:][0]


def draw_dt(tree: DecisionTree):
    """
    Creates dot graph in decision_tree.dot, and using dot.exe creates decision_tree.png and shows it

    :param tree: the Decision tree to be drawn
    :return:
    """
    graph = pgv.AGraph()

    def dfs(node: DecisionTree):
        """
        recursively visiting tree using depth first search algorithm

        :param node: current visited node
        :return:
        """
        nonlocal graph
        graph.add_node(str(node.node_id), label=node.value)
        if node.parent is not None:
            graph.add_edge(str(node.parent), str(node.node_id),
                           label=node.parent_edge)
        for i in node.children:
            dfs(i)

    dfs(tree)
    print(graph.string())
    open("decision_tree.dot", "w").write(graph.string())
    p1 = subprocess.Popen(["dot.exe", "-Tpng", "decision_tree.dot", "-o", "decision_tree.png"])
    p1.wait()
    image = Image.open("decision_tree.png")
    image.show()
