import sys

input = sys.stdin.readline

# a = [list(map(str,input().split())) for _ in range(N)]
# 위와 같이 리스트a 내 요소를 str, int로 구분이 불가능.

N = int(input())
a = []
for _ in range(N):
    x, y, z, w = input().split()
    a.append((x, int(y), int(z), int(w)))
a.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in a:
    print(i[0])
