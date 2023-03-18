import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
l = [] #N개의 수

for i in range(N):
    num = int(input())
    l.append(num)

list_sum = [0] * N

#구간합 배열 저장
for i in range(0, N):
    if i == 0:
        list_sum[i] = l[i]
    else:    
        list_sum[i] = list_sum[i-1] + l[i]

print(list_sum)
for i in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        m = c - l[b-1]
        l[b-1] = c
        for j in range(b-1, N):
            list_sum[j] = list_sum[j] + m
            
    else : 
        print(list_sum[c-1]-list_sum[b-1]+l[b-1])