# 부등호 # 그리디 # 위상 정렬

n = int(input())
sign = input().split()
c = [False] * 10
max, min = "", ""


def possible(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j
    return True


def solve(cnt, s):
    global max, min
    if cnt == n + 1:
        if not len(min):  # 성립하는 값의 가장 최소값이됨(아래의 for 문이 0에서부터 돌기 때문에.)
                          # 그이후에 들어오는값에는 전부 max로 넘어가게 되고, max가 계속 갱신되는 것.
            min = s
        else:
            max = s
        return
    for i in range(10):
        if not c[i]:
            if cnt == 0 or possible(s[-1], str(i), sign[cnt - 1]):
                c[i] = True
                solve(cnt + 1, s + str(i))
                c[i] = False


solve(0, "")
print(max)
print(min)

##########################################
############## 시행착오들ㅜ ###############
##########################################

'''
# 삽질 1. 메모리초과

k = int(input())
signList = list(map(str, input().split()))
def printNum(p):
    for e in p:
        list_e = list(e)
        num = ''
        if validate(0, list_e):  # True 일 때 (부등호 양식을 지켰으면)
            for i in list_e:
                num += str(i)
            print(num)
            break


min = list(permutations(minNums))
max = list(permutations(maxNums))
printNum(max)
printNum(min)


def validate(cnt, numList):  # 0 , 0 1
    if cnt == k:
        return True

    if signList[cnt] == '>':
        if numList[cnt] > numList[cnt + 1]:
            return validate(cnt + 1, numList)
        else:
            return False
    elif signList[cnt] == '<':
        if numList[cnt] < numList[cnt + 1]:
            return validate(cnt + 1, numList)
        else:
            return False
'''

'''
# 삽질 2. 메모리초과
from itertools import permutations

k = int(input())
signList = list(map(str, input().split()))

minNums = [i for i in range(k + 1)]
maxNums = [i for i in range(9, 8 - k, -1)]

p1 = list(permutations(maxNums))
p2 = list(permutations(minNums))

def createList():
    #possible Num
    arr = [0] * k
    cnt = [0] * k 
    for j in range(k):
        for i in range(9):
            arr[j] = i


def find(p):
    for e in p:
        cnt = 0
        for i in range(k):  # 부등호 개수 + 1 = 최대 자리수.
            if signList[i] == '<':
                if e[i] < e[i + 1]:
                    cnt += 1
                    continue
                else:
                    break
            elif signList[i] == '>':
                if e[i] > e[i + 1]:
                    cnt += 1
                    continue
                else:
                    break
        if cnt == k:
            print(''.join([str(l) for l in e]))
            break


find(p1)
find(p2)

'''
