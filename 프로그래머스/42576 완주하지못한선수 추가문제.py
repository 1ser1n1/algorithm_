
#solution 1
def solution1(participant, completion):
    
    name = [] #완주 못한 선수를 담을 리스트
    
    for j in participant:
        try:
            del completion.remove(j)
        except:
            append(j)
        
    return name[0]

1
2
3
4
5
6
7#solution 2
import collections


def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]