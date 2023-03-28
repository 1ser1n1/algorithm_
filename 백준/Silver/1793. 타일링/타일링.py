li = [0 for i in range(251)]
while(True):
    try:
        N = int(input())

        for i in range(N+1):
            if i == 1 or i == 0:
                li[i] = 1
            elif i == 2:
                li[i] = 3
            
            else:
                li[i] = li[i-1]+ (2*li[i-2])
        print(li[N])
        
        
    except:
        break


