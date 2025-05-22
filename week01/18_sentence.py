def solution():

    string = input().strip()

    if string:
        print(len(string.split(' ')))
    else: print(0)

solution()


# 시간복잡도
# 입력 1
# split 문자열 길이만큼 n ( 100만을 넘지 않음 )
# len 1
# 그래서 O(1) 로 봐도 됨

# 공간복잡도
# string 만큼 100만을 넘지 않으므로 1