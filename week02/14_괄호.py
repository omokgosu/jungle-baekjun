n = int(input())

for i in range(n):
    string = input()
    stack = []
    check = True

    for i in string:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) == 0:
                check = False
                break;
            
            check_string = stack.pop()
            
            if check_string != '(':
                check = False
                break;

    print('YES') if check and len(stack) == 0 else print('NO')

