def solution():

    a = int(input())
    b = int(input())
    c = int(input())

    num = a * b * c

    count = [0] * 10

    for i in str(num):
        count[int(i)] += 1

    for i in count: print(i)


solution()

# 시간복잡도 
# input 입력 3
# 연산 (1)
# for 문 ( 곱셉의 결과 n 만큼 ) n 하지만 100보다크고 1000보다 작은걸로 결과가 최댓값이 정해져있으므로 1
# 즉 O(1)

# 공간복잡도 O(n) 
# a,b,c 카운트 [10] O(1)