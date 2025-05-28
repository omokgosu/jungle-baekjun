import sys

n = int(input())
stack = []

for i in range(n):
    stack.append(int(sys.stdin.readline()))

max_stick = 0
count = 0

while len(stack) > 0:
    stick = stack.pop()
    
    if stick > max_stick:
        count += 1
        max_stick = stick

print(count)
    