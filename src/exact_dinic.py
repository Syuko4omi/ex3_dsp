from collections import deque

class Dinic:
    def __init__(self, v_num):
        self.V = v_num #頂点数
        self.G = [[] for i in range(v_num)] #各頂点についてリストがあり、要素は{向かう先,容量,向かう先のリストの何番目の要素に対応しているか}を意味する
        self.level = [0 for i in range(v_num)] #sourceから何ホップで到達できるか(bfsをやるごとに変化する)
        self.iter = [0 for i in range(v_num)]
        self.my_inf = 10**10

    def add_edge(self, from_, to, cap):
        self.G[from_].append({'to': to, 'cap': cap, 'rev': len(self.G[to])})
        self.G[to].append({'to': from_, 'cap': 0, 'rev': len(self.G[from_])-1})

    def bfs(self, s): #sから各頂点に向けた最短距離を計算
        self.level = [-1 for i in range(self.V)]
        q = deque([s])
        self.level[s] = 0
        while (len(q) != 0):
            v = q.popleft()
            for i in range(len(self.G[v])):
                ed = self.G[v][i]
                if ed['cap'] > 0 and self.level[ed['to']] < 0: #幅優先をしているはずなのでlevel(ed['to'])>0ならすでにそのノードの探索は終わっているのでスルー
                    self.level[ed['to']] = self.level[v] + 1
                    q.append(ed['to'])

    def dfs(self, v, t, f): #bfsで求めた最短経路に対して増加パスを探索
        if (v == t):
            return f
        for i in range(self.iter[v], len(self.G[v])):
            self.iter[v] = i #深さ優先して増加パスを見つけて戻ってきたとき、増加しないとわかっている経路には進まないように、探索が終わったところまでをlist.iterで保存する
            ed = self.G[v][i]
            if (ed['cap'] > 0 and self.level[v] < self.level[ed['to']]): #2本目の不等号は逆流防止
                d = self.dfs(ed['to'], t, min(f, ed['cap']))
                if d > 0:
                    ed['cap'] -= d
                    self.G[ed['to']][ed['rev']]['cap'] += d
                    return d
            #print(v, t, self.iter)
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.iter = [0 for i in range(self.V)]
            f = self.dfs(s, t, self.my_inf)
            while f > 0:
                flow += f
                f = self.dfs(s, t, self.my_inf)

#Goldberg's flow algo
def network_max_flow(edge_list, v, e): #無向グラフ,重みが全て1であるとする,頂点は0-index
    v_num = v
    e_num = e
    s = v_num #source
    t = v_num+1 #sink
    new_vertex_num = v_num+2
    lower_bound = 0
    upper_bound = e_num
    min_cut = []
    densest_val = 0

    while upper_bound-lower_bound >= 1/(v_num*(v_num-1)):
        temp_dens = (lower_bound+upper_bound)/2
        new_network = Dinic(new_vertex_num)
        for i in range(new_vertex_num):
            if i == s:
                for j in range(v_num):
                    new_network.add_edge(s, j, e_num)
            elif i == t:
                for j in range(v_num):
                    new_network.add_edge(j, t, e_num+(2*temp_dens)-len(edge_list[j]))
            else:
                for j in range(len(edge_list[i])):
                    new_network.add_edge(i, edge_list[i][j], 1)
        max_flow_val = new_network.max_flow(s, t)
        visited_list = [False for i in range(new_vertex_num)]
        visited_list[s] = True
        reachable_nodes = [] #sから辿れるノードがmin-cut
        q = deque([s])
        while len(q) != 0:
            cur = q.popleft()
            for i in range(len(new_network.G[cur])):
                temp = new_network.G[cur][i]
                if temp['cap'] > 0 and visited_list[temp['to']] == False:
                    reachable_nodes.append(temp['to'])
                    q.append(temp['to'])
                    visited_list[temp['to']] = True
        if len(reachable_nodes) == 0:
            upper_bound = temp_dens
        else:
            lower_bound = temp_dens
            min_cut = reachable_nodes
            densest_val = (lower_bound+upper_bound)/2
    min_cut.sort()
    return densest_val, min_cut



#E_l = [[1],[0,2],[1]]
#print(network_max_flow(E_l, 3, 2))

#E_l = [[1,2,3],[0,2,3],[0,1,3],[0,1,2,4],[3]]
#print(network_max_flow(E_l, 5, 7))

#E_l = [[1],[0,2,3,5,6],[1,4],[1,4,5,6],[2,3,7],[1,3,6],[1,3,5,7],[4,6,8],[7]]
#print(network_max_flow(E_l, 9, 13))

#A = Dinic(5)
#A.add_edge(0,1,10)
#A.add_edge(0,2,2)
#A.add_edge(1,2,6)
#A.add_edge(1,3,6)
#A.add_edge(2,4,5)
#A.add_edge(3,2,3)
#A.add_edge(3,4,8)
#print(A.max_flow(0, 4))

#edge_list = [[1,2,3],[4,5],[5,6],[7,8],[],[],[],[9],[9],[]]
#A = Dinic(10)
#for i in range(10):
#    for j in range(len(edge_list[i])):
#        if (i == 0 and j == 2) or (i == 3 and j == 0):
#            A.add_edge(i, edge_list[i][j], 2)
#        else:
#            A.add_edge(i, edge_list[i][j], 1)
#print(A.max_flow(0, 9))
