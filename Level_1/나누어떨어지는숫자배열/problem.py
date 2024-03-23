def solution(arr, divisor):
    count = 0
    answer = []
    for i in range(0,len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            count += 1
            
    if count == 0 :
        answer.append(-1)
        
        # answer = list(set(answer))
    answer.sort()
    return answer