def solution(absolutes, signs):
    answer = 0
    a = ''
    b = 0
    c = 0
    for i in range(0,len(absolutes)):
        a = str(signs[i])
        if a == 'True':
            b += int(absolutes[i])
        else:
            c += int(absolutes[i])
            
        answer = b - c
    return answer