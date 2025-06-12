import sys
input = lambda: sys.stdin.readline().strip()

# A 와 B 는 문자열
A = input()
B = input()

lenA = len(A)
lenB = len(B)

# A 와 B 의 길이 + 1 만큼 행열 생성
dp = [ [ 0 for _ in range (lenB + 1)] for _ in range(lenA + 1) ]

for i in range(1,len(A) + 1):
    for j in range(1,len(B) + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

print(dp[lenA][lenB])