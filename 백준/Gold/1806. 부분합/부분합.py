import sys
input = sys.stdin.readline


N, M = map(int,input().split())
lst = list(map(int,input().split()))

s, e = 0, 1 #처음과 끝
temp = lst[s] #현재까지 구간합 값
min_len = 987654321

while s < N:
    if temp >= M: #비교하려는 값보다 현재 합이 더 클때
        min_len = min(min_len, e-s) #현재 구간합 길이 저장
        
        temp -= lst[s] #구간합에서 s포인트값 빼기
        s += 1 #S 한칸 전진
        
        if temp <M and e < N:
            temp += lst[e] #e포인트 값 저장
            e += 1 #e 한칸 전진
            
    else: #temp < M 비교대상이 더 클 때
        if e >= N: #e포인트가 리스트 길이를 넘어가면 stop
            break
        
        #e포인트 저장 후 전진
        temp += lst[e]
        e += 1
        
        #현재 길이가 최소구간 합길이보다 길때
        if e-s >= min_len:
            temp -= lst[s]
            s += 1
            
            
print(0 if min_len > N else min_len)
        