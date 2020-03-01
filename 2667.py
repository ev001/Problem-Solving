# 단지번호붙이기 # BFS
import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x, count):
    q = deque()
    q.append([y, x])
    visit[y][x] = count
    while q:
        y, x = q.popleft()

        for idx in range(4):
            ny, nx = y + i_y[idx], x + i_x[idx]

            if 0 <= nx < n and 0 <= ny < n:
                if a[ny][nx] == 1 and visit[ny][nx] == 0:
                    q.append([ny, nx])
                    visit[ny][nx] = count
    return count


n = int(input())
a = [list(map(int, input().strip())) for _ in range(n)]

# 이동방향 4방향
i_x = [-1, 0, 1, 0]
i_y = [0, -1, 0, 1]

# 방문했다는 visit[]
visit = [[0] * n for _ in range(n)]

# 방문 단지 세는 cnt
cnt = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0 and a[i][j] == 1:
            cnt += 1
            bfs(i, j, cnt)

ans = [0] * (n ** 2)
for i in range(n):
    for j in range(n):
        if visit[i][j]:
            ans[visit[i][j]] += 1
print(cnt)
for i in sorted(ans[1:cnt + 1]):
    print(i)
