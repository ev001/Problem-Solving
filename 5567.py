# 결혼식 # 구현, 그래프
import sys, collections

input = sys.stdin.readline


# print = sys.stdout.write

def bfs(start):
    q = collections.deque()
    q.append(start)

    while q:
        node = q.popleft()

        for next in v[node]:
            if check[next] == 0:
                # 다음 방문할 정점의 거리를 현재 정점의 거리 +1이 된다.
                check[next] = check[node] + 1
                q.append(next)


n, m = int(input()), int(input())

# 간선의 정보를 저장할 인접리스트
v = [[] for _ in range(n + 1)]

# 시작 정점으로 부터 거리 정보를 담을 리스트
check = [0] * (n + 1)

# 1. 간선의 정보를 입력받으면서 양방향 그래프로 만들어주기.
for _ in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

# 2. 시작 정점 거리를 1로 체크하고 BFS 탐색을 시작
check[1] = 1
bfs(1)

# 3. 처음 정점의 거리를 1로 잡아주어서 1과 친구인 정점들은 거리를 2로,
#    친구들의 친구는 거리를 3으로 하여 체크. 2와 3을 모두 세어준다.

print(check.count(2) + check.count(3))

# 다른 print 법
'''
    # for i in range(2, n + 1):
    #     if check[i] == 2 or check[i] == 3:
    #         result += 1

'''
