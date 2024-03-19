def solution(x, n):
    answer = []
    
    if x > 0:
        for i in range(x, x*n+1, x):
            answer.append(i)
            
    elif x < 0:
        for i in range(x, x*n-1, x):
            answer.append(i)
        
    else:
        for i in range(1,n+1):
            answer.append(0)
            
    return answer