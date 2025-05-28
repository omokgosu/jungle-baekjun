k = int(input())

stack = []

for _ in range(k):
    number = int(input())

    if number:
        stack.append(number)
    else:
        stack.pop()

print(sum(stack))