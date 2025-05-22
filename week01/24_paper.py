def solution():
    x,y = map(int,input().split(' '))

    count = int(input())

    garo = [ 0, x ]
    saero = [ 0 , y ]

    for _ in range(count):
        type, line = map(int,input().split(' '))

        if type == 1:
            garo.append(line)
        else:
            saero.append(line)


    garo.sort()
    saero.sort()

    maxX = 0
    maxY = 0

    for i in range(1, len(garo)):
        maxX = max(maxX , garo[i] - garo[i-1])

    for i in range(1, len(saero)):
        maxY = max(maxY , saero[i] - saero[i-1])

    print( maxX * maxY )


solution()

