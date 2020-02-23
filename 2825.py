'''
N: WOMEN , M: MAN , K : INTERN
    * 하나의 팀을 만드는 조건 1~3
        1. N + M >= K + 3
        2. N >= 2
        3.M >= 1
    * 위의 조건을 만족하면
        N -= 2
        M -= 1
'''

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    team_count = 0

    n, m, k = map(int, input().split())
    while True:
        if n + m >= k + 3 and n >= 2 and m >= 1:
            n -= 2
            m -= 1
            team_count += 1
        else:
            break
    print(team_count)
