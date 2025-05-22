def solution():

    chars = input().split(' ')

    a = ''.join(reversed(chars[0]))
    b = ''.join(reversed(chars[1]))

    print ( a if int(a) > int(b) else b)

solution()


# 시간복잡도 O(1)

# 공간복잡도 O(1)