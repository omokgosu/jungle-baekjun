n = int(input())

array = [ input().split(' ') for _ in range(n)]

white = 0
blue = 0

def count_square(n , start , end):
    global white,blue

    x1,x2 = start
    y1,y2 = end

    if n == 1:
        if array[x1][x2] == '0': white += 1
        else: blue += 1
        return
    
    default = array[x1][x2]
    check = True
    
    for i in range(x1,y1+1):
        for j in range(x2,y2+1):
            if array[i][j] != default:
                check = False 

    if check == True:
        if default == '0': white += 1
        else: blue += 1    
    else:
        half = n // 2 # 8이면 4로
        #1사분면
        count_square(half , [x1,x2] , [x1+half-1 ,x2+half-1])
        #2사분면
        count_square(half, [x1, x2 + half] , [x1+half-1, y2])
        #3사분면
        count_square(half, [x1 + half, x2] , [y1, x2+half-1] )
        #4사분면
        count_square(half, [x1+half,x2+half] , [y1, y2])

count_square(n, [0,0] , [n-1,n-1])

print(white)
print(blue)
