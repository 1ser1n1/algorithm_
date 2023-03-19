import sys
input = sys.stdin.readline
"""
세그먼트 트리로 풀어야함
메모리 초과
"""

N, M, K = map(int, input().split())

l = [] #N개의 수

for i in range(N):
    num = int(input())
    l.append(num)

mult_l = [0] * N

for i in range(N):
    if i == 0:
        mult_l[i] = l[i]
    else:
        mult_l[i] = mult_l[i-1] * l[i]
        
#구간곱 수정 및 출력
for i in range(M+K):
    a, b, c = map(int, input().split())
    #구간곱 수정
    if a == 1:
        for j in range(b-1, N): #바꾼 위치부터 곱해줌
            mult_l[j] = mult_l[j]/l[b-1] * c
        l[b-1] = c
    #조건에 맞는 구간합 출력       
    else : 
        print(int(mult_l[c-1]/mult_l[b-1] * l[b-1]))