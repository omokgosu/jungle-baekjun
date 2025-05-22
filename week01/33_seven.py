import sys

def solution():

    arr = sorted([int(sys.stdin.readline().rstrip()) for i in range(9)])
    
    total = sum(arr)

    found = False
    for i in range(len(arr) - 1):
        for j in range(i+1,len(arr)):
            if total - arr[i] - arr[j] == 100:
                arr.remove(arr[j])
                arr.remove(arr[i])
                found = True 
                break

        if found: break

    for i in arr:
        print(i)


solution()