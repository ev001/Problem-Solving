# 유턴 싫어 # 배열 # 구현

import sys

input = sys.stdin.readline

# r을 y로 c를 x로 보고 풀자
r, c = map(int, input().split())
map = [list(map(str, input().strip())) for _ in range(r)]

dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]


def find():
    for i in range(r):
        for j in range(c):
            if map[i][j] == '.':
                cnt = 0
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < r and 0 <= nx < c:
                        if map[ny][nx] == '.':
                            cnt += 1
                    else:
                        continue
                if cnt <= 1:
                    return 1
    return 0


print(find())
