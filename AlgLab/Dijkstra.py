import time
import random


class DHeap:
    key = []
    name = []
    index = []
    len = int()
    d = int()
    name1 = int()
    key1 = int()

    def __init__(self, d_=3):
        self.d = d_

    def ascend(self, i):
        p = (i - 1) // self.d
        while i != 0 and (self.key[p] > self.key[i]):
            self.key[i], self.key[p] = self.key[p], self.key[i]
            i = p
            p = (i - 1) // self.d

    def ascend2(self, i):
        key0 = self.key[i]
        name0 = self.name[i]

        p = (i - 1) // self.d
        while i != 0 and (self.key[p] > self.key[i]):
            self.key[i], self.key[p] = self.key[p], self.key[i]
            self.name[i], self.name[p] = self.name[p], self.name[i]
            self.index[self.name[i]] = i
            i = p
            p = (i - 1) // self.d
        self.key[i] = key0
        self.name[i] = name0
        self.index[self.name[i]] = i

    def min_child(self, i):
        n = len(self.key)
        if i * self.d + 1 >= n:
            return 0
        else:
            s = i * self.d + 1
            min_key = self.key[s]
            last = (i + 1) * self.d
            if last >= n:
                last = n - 1
            j = s + 1
            while j <= last:
                if min_key > self.key[j]:
                    min_key = self.key[j]
                    s = j
                j += 1
            return s

    def first_child(self, i):
        n = len(self.key)
        first_child = i * self.d + 1
        if first_child > n:
            return 0
        else:
            return first_child

    def last_child(self, i):
        n = len(self.key)
        first_child = self.first_child(i)
        if first_child:
            return 0
        else:
            return min(first_child + self.d - 1, n)

    def father(self, i):
        return (i - 1) // self.d

    def descend(self, i):
        s = self.min_child(i)
        while s != 0 and self.key[i] > self.key[s]:
            self.key[i], self.key[s] = self.key[s], self.key[i]
            i = s
            s = self.min_child(i)

    def descend2(self, i):
        key0 = self.key[i]
        name0 = self.name[i]

        s = self.min_child(i)
        while s != 0 and self.key[i] > self.key[s]:
            self.key[i] = self.key[s]
            self.name[i] = self.name[s]
            self.index[self.name[i]] = i
            i = s
            s = self.min_child(i)
        self.key[i] = key0
        self.name[i] = name0
        self.index[self.name[i]] = i

    def insert(self, new_key):
        n = len(self.key)
        self.key.append(3)
        self.ascend2(n)

    def delete(self, i):
        n = len(self.key)
        self.key[i] = self.key[n - 1]
        if i != 0 and self.key[i] < self.key[(i - 1) // self.d]:
            self.ascend2(i)
        else:
            self.descend2(i)

    def reduce(self, i, k):
        self.key[i] = self.key[i] - k
        self.ascend2(i)

    def get_min(self):
        # self.name[0], self.name[len(self.name) - 1] = self.name[len(self.name) - 1], self.name[len(self.name) - 1]
        n = int(self.len)
        self.name1 = self.name[0]
        self.key1 = self.key[0]
        self.name[0] = self.name[n - 1]
        self.key[0] = self.key[n - 1]
        self.name[n - 1] = self.name1
        self.key[n - 1] = self.key1

        self.len -= 1

        if self.len > 1:
            self.descend2(0)

    def make(self):
        n = len(self.key)
        i = (n - 1)
        while i >= 0:
            self.descend2(i)
            i = i - 1
        self.len = len(self.name)


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
        valid[ID_min_weight] = False
        up.append(ID_min_weight)
    print("Path   |", up)
    return weight


def Dijkstra_DHeap(n, s, d, matrix):
    weight = [1000000] * n
    d.name = [i for i in range(n - 1, -1, -1)]
    d.key = [1000000] * size
    d.index = [i for i in range(n - 1, -1, -1)]
    d.key[s] = 0
    d.make()
    up = [0] * n
    while d.len > 0:
        d.get_min()
        i = d.name1
        print("curr min ", d.name1)
        weight[i] = d.key1
        print("weight ", d.key1)
        p = matrix[i]
        for index, value in enumerate(p):
            print("name ", d.name)
            print("key  ", d.key)
            print("index", d.index)
            print(d.len)
            j = index
            print("j ", j)
            jq = d.index[j]
            print("jq ", jq)
            if weight[jq] == 1000000:
                if d.key[jq] > weight[i] + value:
                    d.key[jq] = weight[i] + value
                    d.ascend2(jq)
                    up[j] = i
            #print("up", up)
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
matrix = [[MAX, 1, MAX, 2], [1, MAX, 2, MAX], [MAX, 2, MAX, 3], [2, MAX, 3, MAX]]
matrix2 = [[MAX, 7, 9, MAX, MAX, 14],
           [7, 0, 10, 15, MAX, MAX],
           [9, 10, 0, 11, MAX, 2],
           [MAX, 15, 11, 0, 6, MAX],
           [MAX, MAX, MAX, 6, 0, 9],
           [14, MAX, 2, MAX, 9, 0]]




size = len(matrix)
time1 = time.time()

print_header("DIJKSTRA")
print("Result |", Dijkstra(size, 0, matrix))
print("Time   |  %s seconds" % (time.time() - time1))

time1 = time.time()
print_header("DIJKSTRA MARK")
print("Result |", Dijkstra_Mark(size, 0, matrix))
print("Time   |  %s seconds" % (time.time() - time1))

time1 = time.time()
print_header("DIJKSTRA DHEAP")
print(Dijkstra_DHeap(size, 0, d, matrix))
print("Time   |  %s seconds" % (time.time() - time1))


