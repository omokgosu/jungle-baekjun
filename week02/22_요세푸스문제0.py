from collections import deque

queue = deque()
result = []

n,k = map(int, input().split(' '))

for i in range(1,n+1):
    queue.append(str(i))

count = k - 1

while len(queue) > 0:

    number = count % len(queue)
    result.append(queue[number])
    del queue[number]

    count = number + k - 1

print(f"<{', '.join(result)}>")