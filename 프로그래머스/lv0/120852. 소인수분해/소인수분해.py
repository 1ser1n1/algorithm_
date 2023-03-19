def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            if d not in answer:
                answer.append(d)
            n = n/d
        else:
            d = d + 1
    return answer