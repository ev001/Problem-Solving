import sys

input = sys.stdin.readline

a = input().strip()
plus, minus = [], []
element = ""
isMinus = 0

for i in range(len(a)):
    if a[i] == "+":
        if isMinus == 0:
            plus.append(int(element))
            element = ""
        else:
            minus.append(int(element))
            element = ""
    elif a[i] == "-":
        if isMinus == 0:
            plus.append(int(element))
            element = ""
            isMinus = 1
        else:
            minus.append(int(element))
            element = ""

    else:
        element += a[i]
        if len(a) - 1 == i:
            if isMinus == 0:
                plus.append(int(element))
            else:
                minus.append(int(element))

print(sum(plus) - sum(minus))

'''
고민했던점
    어떻게 숫자 요소들을 하나로 묶을것인가 
    = > 각각의 str을 더해서 int로 묶어서 plus,minus 리스트에 저장.
    
'''