# 기타줄 # 그리디

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pack, one = 999999, 999999
res = []

for i in range(M):
    g, s = map(int, input().split())
    pack, one = min(pack, g), min(one, s)

if N > 6:
    q, r = divmod(N, 6)
    res = [pack * (q + 1), pack * q + one * r, one * N]
    if r * one > pack:
        res = min(res[0:2])
    else:
        res = min(res)
else:
    res = min(pack, one * N)

print(res)
