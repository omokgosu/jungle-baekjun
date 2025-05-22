def solution():
    n = int(input())

    for _ in range(n):
        P = input().split(' ')
        
        count = int(P[0])
        S = P[1]

        string = ''
        for char in S:
           string += char*count

        print(string)

solution()


# 시간복잡도
# n 입력 1
# p 입력 후 분리 1
# count 저장 1
# s 저장 1
# string 반복문 8자 제한 상수 O(1)
# 즉 시간복잡도는 O(1)

# 공간복잡도
# n,p,s,count,string 5 가 되겠다.
# 공간복잡도 O(1)
