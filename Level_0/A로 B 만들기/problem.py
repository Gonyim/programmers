def solution(before, after):
    answer = before
    answer[0] = before[0]
    answer[-1] = after[-1]
    return answer