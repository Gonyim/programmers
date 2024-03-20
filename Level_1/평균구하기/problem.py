def solution(arr):
    answer = 0
    s = 0
    for i in range(0, len(arr)):
        s += arr[i]
    
    answer = s/len(arr)
    return answer