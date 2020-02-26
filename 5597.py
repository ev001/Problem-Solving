# 과제 안 내신 분..? # 구현

original = set(i for i in range(1, 31, 1))
a = set(int(input()) for _ in range(28))

for i in sorted(original - a): print(i)

'''
    set과 set 자료형의 특징인 차집합(-) 이용
    sorted 정렬은 set도 가능하며 정렬후 list 반환
    (sort는 None을 반환)

    cf) 교집합 : s1 & s2 , 합집합 s1 | s2  또는 s1.union(s2)
'''