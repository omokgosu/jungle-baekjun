import math

def solution():
    arr = [True] * 1001

    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.ceil(math.sqrt(1000)))):
        count = i+i;

        while(count <= 1000):
            arr[count] = False
            count += i

    n = input()
    array = map(int ,  input().split(' '))

    count = 0;

    for i in array:
        if arr[i]: count += 1

    print(count)


solution()