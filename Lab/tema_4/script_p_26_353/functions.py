import numpy as np


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


def calculate_conditional_probabilities(attributes: np.ndarray, data: np.ndarray, output: np.ndarray) -> dict:
    """
    for each unique output value, for each attribute, we check the apparition of each unique attribute value and
    compute it's probability

    :param attributes:
    :param data:
    :param output:
    :return: dictionary with each attribute values conditional probability
    """
    conditional_probabilities = dict()
    for i in attributes:
        conditional_probabilities[i] = dict()

    output_set = set(output)
    for index, atr in enumerate(data):
        for output_value in output_set:
            conditional_probabilities[attributes[index]][output_value] = 0.0
            filter_array = []
            for i in output:
                if i == output_value:
                    filter_array.append(True)
                else:
                    filter_array.append(False)
            attribute_values_for_output = list(atr[filter_array])
            for i in set(attribute_values_for_output):
                conditional_probabilities[attributes[index]][output_value] = float(
                    attribute_values_for_output.count(i) / len(attribute_values_for_output)
                )
    conditional_probabilities[attributes[-1]] = dict()
    output = list(output)
    for i in output_set:
        conditional_probabilities[attributes[-1]][i] = float(output.count(i) / len(output))
    return conditional_probabilities
