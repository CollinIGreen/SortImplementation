import random
import timeit
class sortSystem:
    def __init__(self):
        self.sortList = []
        self.length = 0
    def genList(self, length):
        self.sortList = list(range(0, length))
        for i in range(length):
            rand = random.randint(0, length-1)
            self.sortList[i], self.sortList[rand] = self.sortList[rand], self.sortList[i]
        self.length = len(self.sortList)
        print("finished")
    def selSort(self):
        list = self.sortList.copy()
        for i in range(self.length):
            holder = list[i]
            hPos = i
            for x in range(i+1, self.length):
                if holder > list[x]:
                    holder = list[x]
                    hPos = x
            list[hPos], list[i] = list[i], list[hPos]
        return list
    def inSort(self):
        list = self.sortList.copy()
        for i in range(1, self.length):
            holder = list[i]
            for x in range(0, i):
                if list[x] > holder:
                    list[i], list[x] = list[x], list[i]
                    break
        return list
    def bubSort(self):
        measure = 0
        list = self.sortList.copy()
        while measure < self.length-1:
           measure = 0
           for i in range(self.length-1):
               if list[i] > list[i+1]:
                   list[i], list[i+1] = list[i+1], list[i]
               else:
                   measure = measure + 1
        return list


hello = sortSystem()
hello.genList(10)

print(timeit.timeit(hello.inSort, number=1))
print("insert")
print(timeit.timeit(hello.selSort, number=1))
print("select")
print(timeit.timeit(hello.bubSort, number=1))
print("Buble")

hello.genList(1000)

print(timeit.timeit(hello.inSort, number=1))
print("insert")
print(timeit.timeit(hello.selSort, number=1))
print("select")
print(timeit.timeit(hello.bubSort, number=1))
print("Buble")

hello.genList(100000)

print(timeit.timeit(hello.inSort, number=1))
print("insert")
print(timeit.timeit(hello.selSort, number=1))
print("select")
print(timeit.timeit(hello.bubSort, number=1))
print("Buble")

print(hello.sortList)
