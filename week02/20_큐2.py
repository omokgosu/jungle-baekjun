from collections import deque
import sys

input = sys.stdin.readline  # 빠른 입력

n = int(input())
queue = deque()

for _ in range(n):
    command = input().strip()

    if command.startswith('push'):
        _, x = command.split()
        queue.append(int(x))

    elif command == 'pop':
        print(queue.popleft() if queue else -1)

    elif command == 'size':
        print(len(queue))

    elif command == 'empty':
        print(0 if queue else 1)

    elif command == 'front':
        print(queue[0] if queue else -1)

    elif command == 'back':
        print(queue[-1] if queue else -1)