# 영역 구하기 # 그래프

import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

m, n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(k)]
fill = [[0] * n for _ in range(m)]
visit = [[0] * n for _ in range(m)]

# a[1] = [ c1, r1, c2, r2 ]
# 왼쪽 아래 r1 c2
# 오른쪽 위 r2 c2
# c 범위 c1 <= c < c2
# r 범위 r1 <= r < r2

# 사각형 채우기.
for element in a:
    c1, r1, c2, r2 = element
    for r in range(r2 - r1):  # 4번 까지
        for c in range(c2 - c1):  # 2 번까지
            # 들어가는 인덱스는 r1,c1에서 + i, j
            ndx, ndy = c1 + c, r1 + r
            fill[ndy][ndx] = 1

# 빈 공간 개수 찾기.
# fill 리스트(1로 구성)가 벽이라고 생각.
# fill 0을 탐색
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

cnt = 0
size_list = []


def bfs(start):
    q = deque()
    q.append(start)
    max_size = 1
    while q:
        x, y = q.popleft()

        for idx in range(4):
            nx, ny = dx[idx] + x, dy[idx] + y
            if 0 <= nx < m and 0 <= ny < n:
                # 새로 방문한곳의 fill이 1이 아니라면?
                if not fill[nx][ny] and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    q.append((nx, ny))
                    max_size += 1
    size_list.append(max_size)


cnt = 0
for i in range(m):
    for j in range(n):
        if not fill[i][j] and not visit[i][j]:
            visit[i][j] = 1
            bfs((i, j))
            cnt += 1

print(cnt)
for i in sorted(size_list):
    print(i, end=' ')
