# 종이의 개수 # 분할 정복

import sys

input = sys.stdin.readline


def same(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if a[x][y] != a[i][j]:
                return False
    return True


def solve(x, y, n):
    if same(x, y, n):
        cnt[a[x][y] + 1] += 1
        return
    m = n // 3
    for i in range(3):
        for j in range(3):
            solve(x + i * m, y + j * m, m)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = [0 for _ in range(3)]

solve(0, 0, n)
for i in range(3):
    print(cnt[i])
