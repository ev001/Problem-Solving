import sys

input = sys.stdin.readline


# x 로부터 10 y로 부터 10 은 모두 1로 칠하기
def check_map(x, y):
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if m[i][j] != 1:
                m[i][j] = 1


N = int(input().strip())
m = [[0] * 100 for i in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    check_map(x, y)

_sum = 0
for i in m:
    _sum += sum(i)
print(_sum)