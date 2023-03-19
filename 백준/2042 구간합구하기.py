"""
시간초과 -> 세그먼트 트리로 풀어야함
"""
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

#구간합 수정 및 출력
for i in range(M+K):
    a, b, c = map(int, input().split())
    #구간합 수정
    if a == 1:
        m = c - l[b-1] #현재 값과 바꿀 값의 오차
        l[b-1] = c
        for j in range(b-1, N): #바꾼 위치부터 오차를 더해줌
            list_sum[j] = list_sum[j] + m 
    #조건에 맞는 구간합 출력       
    else : 
        print(list_sum[c-1]-list_sum[b-1]+l[b-1])