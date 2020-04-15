# DNA # 그리디

import sys
from operator import itemgetter

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(n)]

ans = list()
for i in range(m):
    case = dict()
    for j in range(n):
        if arr[j][i] in case:
            case[arr[j][i]] += 1
        else:
            case[arr[j][i]] = 1
    s = sorted(case.items(), key=itemgetter(1, 0))
    ans.append(max(s, key=itemgetter(1))[0])

print("".join(map(str, ans)))

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != ans[j]:
            cnt += 1
print(cnt)

'''
정렬관련 참고 문서
https://docs.python.org/ko/3/howto/sorting.html
https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
https://hashcode.co.kr/questions/495/dictitems%EC%99%80-dictiteritems%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90%EC%9D%80-%EB%AD%94%EA%B0%80%EC%9A%94

dict.items(): dict의 (key, value) 쌍을 복사한 list를 return

'''