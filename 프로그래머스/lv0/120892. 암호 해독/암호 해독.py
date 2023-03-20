def solution(cipher, code):
    cipher = "0" + cipher
    answer = list(map(lambda x: cipher[x] if x%code==0 else "", range(1,len(cipher))))
    
                    
    return "".join(answer)