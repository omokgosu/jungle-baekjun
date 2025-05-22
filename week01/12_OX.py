def solution():

    n = int(input())

    for i in range(n):
        string = input()

        score = 0
        bonus = 0

        for i in string:
            if i == 'O':
                bonus += 1
                score += bonus
            if i == 'X':
                bonus = 0

        print(score)

solution()

# 시간복잡도  O( n * L ) 문자가 입력된 n 번만큼 그리고 문자 길이L  반복되기 때문에 n * L 로 추측된다.
# 공간복잡도 O(1) 갯수 n 과 문자열 길이 string 을 덮어쓰면서 사용하기 때문에 O(1) 으로 추측된다.