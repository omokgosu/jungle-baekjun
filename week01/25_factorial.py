def solution():
    def factorial(n):
        if n == 1 or n == 0: return 1

        return n * factorial(n-1)

    n = int(input())

    print(factorial(n))


solution()

# 시간복잡도 = O(n) n의 개수에 따라 연산횟수가 달라지니까