N = int(input())

ans = [0] * (N+1)

for i in range(1, N+1):
    if i == 1 or i == 2:
        ans[i] = i
    
    else:
        ans[i] = ans[i-1] + ans[i-2]
        
print(ans[N]%10007)