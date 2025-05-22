import math

def solution():
    
    arr = [True] * 10001

    arr[0] = False
    arr[1] = False

    for i in range(2, int( math.sqrt(10001) + 1) ):
        if arr[i]:
            # i*i부터 시작하는 게 핵심!
            for j in range(i * i, 10001, i):
                arr[j] = False


    n = int(input())

    # print(arr)

    for i in range(n):
        num = int(input())

        a,b= num//2 , num//2

        while(a > 0):
            if arr[a] and arr[b]:
                print(a,b)
                break;
            else:
                a -= 1
                b += 1

solution()

# 시간복잡도 O(1) 계산한번!

# 공간복잡도 O(1) 공간 3개!
