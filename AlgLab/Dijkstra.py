import time
import random



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
    up = []
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
            el_i += 1
        up.append(i)
    print("Path   |", up)
    return weight


class DHeap:
    key = []
    name = []
    index = []
    len = int()
    d = int()
    n = int()
    name1 = int()
    key1 = int()

    def __init__(self, d_=3):
        self.d = d_

    def ascend(self, i):
        key0 = self.key[i]
        name0 = self.name[i]

        p = self.father(i)
        while i != 0 and (self.key[p] > key0):
            self.key[i] = self.key[p]
            self.name[i] = self.name[p]
            self.index[self.name[i]] = i
            i = p
            p = self.father(i)
        self.key[i] = key0
        self.name[i] = name0
        self.index[self.name[i]] = i

    def min_child(self, i):
        min_child = int()
        min_key = int()
        kf = self.first_child(i)
        if kf == 0:
            return i
        else:
            kl = self.last_child(i)
            min_key = self.key[kf]
            min_child = kf
            for j in range(kf, kl + 1):
                if self.key[j] < min_key:
                    min_key = self.key[j]
                    min_child = j
        return min_child

    def first_child(self, i):
        #n = self.len
        n = self.n
        first_child = i * self.d + 1
        if first_child > n:
            return 0
        else:
            return first_child

    def last_child(self, i):
        #n = self.len - 1
        n = self.n
        first_child = self.first_child(i)
        if first_child == 0:
            return 0

        else:
            return min(first_child + self.d - 1, n)

    def father(self, i):
        return (i - 1) // self.d

    def descend(self, i):
        key0 = self.key[i]
        name0 = self.name[i]

        s = self.min_child(i)
        while s != i and key0 > self.key[s]:
            self.key[i] = self.key[s]
            self.name[i] = self.name[s]
            self.index[self.name[i]] = i
            i = s
            s = self.min_child(i)
        self.key[i] = key0
        self.name[i] = name0
        self.index[self.name[i]] = i

    def get_min(self):
        n = self.n
        self.name1 = self.name[0]
        self.key1 = self.key[0]
        self.name[0] = self.name[n]
        self.key[0] = self.key[n]
        self.name[n] = self.name1
        self.key[n] = self.key1
        self.index[0], self.index[n] = self.index[n], self.index[0]
        self.n = n - 1

        if self.n > 0:
            self.descend(0)

    def make(self):
        self.len = len(self.name)
        self.n = self.len - 1
        n = self.n
        while n >= 0:
            self.descend(n)
            n -= 1


def Dijkstra_DHeap(n, s, d, matrix):
    weight = [1000000] * n
    d.name = [i for i in range(0, n)]
    d.key = [1000000] * size
    d.index = [i for i in range(0, n)]
    d.key[s] = 0
    d.make()
    up = []
    while d.n >= 0:
        d.get_min()
        min_node_name = d.name1
        weight[min_node_name] = d.key1
        p = matrix[min_node_name]
        for el, value in enumerate(p):
            curr_node_pos = d.name.index(el)
            if d.key[curr_node_pos] > weight[min_node_name] + value:
                d.key[curr_node_pos] = weight[min_node_name] + value
                d.ascend(curr_node_pos)
        up.append(min_node_name)
    print(d.name)
    print(d.key)
    print(d.index)
    print("Key ", d.key)
    print("Path   |", up)
    return weight


def print_header(name):
    line = "-" * 46
    print(line)
    print(" " * int((23 - len(name)/2)), name, " " * int((23 - len(name)/2)))
    print(line)


def print_separator():
    print("-" * 46)


random.seed()


d = DHeap()

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


matrix = matrix11

size = len(matrix)
time1 = time.perf_counter()

'''d.name = [0, 1, 2]
d.key = [10, 5, 1]
d.index = [0, 1, 2]
d.make()

d.descend(0)
'''

print(d.name)
print(d.key)
print(d.index)

print_header("DIJKSTRA")
print("Result |", Dijkstra(size, 0, matrix))
print("Time   |  %s seconds" % (time.perf_counter() - time1))

time1 = time.perf_counter()
print_header("DIJKSTRA MARK")
print("Result |", Dijkstra_Mark(size, 0, matrix))
print("Time   |  %s seconds" % (time.perf_counter() - time1))

time1 = time.perf_counter()
print_header("DIJKSTRA DHEAP")
print("Result |", Dijkstra_DHeap(size, 0, d, matrix))
print("Time   |  %s seconds" % (time.perf_counter() - time1))
