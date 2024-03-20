def solution(s):
    answer = 0
    if s[0] == "-":
        answer = int(s.replace('-', '')) * -1
    else:
        answer = int(s)
    return answer