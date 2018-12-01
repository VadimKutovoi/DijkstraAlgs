class DHeap:
    key = []
    name = []
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
            self.name[i], self.name[s] = self.name[s], self.name[i]
            i = p
            p = (i - 1) // self.d
        self.key[i] = key0
        self.name[i] = name0

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
            i = s
            s = self.min_child(i)
        self.key[i] = key0
        self.name[i] = name0

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
        self.name[0], self.name[len(self.name) - 1] = self.name[len(self.name) - 1], self.name[len(self.name) - 1]
        #self.name1 = self.name.pop(0)
        #self.key1 = self.key.pop(0)

        if len(self.key) > 1:
            self.descend2(0)

    def make(self):
        n = len(self.key)
        i = (n - 1)
        while i >= 0:
            self.descend2(i)
            i = i - 1

