import functions as f

attributes, data, output = f.read_data("train.txt")
# TODO: implement reading data with "Counts" value
conditional_probabilities = f.calculate_conditional_probabilities(attributes, data, output)
print(conditional_probabilities)
