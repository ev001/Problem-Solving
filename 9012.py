# 괄호 # 스택
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

for i in range(n):
    stack = deque(map(str, input().strip()))
    flag, l_paren, r_paren = False, 0, 0
    while stack:
        tmp = stack.pop()
        if tmp == '(':
            if l_paren:
                l_paren -= 1
            else:
                flag = True
                break
        else: # )
            if r_paren:
                r_paren -= 1
            else:
                l_paren += 1
    # print(i, l_paren, r_paren)
    if flag or l_paren or r_paren:
        print("NO")
    else:
        print("YES")

'''
다른풀이

def is_vps(x):
    stack = collections.deque()
    for i in x:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
 
    if len(stack) == 0:
        return True
 
    return False
 
 
T = int(input())
 
for _ in range(T):
    ip = sys.stdin.readline().strip()
 
    if is_vps(ip):
        print("YES")
    else:
        print("NO")

'''

'''
python에서 list의 경우에는 동적 array로 구현되어 있고 
deque의 경우 양방향 linked list의 형태로 구현되었다.

따라서 stack의 동작을 생각해보면 
동적 array와 linked-list의 append와 pop 연산은 둘다 O(1)임을 알 수 있다.

list가 더 빠른이유는 생성할때 동적 array의 경우가 더 빠르고, 
pop과 append 연산시에 같은 시간복잡도 일지라도 
linked list가 자신과 연결된 node의 주소값을 저장하는 과정과 
linked list의 끝을 가리키는 값 수정 등 여러 추가사항이 있어서 조금 더 느린것으로 예상된다.

deque가 list보다 빠른 경우는 
두 배열의 맨 앞에 추가하는 연산인 deque의 appendleft 와 list의 insert이다.

위의 경우에는 deque의 시간복잡도는 O(1) 이고, 
list는 동적 array 이므로 모든 요소를 왼쪽으로 옮기는 연산 때문에 O(n)의 시간복잡도를 갖는다.

따라서 stack을 활용할때는 list를, 
quque를 활용할때는 deque를 사용하는것이 유리할것이다.


'''
