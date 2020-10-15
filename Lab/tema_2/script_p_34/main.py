from process_input import get_data
import functions as f

(m, n), partitions = get_data()
print(partitions)


partitions_root = f.get_root_of_partitions(n, m, partitions)
root_entropy = f.get_entropy_of_partition(m, partitions_root)
print(partitions_root, root_entropy)


partitions_entropy = f.get_partitions_entropy(n, m, partitions)
print(partitions_entropy)


root_conditional_entropy = f.get_average_conditional_entropy(m, partitions_root, partitions, partitions_entropy)
print(root_conditional_entropy)


IG_root_partitions = root_entropy - root_conditional_entropy
print(IG_root_partitions)



