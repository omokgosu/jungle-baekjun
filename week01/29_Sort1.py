import sys

def merge(low, mid, high, arr):

    temp = []
    l , r = low, mid

    # 어느 한쪽이 끝까지 갈때까지
    while (l < mid and r < high):
        if arr[l] <= arr[r]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[r])
            r += 1
    
    # 왼쪽이 비어있으면 채워주기
    while (l < mid):
        temp.append(arr[l])
        l += 1

    # 오른쪽이 비어있으면 채워주기
    while (r < high):
        temp.append(arr[r])
        r += 1

    for i in range(low,high):
        arr[i] = temp[i-low]
    

def merge_sort(low , high, arr):
    if high - low < 2: # 배열의 크기가 1인경우
        return
    
    mid = (low + high) // 2 ## 중앙값 내림
    merge_sort(low, mid, arr)
    merge_sort(mid, high, arr)
    merge(low, mid, high, arr)
    

# [2,1,3,4]
# 쪼갤수없을 때까지 절반으로 나눈다.
# 그리고 합친다.

def solution():
    
    n =  int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]

    merge_sort(0 , len(arr), arr)

    for i in arr:
        print(i)

solution()