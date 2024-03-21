def solution(s):
    a = 0
    b = 0
    answer = ''
    for i in range(0, len(s)):
        if s[i] == 'p' or s[i] =='P':
            a += 1
        elif s[i] == 'y' or s[i] =='Y':
            b += 1
    if a == b:
        answer = True
    else:
        answer = False
        
    return answer