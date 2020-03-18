# 퇴사 # DP

import sys

input = sys.stdin.readline

N = int(input())
t, p = [], []
d = [0] * 15
for i in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

ans = 0
for i in range(N):
    if i + t[i] <= N:
        d[i + t[i]] = max(d[i + t[i]], d[i] + p[i])
        ans = max(ans, d[i + t[i]])

    d[i + 1] = max(d[i + 1], d[i])
    ans = max(ans, d[i + 1])

print(ans)
