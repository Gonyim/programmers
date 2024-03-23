def solution(arr):
    answer = arr.copy()
    a = arr.copy()
    a.sort()
    if len(arr) > 1:
        answer.remove(a[0])
    else:
        answer[0] = -1
        
    return answer