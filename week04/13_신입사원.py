import sys
input = lambda: sys.stdin.readline().strip()

# T는 테스트 케이스의 갯수
T = int(input())

# N은 테스크 케이스 별 지원자의 숫자
for _ in range(T):
    N = int(input())

    result = sorted( [ tuple(map(int, input().split(' '))) for _ in range(N) ] , key=lambda x: x[0] )

    count = 1

    grade = result[0][1]

    for i in range(1,len(result)):
        if result[i][1] < grade:
            count += 1
            grade = result[i][1]

    print(count)