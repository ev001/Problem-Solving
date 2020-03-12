# 유기농 배추 # 그래프
import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())
# 이 문제는 bfs로 돌수 있는 공간이 몇개 있는지

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(tc):
    r, c, p = map(int, input().split())
    arr = [[0] * c for _ in range(r)]
    visit = [[0] * c for _ in range(r)]

    for i in range(p):
        rr, cc = map(int, input().split())
        arr[rr][cc] = 1

    q = deque()
    cnt = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1 and visit[i][j] == 0:
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < r and 0 <= ny < c:  # 탐색할수있는 좌표면?
                            if arr[nx][ny] == 1 and visit[nx][ny] == 0:
                                q.append((nx, ny))
                                visit[nx][ny] = 1
                cnt += 1
    print(cnt)
