def solution(numbers):
    answer = 0
    for i in range(0, len(numbers)):
        answer += numbers[i]
        
    answer = 45 - answer
    return answer

# 1. 0~9 까지의 리스트
# 2. 여기서 찾을수 없는 0~9 까지의 숫자를 모두 더한 수를 리턴

# 뭐가 있을까.. while문 쓰다 포기..