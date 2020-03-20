# 기타줄 # 그리디

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
# n: 사야하는 기타줄 개수, m 브랜드 개수
# arr[0] : 6개 세트 가격 arr[1] 낱개 가격


# 경우의 수
# 1. 세트로만 구성
# n을 6으로 나눈다?
# 세트 1개 몫이 1이고 나머지가 없으면 세트 1개
# 몫이 1이상이고 나머지가 있으면 세트 2개
# 몫이 2이고 나머지가 없으면 / 있으면 ...

ans = 0
# 몫이 0이면
if not N // 6:
    ans = arr[0]
else:
    # 몫은 있는데 나머지 유무로 나누기
    if not N % 6:  # 나머지 없음
        ans = max(ans, arr[0] * (N // 6))
    else:  # 나머지 있음
        ans = max(ans, arr[0] * ((N // 6) + 1))

        # 2. 세트 + 낱개로 구성
        # 3. 낱개로 구성.
