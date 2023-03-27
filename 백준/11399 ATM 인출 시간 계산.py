import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))
num = sorted(num)
time = []

for i in range(N):
    time.append(sum(num[:i+1]))
    
print(sum(time))