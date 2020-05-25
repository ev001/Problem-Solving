# 우체국

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

sum = 0
for a in arr:
    sum += a[1]
sum /= 2
temp1 = 0
idx = 0
while temp1 <= sum:
    temp1 += arr[idx][1]
    idx += 1
print(arr[idx - 1][0])

