import sys
input = sys.stdin.readline

# 이진수 문자열
binary = 0b00000000000000000000

# N은 연산 횟수
N = int(input())

for _ in range(N):
    command = input()
    
    if command.startswith('all'):
        binary = -1
        continue
    if command.startswith('empty'):
        binary = 0
        continue

    command,target = command.split(' ')
    target = int(target)

    # 0010 을 만들고 or 연산으로 무조건 1로 == add
    if command == 'add':
        binary |= (1 << target)

    # 0010 을 만들고 and 연산으로 무조건 0으로 == remove
    if command == 'remove':
        binary &= ~(1 << target) 

    # 0010 을 만들고 True 면 1 False 면 0인데..
    if command == 'check':
        print(1) if binary & (1 << target) else print(0)
        
    # 1이면 0으로 0이면 1로
    if command == 'toggle':
        binary ^= (1 << target)