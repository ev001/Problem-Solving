# 랜선 자르기 # 이분탐색

import sys

input = sys.stdin.readline


def check(x):
    cnt = 0
    for i in range(n):
        cnt += (a[i] // x)

    return cnt >= m


n, m = map(int, input().split())
a = [int(input().strip()) for _ in range(n)]

ans = 0
left, right = 1, max(a)

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        if ans < mid:
            ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
