from itertools import permutations

def solution():
    n = int(input())

    arr = list(map(int,input().split(' ')))

    combination = list(permutations(arr,n))

    maxValue = 0

    for i in combination:
        currentMax = 0
        for j in range(len(i)-1):
            currentMax += abs(i[j] - i[j+1])

        maxValue = max(currentMax , maxValue)

    print(maxValue)

solution()


# 모든순열 조회 알고리즘
def permutation(arr, r):
    arr = sorted(arr)  # 원본 배열 정렬
    used = [0 for _ in range(len(arr))]  # 사용 여부 체크 배열

    def generate(chosen, used):
        if len(chosen) == r:         # r개 골랐으면 출력
            print(chosen)
            return

        for i in range(len(arr)):
            if not used[i]:         # 안 쓴 원소면
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)  # 재귀 호출
                used[i] = 0
                chosen.pop()           # 원상 복구 (백트래킹)
    generate([], used)
    



# permutation([1,2,3] , 2)