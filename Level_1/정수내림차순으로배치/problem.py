def solution(n):
    answer = 0
    b = ''
    a = list(map(int,str(n)))
    a.sort(reverse=True)
    for i in range(0, len(a)):
        b += str(a[i])
    answer = int(b)
    return answer