import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
mydeque = deque() #deque 자료구조 활용
now = list(map(int, input().split()))

for i in range(N): 
    while mydeque and mydeque[-1][0] > now[i]: #deque안의 마지막 값이 지금 넣으려는 값보다 크면 deque 마지막 값 삭제
        mydeque.pop()
    mydeque.append((now[i], i))
    
    if i - L >= mydeque[0][1]: #슬라이딩 박스에 포함되지 않으면 삭제
        mydeque.popleft()
        
    print(mydeque[0][0], end = " ")