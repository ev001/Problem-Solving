# 트리의 순회 # 분할 정복

import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def solve(i_f, i_e, p_f, p_e):
    if i_f > i_e or p_f > p_e:
        return
    root = postOrder[p_e]
    print(root, end=' ')
    p = position[root]

    left = p - i_f
    solve(i_f, p - 1, p_f, p_f + left - 1)
    solve(p + 1, i_e, p_f + left, p_e - 1)


n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

position = [0] * 100001
for i in range(n):
    position[inOrder[i]] = i

solve(0, n - 1, 0, n - 1)

'''
    파이썬은 재귀 깊이가 얕다.
    재귀 최대 깊이를 조정해줘야한다.
    sys.setrecursionlimit(10 ** 8)

'''