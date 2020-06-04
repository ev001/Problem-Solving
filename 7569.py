# 토마토 3차원 # 7569

import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
visit = [[[-1] * m for _ in range(n)] for _ in range(h)]
arr = list()
q = deque()

for k in range(h):
    tmp = list()
    for r in range(n):
        row = list(map(int, input().split()))
        for c, e in enumerate(row):
            if e == 1:
                q.append((k, r, c))
                visit[k][r][c] = 0
        tmp.append(row)
    arr.append(tmp)

dh, dx, dy = (1, -1, 0, 0, 0, 0), (0, 0, 0, 0, 1, -1), (0, 0, 1, -1, 0, 0)


def bfs():
    while q:
        hh, x, y = q.popleft()

        for idx in range(6):
            nh = hh + dh[idx]
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nh < h and 0 <= nx < n and 0 <= ny < m:
                if visit[nh][nx][ny] == -1 and arr[nh][nx][ny] == 0:
                    visit[nh][nx][ny] = visit[hh][x][y] + 1
                    q.append((nh, nx, ny))


bfs()
ans = 0
flag = False  # -1 이면 True
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 0 and visit[k][i][j] == -1:
                ans = -1
                flag = True
                break
            ans = max(ans, visit[k][i][j])
    if flag:
        break
print(ans)


'''
간과했던점:
2중 이상이 for문에서 break를 한번만 걸어 제대로 제어를 하지 못했음.

참고해볼만한 코드
from collections import deque

n, m, h = map(int, input().split())
grid = [[list(map(int, input().split())) for y in range(m)] for z in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
Q = deque([])

for z in range(h):
    for y in range(m):
        for x in range(n):
            if grid[z][y][x] == 1:
                Q.append((x,y,z))

def bfs():
    day = -1

    while Q:
        day+=1

(출처) : https://www.acmicpc.net/source/2007155


'''