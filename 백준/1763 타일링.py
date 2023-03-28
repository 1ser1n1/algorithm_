"""
li가 가질수 있는 경우의수
li[i-1]에서 2x1의 타일을 세로로 붙인 경우
li[i-2]에서 2x2의 타일을 붙인 경우
li[i-2]에서 2x1의 타일 두 개를 가로로 붙인 경우
"""
li = [0] * (N+1)
while True:
    try:
        N = int(input())

        for i in range(1, N+1):
            if i == 1:
                li[i] = i
            elif i == 2:
                li[i] = 3
            
            else:
                li[i] = li[i-1]+ (2*li[i-2])
        print(li[N])
        
        
    except:
        break

