# 알파벳 # bfs

import sys

input = sys.stdin.readline

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs(x, y):
    global answer
    q = {(x, y, arr[x][y])}

    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and (arr[nx][ny] not in ans):
                q.add((nx, ny, ans + arr[nx][ny]))
                answer = max(answer, len(ans) + 1)


r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

answer = 1
bfs(0, 0)
print(answer)
