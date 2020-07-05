import sys

input = sys.stdin.readline

n = str(input()).strip()
change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

letter_cnt = 0
cnt = 0
for c in change:
    if c in n:
        count = n.count(c)
        cnt += count
        n = n.replace(c, ' ')

print(cnt + len(n.replace(' ', '')))

# str.strip : 앞 뒤 공백 제거에 사용
# str.replace : 모든 공백 제거에 사용

'''
생각해보니 따로 변수를 둘 필요도 없이
2개 이상의 크로아티아 알파벳은 하나로 count 되니까
입력받은 string 에서 크로아티아 알파벳을 발견한다면
* 으로 바꾸고 문자열의 길이를 출력하면 된다.

for c in change:
    n = n.replace(c, '*')

print(len(n))
'''
