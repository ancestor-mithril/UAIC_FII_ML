from typing import List
import numpy as np
import entropy as h
from dt import DecisionTree


def get_best_attribute_index(attributes: np.ndarray, data: np.ndarray, output: np.ndarray, output_set: np.ndarray,
                             data_set: np.ndarray) -> (int, List[float]):
    """
    it calculates the conditional entropy for each attribute and return the index of the minimum

    so, for each attribute, its values from data are selected

        then a conditional_entropy_parameters matrix is used to register the apparitions of each pair of (input, output)
         of current attribute

        for each value of chose attribute, we calculate its index in value set, calculate the index of its output in the
        output set, and using the two indexes we register the pair of (value, output) in conditional_entropy_parameters
        matrix

        using conditional_entropy_parameters matrix, we calculate the average conditional entropy of current attribute
        and register it, along with its partitions entropies

    we chose the index of the lowest conditional entropy, and return it along with its partitions entropies

    :param attributes: attributes name
    :param data: matrix with values for each attribute per row
    :param output: output for each column in matrix
    :param output_set: all output values
    :param data_set: all attribute values for each attribute
    :return: index of best attribute and it's partitions
    """
    output_set_len = len(output_set)
    conditional_entropies = np.zeros(len(data))
    partitions_entropies = []
    for row_index, row in enumerate(data):
        conditional_entropy_parameters = np.array([np.zeros(output_set_len) for x in data_set[row_index]])
        for index_of_value in range(len(row)):
            c_e_p_index = np.where(data_set[row_index] == row[index_of_value])[0][0]
            c_output_index = np.where(output_set == output[index_of_value])[0][0]
            conditional_entropy_parameters[c_e_p_index, c_output_index] += 1
        conditional_entropies[row_index], x = h.get_conditional_entropy(conditional_entropy_parameters)
        partitions_entropies.append(x.tolist())

    index = np.where(conditional_entropies == np.amin(conditional_entropies))[0][0]

    # print("Best attribute: ", attributes[index], " from ", attributes[:-1], ", with partition = ",
    #       partitions_entropies[index])
    return index, partitions_entropies[index]


def id3(attributes: np.ndarray, data: np.ndarray, output: np.ndarray) -> DecisionTree:
    """
    ID3 algorithm implementation. Creates decision tree.

    :param attributes: array of column names
    :param data: array of data for each attribute
    :param output: array of output for each row
    :return: the decision tree resulted
    """
    output_set = np.array(list(set(output)))
    node_index = 0

    def create_decision_tree(
            local_attributes: np.ndarray,
            local_data: np.ndarray,
            local_output: np.ndarray,
    ) -> DecisionTree:
        """
        in each recursion, we calculate for each remaining attribute a list of unique possible values this iteration.

        from the remainder attributes, we choose the best attribute with the lowest average conditional entropy and
        we get its index and partition entropies

        we create the Node associated to this attribute, and after that,
        for each partition of chosen best node
            we get the value of attribute in current partition
            if partition entropy is 0 => for each value of partition, we have the same output
                we get the output for partition, and create a terminal node, a leaf, with value equal to output of
                partition value
            else
                we filter each other attribute and also the output, so that we only have elements which can be
                descendents of current partition value
                we calculate "data", "attributes", and "output" for a future recursion
                if no further recursion is possible (we have no other attribute to be chosen next)
                    we create a leaf with entropy, and value = count of each output apparition for current partition
                    value
                else
                    we recursively calculate the child of current partition and append it to chosen best node children




        :param local_attributes: array of column names
        :param local_data: array of data for each attribute
        :param local_output: array of output for each row
        :return: a Node in tree along with its children
        """
        nonlocal output_set
        nonlocal node_index
        possible_values_for_attribute = np.array([np.array(list(set(x))) for x in local_data], dtype=object)

        current_best_attribute_index, node_values = get_best_attribute_index(
            local_attributes, local_data, local_output, output_set, possible_values_for_attribute
        )
        current_node = DecisionTree(value=local_attributes[current_best_attribute_index], node_id=node_index)
        node_index += 1

        for i, v in enumerate(node_values):
            specific_condition = possible_values_for_attribute[current_best_attribute_index][i]
            if node_values[i] == 0:
                for value in range(len(local_data[current_best_attribute_index])):
                    if local_data[current_best_attribute_index][value] == specific_condition:
                        node_output = local_output[value]

                child = DecisionTree(node_id=node_index, value=node_output, is_leaf=True,
                                     parent_edge=specific_condition, parent=current_node.node_id,
                                     parent_value=current_node.value)
                node_index += 1
            else:
                filter_array = []
                for value in local_data[current_best_attribute_index]:
                    if value == specific_condition:
                        filter_array.append(True)
                    else:
                        filter_array.append(False)
                future_attributes = np.copy(local_attributes)
                future_attributes = np.delete(future_attributes, obj=current_best_attribute_index, axis=0)
                future_data = np.copy(local_data)
                future_data = np.delete(future_data, obj=current_best_attribute_index, axis=0)
                aux = []
                for future_row in range(len(future_data)):
                    aux.append(future_data[future_row][filter_array])
                future_data = np.array(aux)
                future_output = np.copy(local_output)[filter_array]
                if len(future_attributes) == 1:
                    unique, counts = np.unique(future_output, return_counts=True)
                    value = str(dict(zip(unique, counts)))
                    child = DecisionTree(node_id=node_index, is_leaf=True, value=value,
                                         parent_edge=specific_condition, parent=current_node.node_id,
                                         parent_value=current_node.value)
                    node_index += 1
                else:
                    child = create_decision_tree(
                        future_attributes, future_data, future_output
                    )
                    child.parent_edge = specific_condition
                    child.parent = current_node.node_id
                    child.parent_value = current_node.value
            current_node.add_children(child)
        return current_node

    tree = create_decision_tree(attributes, data, output)
    return tree
