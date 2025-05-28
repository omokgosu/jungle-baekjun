import sys

n,exponent = map(int, (input().split(' ')))

base_matrix = [ list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(n)]

def mul(A,B):
    result = [ [0]* n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += ((A[i][k]%1000) * (B[k][j]%1000)) % 1000
            
            result[i][j] %= 1000
    
    return result

def matrix_power(matrix,power):
    if power == 1:
        return [[element % 1000 for element in row] for row in matrix]
    
    half = matrix_power(matrix, power//2)
    result = mul(half,half)

    if power % 2 == 1:
        result = mul(result,matrix)

    return result

# 출력
result_matrix = matrix_power(base_matrix , exponent)

for row in result_matrix:
    print(' '.join(map(str,row)))

