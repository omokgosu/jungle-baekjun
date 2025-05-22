import sys
# 힙 정렬

def down_heapify(arr, root, size):
    while root * 2 + 1 < size:
        left = root * 2 + 1
        right = root * 2 + 2 
        smallest = root

        if left < size and arr[left] > arr[smallest]: smallest = left
        if right < size and arr[right] > arr[smallest]: smallest = right

        if smallest == root: break
        else:
            arr[root] , arr[smallest] = arr[smallest] , arr[root]
            root = smallest

def solution():
    
    # count = int(input())
    # arr = []

    # for i in range(count):
    #     arr.append(int(sys.stdin.readline()))

    arr = [4,10,3,5,1,2,7]

    n = len(arr)

    # 힙화
    for i in range( (n-2)//2 , -1, -1):
        down_heapify( arr, i, n)

    # 힙정렬
    for i in range( n-1 ,0 ,-1):
        arr[0],arr[i] = arr[i],arr[0]
        down_heapify(arr, 0, i)

    print(arr)

solution()