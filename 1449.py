# 수리공 항승 # 그리디

import sys

input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))

start, cnt = 0, 0
for a in sorted(arr):
    if start < a:
        start = a + l - 1
        cnt += 1
print(cnt)
