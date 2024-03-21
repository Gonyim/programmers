def solution(x):
    b = 0
    a = list(map(int,str(x)))
    for i in range(0,len(a)):
        b += a[i]
        if x % b == 0:
            answer = True
        else:
            answer = False
    return answer