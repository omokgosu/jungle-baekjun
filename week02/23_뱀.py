from collections import deque
# 뱀은 처음에 오른쪽을 향한다.
#     우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 정사각형 보드의 크기 N * N
N = int(input())

# 사과의 위치
apple = [ [ False for _ in range(N) ] for _ in range(N)]

# 사과의 갯수
apple_count = int(input())

for i in range(apple_count):
    x,y = map(int, input().split(' '))
    apple[x-1][y-1] = True

# 방향 전환
COMMAND = int(input())
snake_direction = deque()

for _ in range(COMMAND):
    move,rotate = input().split(' ')
    snake_direction.append([int(move),rotate])


# 뱀 몸길이 정보
snake = deque()
snake.append([1,1])


def snake_move(second , snake_position, direction):

    while True:
        print(snake)
        
        second += 1

        new_x = snake_position[0] + dx[direction]
        new_y = snake_position[1] + dy[direction]

        # 게임종료
        if [new_x,new_y] in snake: # 자기 몸뚱아리에 부딪힐 때
            return second
        if not (1 <= new_x < N+1 and 1 <= new_y < N+1): # 벽에 부딪힐 때
            return second
        
        # 가려는 곳에 사과가 있음;;
        if apple[new_x-1][new_y-1]:
            snake.append([new_x,new_y]) # 몸땡이 늘리기
            apple[new_x-1][new_y-1] = False
        else: # 가려는 곳에 사과가 없음;;
            snake.append([new_x,new_y])
            snake.popleft()
        
        # 머리위치
        snake_position = [new_x,new_y]

        if snake_direction and second == snake_direction[0][0]:
            new_direction = 0
            if snake_direction[0][1] == 'D':
                new_direction = direction + 1
                if new_direction > 3: new_direction = 0
            else:
                new_direction = direction - 1
                if new_direction < 0: new_direction = 3
            direction = new_direction

            snake_direction.popleft()

    

second = snake_move(0,[1,1],0)

print(second)
