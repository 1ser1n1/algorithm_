from collections import Counter
def solution(s):
    dic = Counter(s)
    answer = [i for i in list(dic.keys()) if dic[i]==1]
    return "".join(sorted(answer))