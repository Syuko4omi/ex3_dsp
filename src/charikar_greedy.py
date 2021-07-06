import bisect

class node:
    def __init__(self, prev, next, removed):
        self.prev = prev
        self.next = next
        self.removed = removed

def naive_greedy(edge_list, v, e):
    L = []
    p = v
    q = 2*v+1
    deg_list = [len(edge_list[i]) for i in range(v)]
    for i in range(3*v+2):
        new_node = node(-1, -1, False)
        L.append(new_node)
    for i in range(v+1):
        L[p+i].next = q+i
        L[q+i].prev = p+i
    for i in range(v):
        d_num = deg_list[i]
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
        deg_list[removing_node] = 0
        next = L[removing_node].next
        L[p+scan_deg].next = next
        L[next].prev = p+scan_deg
        L[removing_node].prev = -1
        L[removing_node].next = -1
        L[removing_node].removed = True
        set_of_node.discard(removing_node)
        for j in range(len(edge_list[removing_node])):
            adj_node = edge_list[removing_node][j]
            if L[adj_node].removed == True:
                continue
            prev = L[adj_node].prev
            next = L[adj_node].next
            L[prev].next = next
            L[next].prev = prev
            new_deg = deg_list[adj_node]-1
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
    return max_density, densest_subgraph


#print(naive_greedy([[1],[0,2],[1]], 3,2))
#print(naive_greedy([[1],[0,2,3,5,6],[1,4],[1,4,5,6],[2,3,7],[1,3,6],[1,3,5,7],[4,6,8],[7]], 9, 13))
