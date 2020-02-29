# 음식평론가 # 구현 # 수학
import sys

input = sys.stdin.readline


def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


s, m = map(int, input().split())
print(m - GCD(s, m))