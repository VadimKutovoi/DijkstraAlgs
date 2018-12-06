import time
import random
import DHeap
import scripts


MAX = 1000000
matrix2 = [[MAX, 2],
           [2, MAX]]

matrix3 = [[MAX, 1, MAX],
           [1, MAX, 2],
           [MAX, 2, MAX]]

matrix4 = [[MAX, 1, MAX, 2],
           [1, MAX, 2, MAX],
           [MAX, 2, MAX, 3],
           [2, MAX, 3, MAX]]

matrix6 = [[MAX, 7, 9, MAX, MAX, 14],
           [7, 0, 10, 15, MAX, MAX],
           [9, 10, 0, 11, MAX, 2],
           [MAX, 15, 11, 0, 6, MAX],
           [MAX, MAX, MAX, 6, 0, 9],
           [14, MAX, 2, MAX, 9, 0]]

matrix11 = [[MAX, 2, 1, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
            [2, MAX, MAX, 1, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
            [1, MAX, MAX, MAX, 3, MAX, MAX, MAX, MAX, MAX, MAX],
            [MAX, MAX, MAX, 1, MAX, 2, MAX, MAX, MAX, MAX, MAX],
            [MAX, MAX, 3, MAX, 1, MAX, MAX, MAX, MAX, MAX, MAX],
            [MAX, MAX, MAX, 2, 1, MAX, 3, 4, MAX, MAX, MAX],
            [MAX, MAX, MAX, MAX, MAX, 3, MAX, MAX, 1, MAX, MAX],
            [MAX, MAX, MAX, MAX, MAX, 4, MAX, MAX, MAX, 2, MAX],
            [MAX, MAX, MAX, MAX, MAX, MAX, 1, MAX, MAX, MAX, 3],
            [MAX, MAX, MAX, MAX, MAX, MAX, 1, MAX, MAX, MAX, 1],
            [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 3, 1, MAX]]


def Dijkstra(n, s, matrix):
    # n - nodes count, s - start node
    valid = [True] * n
    weight = [1000000] * n
    weight[s] = 0
    up = []
    for i in range(n):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(n):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        up.append(ID_min_weight)
        valid[ID_min_weight] = False
    print("Path   |", up)
    return weight


def Dijkstra_Mark(n, s, matrix):
    weight = [1000000] * n
    weight[s] = 0
    h = [0] * n
    up = [0] * n
    nq = n
    while nq > 0:
        c = 0
        while h[c] != 0:
            c += 1
        i = c
        for k in range(c + 1, n):
            if h[k] == 0:
                if weight[i] > weight[k]:
                    i = k
        h[i] = 1
        nq -= 1
        p = matrix[i]
        el_i = 0
        for el in p:
            j = el_i
            if h[j] == 0:
                if weight[j] > weight[i] + el:
                    weight[j] = weight[i] + el
                    up[j] = i
            el_i += 1
    print("Path   |", up)
    return weight


def Dijkstra_DHeap(n, s, d, matrix):
    weight = [1000000] * n
    d.name = [i for i in range(0, n)]
    d.key = [1000000] * size
    d.index = [i for i in range(0, n)]
    d.key[s] = 0
    d.make()
    up = [0] * n
    while d.n >= 0:
        d.get_min()
        min_node_name = d.name1
        weight[min_node_name] = d.key1
        p = matrix[min_node_name]
        for el, value in enumerate(p):
            curr_node_pos = d.index[el]
            if d.key[curr_node_pos] > weight[min_node_name] + value:
                d.key[curr_node_pos] = weight[min_node_name] + value
                d.ascend(curr_node_pos)
                up[el] = min_node_name
    print("Path   |", up)
    return weight


random.seed("sad")
'''s = 1000
matrix_r = [[0 for x in range(s)] for y in range(s)]
for i in range(0, s):
    for j in range(0, s):
        if i == j:
            matrix_r[i][j] = MAX
        else:
            matrix_r[i][j] = random.randint(1, 10)'''

# _matrix = matrix11


_matrix = scripts.generate_matrix(5000)
size = len(_matrix)
#print(_matrix)

scripts.print_header("DIJKSTRA MARK")
time1 = time.time()
res_mark = Dijkstra_Mark(size, 0, _matrix)
print("Result |", res_mark)
print("Time   |  %s seconds" % (time.time() - time1))


scripts.print_header("DIJKSTRA D-HEAP")
dheap = DHeap.DHeap()
time1 = time.time()
res_heap = Dijkstra_DHeap(size, 0, dheap, _matrix)
time2 = time.time()
print("Result |", res_heap)
print("Time   |  %s seconds" % (time2 - time1))

scripts.print_separator()
print("Error count : ", scripts.compare_lists(res_mark, res_heap))

