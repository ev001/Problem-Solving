# 문서 검색 # 그리디
import sys

input = sys.stdin.readline

arr, a = input().strip(), input().strip()
ans = 0
len_a = len(a)
for i in range(len(arr)):
    cur_idx, max_count = -1, 0
    for j in range(i, len(arr)):
        if j > cur_idx:
            if arr[j:j + len_a] == a:
                cur_idx = j + len_a-1
                max_count += 1
        if max_count > ans:
            ans = max_count
print(ans)

'''
문자열 받고 strip 해줘야 개행문자를 제거해줌.
'''