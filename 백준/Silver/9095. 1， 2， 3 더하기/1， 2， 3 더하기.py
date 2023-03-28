T = int(input())

for i in range(T):
    n = int(input())
    li = [0] *(n+1)
    for i in range(1,n+1):
        if i == 1:
            li[i] = 1
        elif i == 2:
            li[i] = 2
        elif i == 3:
            li[i] = 4
        
        else:
            li[i] = li[i-1] + li[i-2] + li[i-3]
    
    print(li[n])