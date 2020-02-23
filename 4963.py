# 1. 이동가능한지(map[][]=1)
# 2. 맵을 벗어나지않는 유효한 범위(nx, ny의 범위체크)
# 3. 마지막으로 한번도 방문한적이 없는 곳 (visit=0)이라면,
#   함수를 재귀호출하여 visit 값을 1로 변경해주기.
#   더이상 주변에 탐색가능한 섬이 없을 때, DFS 함수는 종료되고 cnt 값이 1 증가.
import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def dfs(x, y):
    visit[x][y] = 1
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= h or nx < 0 or ny >= w or ny < 0:
            continue
        if a[nx][ny] == 1 and visit[nx][ny] == 0:
            dfs(nx, ny)
    return 0


# 방향 8방향 (위,아래,좌,우 + 대각선 4방향)
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]

# 지도 초기화 부분
while True:
    w, h = map(int, input().split())

    # 0이면(not w) 끝내기.
    if not w:
        break
    # 지도 만들기
    a = [list(map(int, input().split())) for _ in range(h)]
    # visit 0으로 초기화
    print(a)
    visit = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == 1 and visit[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
