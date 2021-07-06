import re
import os
import pickle

print("file name:")
file_name = input()
ver_num = 3000 #頂点数
edge_num = 0
G = []
Graph = []

#重みなし無向グラフについて
#1行目から辺が張られている頂点が一行ずつ書かれている
#辺はa bとb aが両方書いてあっても、片方しか書いてなくてもOK

def cut_off(li): #リストの空の部分を削除
    k = 0
    for i in range(len(li)-1, -1, -1):
        if len(li[i]) != 0:
            k = i
            break
    return li[:k+1]

G = [[0 for i in range(ver_num)] for j in range(ver_num)]
for line in open (file_name, 'r'):
    str_item = line.rstrip(os.linesep)
    L = list(map(int, re.split('\s', str_item)))
    if len(L) == 2 and L[0] != L[1]: #自己ループは削除,多重辺は1本にする
        G[L[0]][L[1]] = 1
        G[L[1]][L[0]] = 1

for i in range(ver_num):
    temp = []
    for j in range(ver_num):
        if G[i][j] == 1:
            temp.append(j)
            edge_num += 1
    Graph.append(temp)
edge_num //= 2

new_graph = cut_off(Graph)
new_file_name = file_name[:len(file_name)-4]+'_list_style.txt'
with open(new_file_name, 'wb') as f:
    pickle.dump(new_graph, f)
print(new_graph, len(new_graph), edge_num)
