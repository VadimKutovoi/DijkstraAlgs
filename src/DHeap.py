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
        self.index[self.name[0]], self.index[self.name[n]] \
            = self.index[self.name[n]], self.index[self.name[0]]
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