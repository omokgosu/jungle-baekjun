n = int(input())

stack = []

for i in range(n):
    string = input()
    
    if string.startswith('push'):
        a,b = string.split(' ')
        stack.append(int(b))

    if string == 'pop':
        if len(stack) == 0:
            print(-1)
        else: print(stack.pop())

    if string == 'size':
        print(len(stack))

    if string == 'empty':
        print(1) if len(stack) == 0 else print(0)
        
    if string == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])