# 안전 영역 # dfs

import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def dfs(x, y, h):
    for m in range(4):
        nx, ny = x + dx[m], y + dy[m]
        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and arr[nx][ny] > h:
            visit[nx][ny] = True
            dfs(nx, ny, h)


ans = 1
for k in range(max(map(max, arr))):
    visit = [[False] * n for _ in range(n)]
    safe = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not visit[i][j]:
                safe += 1
                visit[i][j] = True
                dfs(i, j, k)
    ans = max(ans,safe)

print(ans)

'''
    * 알게된점
    max(map(max, arr))
    다음과 같이 max 값을 뽑아낼 수 있음.
'''