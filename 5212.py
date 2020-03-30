# 지구온난화 # 구현

import sys
import copy

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(r)]
draw = copy.deepcopy(arr)
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(r):
    for j in range(c):
        cnt = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] == '.':
                    cnt += 1
            if (nx == r or ny == c) or (nx == -1 or ny == -1):
                cnt += 1
            if cnt >= 3:
                draw[i][j] = '.'

findIdx = []
for i in range(r):
    for j in range(c):
        if draw[i][j] == 'X':
            findIdx.append((i, j))

min_ij, max_ij = [11, 11], [-1, -1]

for e in findIdx:
    # 최ㅅ값 찾기
    # i
    if e[0] < min_ij[0]:
        min_ij[0] = e[0]
    # j
    if e[1] < min_ij[1]:
        min_ij[1] = e[1]

    # 최ㄷ값 찾기
    if e[0] > max_ij[0]:
        max_ij[0] = e[0]
    if e[1] > max_ij[1]:
        max_ij[1] = e[1]

for i in range(min_ij[0], max_ij[0] + 1):
    for j in range(min_ij[1], max_ij[1] + 1):
        print(draw[i][j], end="")
    print()

'''         
    전부 돌면서 육지 중에 상하좌우(범위 넘는곳도 포함) 
    중 3곳 이상이 .이면     . 로바꿈
'''
