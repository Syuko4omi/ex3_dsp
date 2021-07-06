import copy
import matplotlib.pyplot as plt
import numpy as np

class node:
    def __init__(self, prev, next, removed):
        self.prev = prev
        self.next = next
        self.removed = removed

def show_list(L):
    for i in range(len(L)):
        print(L[i].prev, L[i].next, L[i].removed)

def iterative_greedy(edge_list, deg_l, v, e, weight_vec, T): #T=1からスタート
    L = []
    p = v
    q = (1+T)*v+1
    deg_list = copy.deepcopy(deg_l)
    weight_list = weight_vec

    ret_load_vec = copy.deepcopy(weight_vec)
    for i in range((1+2*T)*v+2):
        new_node = node(-1, -1, False)
        L.append(new_node)
    for i in range(T*v+1):
        L[p+i].next = q+i
        L[q+i].prev = p+i
    for i in range(v):
        d_num = weight_list[i]+deg_list[i]
        x = p+d_num
        y = L[x].next
        L[x].next = i
        L[i].prev = x
        L[i].next = y
        L[y].prev = i

    scan_deg = 0
    remaining_vertex = v
    remaining_edge = e
    max_density = e/v
    densest_subgraph = [i for i in range(v)]
    set_of_node = {i for i in range(v)}
    for i in range(v):
        remaining_vertex -= 1
        if scan_deg > 0:
            scan_deg -= 1
        while L[p+scan_deg].next == q+scan_deg:
            scan_deg += 1
        removing_node = L[p+scan_deg].next
        deg_h_u = deg_list[removing_node]
        ret_load_vec[removing_node] += deg_h_u
        deg_list[removing_node] = 0
        #print(removing_node, deg_list)
        #show_list(L)
        next_ = L[removing_node].next
        L[p+scan_deg].next = next_
        L[next_].prev = p+scan_deg
        L[removing_node].prev = -1
        L[removing_node].next = -1
        L[removing_node].removed = True
        set_of_node.discard(removing_node)
        for j in range(len(edge_list[removing_node])):
            adj_node = edge_list[removing_node][j]
            if L[adj_node].removed == True:
                continue
            prev_ = L[adj_node].prev
            next_ = L[adj_node].next
            L[prev_].next = next_
            L[next_].prev = prev_
            new_deg = weight_list[adj_node]+deg_list[adj_node]-1
            deg_list[adj_node] -= 1
            new_prev = p+new_deg
            new_next = L[p+new_deg].next
            L[new_prev].next = adj_node
            L[adj_node].prev = new_prev
            L[adj_node].next = new_next
            L[new_next].prev = adj_node
            remaining_edge -= 1
        if remaining_vertex > 0:
            if remaining_edge/remaining_vertex > max_density:
                max_density = remaining_edge/remaining_vertex
                densest_subgraph = list(set_of_node)
        #print(remaining_edge, remaining_vertex)
    #print(ret_load_vec, max_density, densest_subgraph)
    return max_density, densest_subgraph, ret_load_vec

def greedy_pp(T, edge_list, v, e):
    history_of_density = []
    #test2
    temporal_max_density = []
    #test2
    deg_list = [len(edge_list[i]) for i in range(v)]
    max_density = 0
    densest_subgraph = []
    weight_vec = [0 for i in range(v)]

    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax1.set_title('degree distribution')
    ax1.set_xlabel('degree')
    ax1.set_ylabel('freq')
    plt.yscale('log')
    plt.hist(deg_list, bins = 100)

    detected_subgraph = []
    for i in range(T):
        print("iteration:", i+1)
        temp_max_density, temp_densest_subgraph, weight_vec = iterative_greedy(edge_list, deg_list, v, e, weight_vec, i+1)
        #test 2
        if len(detected_subgraph) == 0:
            detected_subgraph.append([[i+1], temp_max_density, temp_densest_subgraph])
        else:
            flag = False
            for j in range(len(detected_subgraph)):
                if detected_subgraph[j][2] == temp_densest_subgraph:
                    detected_subgraph[j][0].append(i+1)
                    flag = True
                    break
            if flag == False:
                detected_subgraph.append([[i+1], temp_max_density, temp_densest_subgraph])
        temporal_max_density.append(temp_max_density)
        #test 2
        if max_density < temp_max_density:
            max_density = temp_max_density
            densest_subgraph = temp_densest_subgraph
        history_of_density.append(max_density)
    #test2
    #print(detected_subgraph)
    #print("********************************")

    #x_axis = np.array([i+1 for i in range(20)])
    #plt.plot(x_axis, np.array(history_of_density)/max(history_of_density), linewidth = 4, color = "red")
    #plt.plot(x_axis, np.array(temporal_max_density)/max(history_of_density), "blue", linestyle="dashed")
    #plt.xlabel("iterations")
    #plt.ylabel("approx ratio")
    #plt.show()
    #test2

    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    #test3 degree_dist, weight_dist
    #L_L = [45, 46, 570, 773, 1653, 2212, 2741, 2952, 3372, 4164, 4511, 4513, 6179, 6610, 6830, 7956, 8879, 9785, 11241, 11472, 12365, 12496, 12781, 12851, 14540, 14807, 15003, 15659, 17655, 17692, 18894, 19423, 19961, 20108, 20562, 20635, 21012, 21281, 21508, 21847, 22691, 22887, 23293, 24955, 25346, 25758]
    #weight_L_L = []
    #deg_L_L = []
    #for i in range(len(L_L)):
        #weight_L_L.append(weight_vec[L_L[i]])
        #deg_L_L.append([deg_list[L_L[i]], L_L[i]])

    #deg_L_L.sort()
    #deg_L_L.reverse()

    ax2 = fig.add_subplot(1,2,2)
    ax2.set_title('weight distribution')
    ax2.set_xlabel('weight')
    ax2.set_ylabel('freq')
    plt.yscale('log')
    ax2.hist(weight_vec, bins = 300)
    plt.show()

    #print(weight_L_L)
    #print(deg_L_L)
    #test3
    return max_density, densest_subgraph, history_of_density

    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    

#print(naive_greedy([[1],[0,2],[1]], 3,2))
#print(naive_greedy([[1],[0,2,3,5,6],[1,4],[1,4,5,6],[2,3,7],[1,3,6],[1,3,5,7],[4,6,8],[7]], 9, 13))

#print(greedy_pp(2, [[1],[0,2],[1]], 3, 2))
#print(greedy_pp(15, [[1],[0,2,3,5,6],[1,4],[1,4,5,6],[2,3,7],[1,3,6],[1,3,5,7],[4,6,8],[7]], 9, 13))
