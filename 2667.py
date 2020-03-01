# 단지번호붙이기 # BFS
import sys
import collections

input = sys.stdin.readline


def bfs(length):
    q = collections.deque()
    cnt = 1
    for i in range(length):
        for j in range(length):
            q.append(a[i, j])  # [y,x] 좌표
            node = q.popleft()
            for idx in range(4):
                x = node[1] + i_x[idx]
                y = node[0] + i_y[idx]
                if 0 <= x <= n - 1 and 0 <= y <= n - 1:
                    if a[y][x] == 1 and visit[y][x] == 0:
                        q.append(visit[y][x])
                        visit[y][x] = 1
            cnt += 1
    return cnt


n = int(input())
a = [list(map(int, input().strip())) for _ in range(n)]

# 이동방향 4방향
i_y = [0, -1, 0, 1]
i_x = [-1, 0, 1, 0]

# 단지 리스트 d_list[]
d_list = []
# 한 단지 세는거 cnt

# 방문했다는 visit[]
visit = [[0] * n for _ in range(n)]

print(bfs(n))
