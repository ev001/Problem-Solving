# 유기농 배추
import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs(r, c):
    q = deque()
    q.append((r, c))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append((nx, ny))


for _ in range(tc):
    # m : 가로, n: 세로
    m, n, k = map(int, input().split())

    arr = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    for i in range(k):
        c, r = map(int, input().split())
        arr[r][c] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visit[i][j] == 0:
                bfs(i, j)
                cnt += 1

    print(cnt)
