# 시리얼 번호 # 정렬

# 선택정렬로 구현
# 길이가 짧은게 앞으로
# 길이가 같다면 숫자 합 작은게 앞으로.
# 그것도 안되면 사전순으로.

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(str, input().strip())) for _ in range(n)]


def sumNumber(a):
    str_0, str_9 = '0', '9'
    idx = []
    for k in a:
        if str_0 <= k <= str_9:
            idx.append(int(k))
    return sum(idx)


def sortDic(a, b):
    for k in range(len(a)):
        if a[k] > b[k]:
            return True
        elif a[k] < b[k]:
            return False


for i in range(len(arr) - 1):
    min_idx = i
    for j in range(i + 1, len(arr)):
        # 길이비교
        if len(arr[min_idx]) > len(arr[j]):
            min_idx = j
            continue
        elif len(arr[min_idx]) < len(arr[j]):
            continue

        else:  # 길이가 같은경우, 숫자비교
            if sumNumber(arr[min_idx]) > sumNumber(arr[j]):
                min_idx = j

            elif sumNumber(arr[min_idx]) < sumNumber(arr[j]):
                continue

            else:  # 숫자까지 같은경우, 사전순 정렬 (True면 i가 더크다)
                if sortDic(arr[min_idx], arr[j]):
                    min_idx = j

                elif not sortDic(arr[min_idx], arr[j]):
                    continue
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

for i in arr:
    print("".join(i))
