# 산성 용액 특성값 = 1 ~ 10억
# 알칼리성 용액 특성값 = -1 ~ -10억

# 산성 + 알칼리성 특성 값 =  산 특 + 알 특
n = int(input())

solution = sorted(list(map(int,input().split(' '))))

def binary_search():

    start = 0
    end = len(solution) - 1

    answer = [solution[start],solution[end]]
    hap = float("inf")

    while start < end:
        plus = solution[start] + solution[end]

        if abs(plus) < abs(hap): 
                        answer = [solution[start],solution[end]]
                        hap = plus

        if plus == 0:
            answer = [solution[start],solution[end]]
            break;
        if plus > 0:
            end -= 1
        else:
            start += 1


    print(answer[0],answer[1])

binary_search()

