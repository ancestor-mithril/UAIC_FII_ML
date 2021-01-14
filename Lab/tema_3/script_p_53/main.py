import functions as f
import id3


attributes, data, output = f.read_data("train.txt")


for i, j in zip(attributes, data):
    print(i, j, sep='\t')
print(attributes[-1], output, sep='\t')


decision_tree = id3.id3(attributes, data, output)
print('\n', decision_tree.to_string(1))


f.draw_dt(decision_tree)
