# 효율적인 해킹 # 그래프

import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for i in range(n + 1)]

# dfs로 최대 탐색 횟수를 찾고, 그탐색 횟수를 가진 숫자를 리턴.

for i in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)


def dfs(node):
    infection[node] = True
    global cnt
    cnt += 1
    for i in range(len(arr[node])):
        print("start:", node, arr[node])
        if arr[node][i]:
            if not infection[arr[node][i]]:
                dfs(arr[node][i])


depth_list = []
max_infection = 0
for i in range(1, n + 1):
    infection = [0] * (n + 1)
    cnt = 0
    dfs(i)
    depth_list.append((i, cnt))

    if max_infection < cnt:
        max_infection = cnt

for e in depth_list:
    if max_infection == e[1]:
        print(e[0], end=" ")
