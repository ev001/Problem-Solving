import sys

input = sys.stdin.readline

def greedy(times):
    next_time = 0
    min_time = 0
    for time in times:
        next_time += time
        min_time += next_time

    return min_time

if __name__ == "__main__":
    N = int(input())
    times = list(map(int, input().split()))
    times.sort()

    print(greedy(times))