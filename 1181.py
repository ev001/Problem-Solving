# 단어 정렬 # 정렬

import sys

input = sys.stdin.readline

n = int(input())

# string 으로 정렬
a = list()
for _ in range(n):
    e = input().strip()
    a.append([len(e), e])

# 단어수 작은것부터, 같을경우 알파벳 빠른순
# 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

a.sort(key=lambda x: (x[0], x[1]))

for idx, e in enumerate(a):
    if not idx == n-1 and a[idx][1] == a[idx+1][1]:
        pass
    else:
        print(e[1])
