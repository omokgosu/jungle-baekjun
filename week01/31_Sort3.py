import sys

def solution():
    
    array = [0] * 10001

    num = int(input())

    for _ in range(num):
        array[int(sys.stdin.readline())] += 1

    for i in range(1, 10001):
        for _ in range(array[i]):
            print(i)
solution()