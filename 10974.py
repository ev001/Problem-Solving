# 모든 순열

from itertools import permutations

n = int(input())

a = list(permutations([i for i in range(1, n + 1)]))
for e in a:
    print(" ".join(map(str, e)))
