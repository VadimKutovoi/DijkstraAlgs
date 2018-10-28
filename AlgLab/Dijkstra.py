import time
import random

class DHeap:
    key = []
    name = []
    index = []
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
            self.key[i], self.key[s] = self.key[s], self.key[i]
            self.name[i], self.name[s] = self.name[s], self.name[i]
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
        #self.name[0], self.name[len(self.name) - 1] = self.name[len(self.name) - 1], self.name[len(self.name) - 1]
        self.name1 = self.name.pop(0)
        self.key1 = self.key.pop(0)

        if len(self.key) > 1:
            self.descend2(0)

    def make(self):
        n = len(self.key)
        i = (n - 1)
        while i >= 0:
            self.descend2(i)
            i = i - 1

def Dijkstra(n, s, matrix):
    valid = [True] * n
    weight = [1000000] * n
    weight[s] = 0
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
    return weight

def Dijkstra_DHeap(n, s, d, matrix):
    weight = [1000000] * n
    d.name = [i for i in range(0, n)]
    d.key = [1000000] * size
    d.index = [i for i in range(0, n)]
    d.key[s] = 0
    nq = n
    d.make()
    while nq > 0:
        d.get_min()
        i = d.name1
        weight[i] = d.key1
        p = matrix[i]
        el_i = 0
        for el in p:
            k = el_i
            jq = d.index[k]
            if weight[k] == 1000000:
                if d.key[jq] > weight[i] + el:
                    d.key[jq] = weight[i] + el
                    d.ascend2(k)
            el_i += 1
    return weight


def Dijkstra_Mark(n, s, matrix):
    weight = [1000000] * n
    weight[s] = 0
    h = [0] * n
    nq = n
    while nq > 0:
        c = 0
        while h[c] != 0:
            c += 1
        i = c
        for k in range(c+1, n):
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
    return weight


random.seed()

size = 4
d = DHeap()

#matrix = [[] for i in range(0, size)]
#for i in range(0, size):
#    for j in range(0, size):
#        matrix[i].append(random.randrange(1, 100))

MAX = 1000000
matrix = [[MAX, 1, MAX, 1], [1, MAX, 2, MAX], [MAX, 2, MAX, 1], [1, MAX, 1, MAX]]

time1 = time.time()
print(Dijkstra(size, 0, matrix))
print("Dijkstra time %s seconds" % (time.time() - time1))

time1 = time.time()
print(Dijkstra_Mark(size, 0, matrix))
print("Dijkstra_Mark time %s seconds" % (time.time() - time1))

time1 = time.time()
print(Dijkstra_DHeap(size, 0, d, matrix))
print("Dijkstra_DHeap time %s seconds" % (time.time() - time1))
