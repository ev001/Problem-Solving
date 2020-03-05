# 배열 합치기 # 분할 정복

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []
i, j = 0, 0

while i < n or j < m:
    if j >= m or (i < n and a[i] <= b[j]):
        ans.append(a[i])
        i += 1
    else:
        ans.append(b[j])
        j += 1

for i in ans:
    print(i, end=' ')

'''
    고려할 점 
    이미 정렬이 되어있는 상황 고려
    while 및 if 조건
'''