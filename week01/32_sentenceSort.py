import sys

def isCharComparison(a,b):
    if len(a) > len(b): return True
    if len(a) < len(b): return False
    if a > b: return True
    return False
    

def down_heapify(arr, root ,size):
    while 2 * root + 1 < size:
        left = 2 * root + 1
        right = 2 * root + 2
        largest = root

        if (
            left < size and
            isCharComparison(arr[left],arr[largest])
        ): largest = left
        
        if (
            right < size and
            isCharComparison(arr[right],arr[largest])
        ): largest = right

        if largest == root: break

        arr[largest] , arr[root] = arr[root] , arr[largest]

        root = largest
        

def heap_sort():
    
    words = int(input())


    arr = list(set([sys.stdin.readline().rstrip() for _ in range(words)]))
    n = len(arr)

    for i in range( (n-2)//2  ,-1,-1):
        down_heapify(arr,i,n)


    for i in range(n-1,0,-1):
        arr[i] , arr[0] = arr[0] ,arr[i]
        down_heapify(arr,0,i)

    for i in arr:
        print(i)

heap_sort()