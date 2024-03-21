def solution(n):
    answer = []
    a = 0
    a = str(n)
    for i in range(0,len(a)):
        answer.append(int(a[len(a)-i-1]))
    return answer