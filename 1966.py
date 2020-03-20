# 프린터 큐 # 시뮬레이션

import sys
from collections import deque

input = sys.stdin.readline

tc = int(input().strip())

for _ in range(tc):
    N, M = map(int, input().split())
    q, cp_q = deque(), deque()
    for idx, x in enumerate(list(map(int, input().split()))):
        q.append(x)
        if idx == M:
            cp_q.append(1)
        else:
            cp_q.append(0)

    cnt = 0
    while q:
        if q[0] == max(q):
            cnt += 1
            if cp_q[0] == 1:
                print(cnt)
                break
            else:
                q.popleft()
                cp_q.popleft()
        else:
            q.rotate(-1)
            cp_q.rotate(-1)
