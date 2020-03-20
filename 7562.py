# 나이트의 이동 # bfs
import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        if x == goal[0] and y == goal[1]:
            print(visit[x][y])
            return
        for i in range(8):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))


tc = int(input())

dx = (2, 1, -1, -2, -2, -1, 1, 2)
dy = (1, 2, 2, 1, -1, -2, -2, -1)

for _ in range(tc):
    n = int(input().strip())
    visit = [[0] * n for _ in range(n)]
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    bfs()

'''
    방문 coount를 올릴때, 
    count 변수를 만들지말고 
    이전에 방문한 방문지에 +1 하기.
    visit[nx][ny] = visit[x][y] + 1
'''