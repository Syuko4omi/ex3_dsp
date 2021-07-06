import numpy as np
import matplotlib.pyplot as plt

def jaccard_similarity_coefficient(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    set_intersection = set.intersection(set_a, set_b)
    num_of_intersection = len(set_intersection)
    set_union = set.union(set_a, set_b)
    num_of_union = len(set_union)

    if num_of_union == 0:
        return 1.0
    else:
        return num_of_intersection/num_of_union

optimal = [] #最密グラフの頂点集合が入る
found_graph_list = []

for i in range(20):
    for j in range(len(found_graph_list)):
        if i+1 in found_graph_list[j][0]:
            L.append(jaccard_similarity_coefficient(optimal, found_graph_list[j][2]))
fig = plt.figure()
ax2 = fig.add_subplot(1,1,1)
ax2.set_xlabel('iteration')
ax2.set_ylabel('jaccard similarity coefficient')
plt.plot([i+1 for i in range(20)], np.array(L))
plt.show()
