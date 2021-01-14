class DecisionTree(object):
    def __init__(self, node_id: int, value: str = "", is_leaf: bool = False, children: list = None,
                 parent_value: str = None, parent: int = None, parent_edge: str = None):
        """

        :param node_id: int | should be unique id in tree
        :param value: str | usually name of chosen attribute, or output if is_leaf = True
        :param is_leaf: bool | checked if node is terminal
        :param children: list | list containing all direct descendants of current node
        :param parent_value: str | name of parent attribute
        :param parent: int | should be parent unique id
        :param parent_edge: str | value of parent attribute edge
        """
        if children is None:
            children = []
        self.value = value
        self.is_leaf = is_leaf
        self.children = children
        self.node_id = node_id
        self.parent_value = parent_value
        self.parent = parent
        self.parent_edge = parent_edge

    def add_children(self, new_node: "DecisionTree"):
        self.children.append(new_node)

    def to_string(self, tabs: int):
        string = "\t" * (tabs - 1)
        if self.parent_edge is not None:
            string += self.parent_edge + "\t"
        string += "\tNode: " + str(self.node_id) + " with value = " + str(self.value) + " is leaf = " + str(
            self.is_leaf) + "\n"
        if len(self.children) > 0:
            string += "\t" * tabs + "Node " + str(self.node_id) + " has " + str(len(self.children)) + " child nodes:\n"
            for i in self.children:
                string += i.to_string(tabs + 1) + "\n"
        return string
