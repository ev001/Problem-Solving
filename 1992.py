# 쿼드트리 # 분할 정보

import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def same(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if a[i][j] != a[x][y]:
                return False
    return True


def solve(x, y, n):
    if same(x, y, n):
        print(a[x][y], end="")
        return
    else:
        print("(", end="")
        m = n // 2
        for i in range(2):
            for j in range(2):
                solve(x + m * i, y + m * j, m)
        print(")", end="")


num = int(input())
a = [list(map(int, input().strip())) for _ in range(num)]

solve(0, 0, num)


'''
    same의 범위를 잡지 못해서 시간을 많이 씀.
'''
