# 로또 # 그래프

import sys

input = sys.stdin.readline


def dfs(start, depth):
    if depth == 6:
        for x in combi:
            print(x, end=' ')
        print('')
        return
    for i in (start, a[0]):
        print(a[0])
        combi[depth] = lotto[i]
        dfs(i + 1, depth + 1)


while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    lotto = [0] * 13
    for idx, x in enumerate(a[1:]):
        lotto[idx] = x

    combi = [0] * 13
    dfs(0, 0)
    print('\n')
