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


'''
# 정규표현식을 사용한 풀이
import sys, re
input = lambda :sys.stdin.readline().rstrip()

def sol(st):
    st = re.sub('[A-Z]','',st)
    sum_ = sum(map(int,st))
    return sum_

if __name__ == '__main__':
    n = int(input())
    res = list()
    for _ in range(n):
        a = input()
        temp = [len(a), sol(a), a]
        res.append(temp)
    res.sort()
    for i in res:
        print(i[2])

# 다른 풀이
n=int(input())

arry=[]
for _ in range(n):
    count=0
    a=input()
    for i in a:
       if i.isdigit():
           count+=int(i)
    arry.append([a,count])

arry.sort(key=lambda arry:(len(arry[0]),arry[1],arry[0]))

for x in arry:
    print(x[0])

'''