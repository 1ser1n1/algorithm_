import sys
input = sys.stdin.readline

N = int(input())

xy_list = [0] * N
for i in range(N):
    xy_list[i] = list(map(int, input().split()))
    
xy_list.sort(key = lambda x: (x[1], x[0]))
for i in xy_list:
    print(i[0], i[1])