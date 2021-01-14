from process_input import get_data
import functions as f

(m, n), partitions = get_data()
print("Partitions: ")
print(partitions, '\n')


partitions_root = f.get_root_of_partitions(n, m, partitions)
root_entropy = f.get_entropy_of_partition(m, partitions_root)
print("Partitions root: ", partitions_root, '\n')
print("Root entropy", root_entropy, '\n')


partitions_entropy = f.get_partitions_entropy(n, m, partitions)
print("Partitions entropy", partitions_entropy, '\n')


root_conditional_entropy = f.get_average_conditional_entropy(m, partitions_root, partitions, partitions_entropy)
print("Root conditional entropy", root_conditional_entropy, '\n')


IG_root_partitions = root_entropy - root_conditional_entropy
print("Information gained", IG_root_partitions, '\n')



