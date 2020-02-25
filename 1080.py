# 크기 제한이 20억이다.
# for문으로는 불가.
# 수식을 이용한다.

import sys

input = sys.stdin.readline


def flip(i, j):
    for x in range(i, i + 3, 1):
        for y in range(j, j + 3, 1):
            a[x][y] = 1 - a[x][y]


N, M = map(int, input().split())

a = [list(map(int, input().strip())) for _ in range(N)]
b = [list(map(int, input().strip())) for _ in range(N)]

ans = 0
# 3*3 의 부분행렬의 범위는 전체 N-2, M-2 이다.
for i in range(N - 2):
    for j in range(M - 2):
        if a[i][j] != b[i][j]:
            ans += 1
            flip(i, j)

print(ans if sorted(a) == sorted(b) else -1)