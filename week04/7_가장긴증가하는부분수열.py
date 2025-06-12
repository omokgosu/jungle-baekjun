import sys
input = lambda: sys.stdin.readline().strip()

# N은 수열의 크기
N = int(input())

# 수열
A = list(map(int, input().split(' ')))

# dp 초기화
dp = [ 1 ] * N 

for i in range(len(A)):
                            
    # 시작을 i 로 설정
    max_value , max_count = A[i] , dp[i]

    
    for j in range( i+1 , len(A)):
        if A[j] > max_value and max_count + 1 > dp[j]:
            dp[j] += 1

print(max(dp))