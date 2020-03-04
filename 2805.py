# 나무자르기 # 이분탐색

import sys

input = sys.stdin.readline


def check(a, mid, m):
    cnt = 0

    for i in range(len(a)):
        if a[i] - mid > 0:
            cnt += a[i] - mid

    return cnt >= m


n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right, ans = 0, max(a), 0
while left <= right:
    mid = (left + right) // 2
    if check(a, mid, m):
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)