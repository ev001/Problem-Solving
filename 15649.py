# N과 M(1) # 백트래킹
import sys

sys.setrecursionlimit(10 ** 9)

'''
    * visit ans depth 변수 사용

    visit : 제시된 수들이 쓰였는지 확인 (False로 초기화)
    depth = 리스트에 들어있는 개수 (0 으로 초기화)
    ans = 리스트 수들 ans[1 ~ k 까지]

'''

n, m = map(int, input().split())
visit = [False] * n
ans = []


# 현재 depth 까지 개수를 택
def solve(depth):
    if depth == m:  # m개를 모두 택했으면
        print(' '.join(map(str, ans)))
        return

    for i in range(len(visit)):
        if not visit[i]:
            visit[i] = True
            ans.append(i + 1)  # i + 1인 이유는 i가 0부터 최대수 -1 까지라서.
            solve(depth + 1)
            visit[i] = False
            ans.pop()

solve(0)
