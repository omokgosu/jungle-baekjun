import sys

class maxHeap:
    
    def __init__(self):
        self.heap = []

    def isEmpty(self):
        return 0 if self.heap else 1

    def insert(self,node):
        self.heap.append(node)
        index = len(self.heap) - 1
        parent = (index - 1) // 2

        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def delete(self):
        if self.isEmpty(): return 0
        
        value = self.heap[0]

        self.heap[0] , self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1] , self.heap[0]
        self.heap.pop()

        root = 0
        while root < len(self.heap):
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2

            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == root:
                break
            else:
                self.heap[largest] , self.heap[root] = self.heap[root] , self.heap[largest]
                root = largest

        return value

hp = maxHeap()

n = int(input())

for i in range(n):
    command = sys.stdin.readline().strip()

    if command == '0':
        print(hp.delete())
    else:
        hp.insert(int(command))