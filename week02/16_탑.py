from collections import deque

n = int(input())

top = list(map(int,input().split(' ')))

stack = deque()
result = [ 0 for _ in range(n) ]

while n > 0:
    current_top = top[n-1]

    while stack and stack[-1][0] <= current_top:
        a,b = stack.pop()
        result[b] = n

    stack.append([ current_top , n-1 ])
    n -= 1

print(' '.join(str(x) for x in result))