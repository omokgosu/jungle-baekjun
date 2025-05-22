def n_queens(row, n, cols, diag1, diag2):
    if row == n:
        return 1

    count = 0
    for col in range(n):
        if cols[col] or diag1[row + col] or diag2[row - col + n - 1]:
            continue

        # 상태 변경
        cols[col] = True
        diag1[row + col] = True
        diag2[row - col + n - 1] = True

        count += n_queens(row + 1, n, cols, diag1, diag2)

        # 상태 복구 (백트래킹)
        cols[col] = False
        diag1[row + col] = False
        diag2[row - col + n - 1] = False

    return count

def solution():
    n = int(input())
    cols = [False] * n            # 열 체크
    diag1 = [False] * (2 * n - 1) # ↘ 대각선 (row + col)
    diag2 = [False] * (2 * n - 1) # ↙ 대각선 (row - col + n - 1)
    
    print(n_queens(0, n, cols, diag1, diag2))

solution()