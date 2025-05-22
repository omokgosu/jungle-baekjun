def solution():

    n = int(input())

    for _ in range(n):
        score_list = list( map ( float, input().split(' ') ))
        people = score_list[0]
        score = score_list[1:]

        avg = sum(score) / people
        count = len(list(filter(lambda x: x > avg , score)))

        print (f"{(count / people * 100):.3f}%")  


solution()

# 시간복잡도 O(nm)
# 입력케이스 5번 n   
# 사용자 입력을 map 으로 변환 m
# map 불변객체를 list 로 변환 m
# score_list[0] 을 score 에 담기 1
# 1부터 새 배열에 담기 len - 1  = 1
# 평균구하기 = m + 1
# filter 후 list 로 변환후 len 2m + 1
# 5n + 4

# 공간복잡도 O(n) ( n 은 반복횟수가 아닌 입력 사람수 )
# score_list를 담을 m 만큼의 배열
# people 1
# score m-1
# avg 1
# count 1
# n+2