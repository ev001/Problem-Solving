# 나이순 정렬 # 정렬
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(str, input().split())) for i in range(n)]

# 나이 순, 나이가 같으면 가입한 순

arr.sort(key=lambda x: int(x[0]))

for e in arr:
    print(e[0], e[1])
