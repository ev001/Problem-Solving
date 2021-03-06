#  이전 순열

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


def prev_permutation():
    i = n - 1
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1

    if i <= 0:
        return False

    j = n - 1
    while i > 0 and arr[j] >= arr[i - 1]:
        j -= 1

    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    j = n - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return True


if not prev_permutation():
    print(-1)

else:
    print(" ".join(map(str,arr)))
