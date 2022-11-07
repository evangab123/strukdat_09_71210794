class Node:
    def __init__(self,data,priority):
        self._data = data
        self._priority = priority

class PriorityQueueSortedList:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0
    
    def add(self, e,n):
        baru = Node(e,n)
        self._data.append(tuple([baru._data,baru._priority]))
        self._data.sort(key=lambda a: a[1])

    def peek(self):
        print("Data Prioritas Tertinggi :", self._data[0])

    def update(prioBaru, dataBaru):
        pass

    def remove(self):
        return self._data.pop(0)

    def removePrio(self,prio):
        pass
    def printIsiQueue(self):
        if self.is_empty():
            print("Empty!")
        else:
            print("Isi Semua Queue :")
            for i in range(len(self._data)):
                print(self._data[i],end=" ")

sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.remove()
sortedList.peek()
sortedList.printIsiQueue()
