n = int(input())
num = n
cnt = 0 #사이클 수
while True:
    a = num//10 #십의자리수
    b = num%10 #1의 자리 수
    c = (a + b) % 10 #1의 자리 수
    num = (b*10) + c
    
    cnt = cnt + 1 #사이클 수 더하기
    if(num == n) : 
        break
print(cnt)