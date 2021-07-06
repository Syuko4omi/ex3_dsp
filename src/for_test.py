import exact_dinic
import charikar_greedy
import greedy_pp
import pickle

print("file name:")
file_name = input()

Graph = []
with open(file_name, "rb") as f:
    Graph = pickle.load(f)

length_graph = len(Graph)
edge_num = 0
ver_num = 0
for i in range(length_graph): #実際の頂点と辺の数を再計算
    t = len(Graph[i])
    if t != 0:
        ver_num += 1
        edge_num += t

edge_num //= 2

print("nodes:", ver_num, "edges:", edge_num)
print("*****")
print(exact_dinic.network_max_flow(Graph, length_graph, edge_num))
print("***")
#print(charikar_greedy.naive_greedy(Graph, length_graph, edge_num))
#print("***")
print(greedy_pp.greedy_pp(20, Graph, length_graph, edge_num))
