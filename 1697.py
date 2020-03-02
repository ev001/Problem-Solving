# 숨바꼭질 #bfs
import sys
from collections import deque

input = sys.stdin.readline


def solve():
    while q:
        # cur :  current
        cur = q.popleft()
        if cur == k:
            return visit[cur]
        nextPos(cur - 1, cur)
        nextPos(cur + 1, cur)
        nextPos(cur * 2, cur)


def nextPos(next, cur):
    # next 지점이 범위 내에 있고,
    # 한번도 방문하지 않았거나,
    # 최소 시간으로 해당 방을 방문한 경우
    if 0 <= next < maxSize and \
            (visit[next] == 0 or visit[cur] + 1 < visit[next]):
        visit[next] = visit[cur] + 1
        q.append(next)


# n : 내 위치, k : 동생위치
n, k = map(int, input().split())
maxSize = 100001
visit = [0] * maxSize
q = deque([n])
print(solve())
