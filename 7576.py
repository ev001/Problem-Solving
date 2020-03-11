# 토마토 # 7576 # bfs

# m 가로칸수 n 세로칸수

import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                # 좌표에 토마토가 있고(0), 방문을 안했다면(-1)
                if a[nx][ny] == 0 and check[nx][ny] == -1:
                    q.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[-1] * m for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            check[i][j] = 0
            q.append((i, j))

bfs()

ans = max([max(row) for row in check])

for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and check[i][j] == -1:
            ans = -1
            break
print(ans)
