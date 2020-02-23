import sys
#from collections import *

input = sys.stdin.readline

# 방향
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())

# 미로 초기화
# sys.stdin.readline() 함수를 input()사용했음으로 strip()으로 끝의 개행을 제거
a = [list(map(int, input().strip())) for _ in range(N)]

# 방문할 곳 초기화
visit = [[0] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]

# 시작 부분
q = []
q.append((0, 0))

visit[0][0] = 1
dist[0][0] = 1
while q:
    x, y = q.pop(0)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visit[nx][ny] == 0 and a[nx][ny] == 1:
                q.append((nx, ny))
                visit[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1

print(dist[N - 1][M - 1])
