from bisect import bisect_left

def solve(miuns, plus):
    """
    miuns: 음수 리스트(성별 무관)
    plus: 양수 리스트(성별 무관)
    """
    global res
    miunsIndex = 0 #음수 리스트의 시작 인덱스
    plusIndex = len(plus) -1 #양수 리스트의 시작 인덱스
    
    while miunsIndex < len(miuns) and plusIndex >= 0:
        if miuns[miunsIndex] + plus[plusIndex] < 0: #두 수의 합이 음수라면 한쌍의 커플 완성
            miunsIndex += 1
            plusIndex -= 1
            res +=1
        else: 
            plusIndex -= 1 #제일 작은 음수와 제일 큰 양수의 합이 0 이상일 경우, 다음 음수를 더하더라도 0이상이 므로 양수의 포인트만 옮겨줌



N = int(input())
men = sorted(list(map(int, input().split())))
women = sorted(list(map(int, input().split())))
res = 0

manPlusIndex = bisect_left(men, 0)  # 남자 리스트에서 양수가 시작되는 인덱스
womanPlusIndex = bisect_left(women, 0)  # 여자 리스트에서 양수가 시작되는 인덱스

solve(men[:manPlusIndex], women[womanPlusIndex:])  # 남자의 음수, 여자의 양수
solve(women[:womanPlusIndex], men[manPlusIndex:])  # 여자의 음수, 남자의 양수

print(res)

