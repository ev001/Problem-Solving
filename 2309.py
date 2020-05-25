# 일곱 난쟁이 # 브루트포스

import itertools
import sys

input = sys.stdin.readline
arr = [int(input().strip()) for _ in range(9)]
arr.sort()
s = sum(arr)
combi = list(itertools.combinations(arr, 2))

for i in combi:
    r = s
    r -= (i[0] + i[1])
    if r == 100:
        arr = set(arr)
        arr -= {i[0], i[1]}
        print("\n".join(map(str, (list(arr)))))