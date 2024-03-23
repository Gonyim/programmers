def solution(s):
    a = ['0','1','2','3','4','5','6','7','8','9']
    b = []
    count = 0
    b = sorted(s)
    for i in b:
        if i in a:
            count += 1
            
    if count == len(s) and len(s) == 4:
        answer = True
    elif count == len(s) and len(s) == 6:
        answer = True
    else:
        answer = False
    return answer