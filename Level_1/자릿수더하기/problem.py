def solution(n):
    answer = 0
    a = str(n)
    for i in range(0, len(a)):
        answer += int(a[i])
    return answer