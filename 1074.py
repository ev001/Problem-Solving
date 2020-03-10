# Z # 분할 정복

import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def power(k):
    return 2 ** k


def solve(n, x, y):
    if n == 1:
        return 2 * x + y
    else:
        if x < power(n - 1):
            if y < power(n - 1):
                return solve(n - 1, x, y)
            else:
                return solve(n - 1, x, y - power(n - 1)) + power(2 * n - 2)
        else:
            if y < power(n - 1):
                return solve(n - 1, x - power(n - 1), y) + power(2 * n - 2) * 2
            else:
                return solve(n - 1, x - power(n - 1), y - power(n - 1)) + power(2 * n - 2) * 3;


n, r, c = map(int, input().split())

print(solve(n, r, c))
