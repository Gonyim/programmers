def solution(array):
    # 빈도를 저장할 딕셔너리
    frequency = {}

    # 각 숫자의 빈도를 계산
    for num in array:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # 최대 빈도를 찾습니다.
    max_freq = max(frequency.values())

    # 최대 빈도가 여러 개의 숫자에서 나타나는지 확인합니다.
    modes = [num for num, freq in frequency.items() if freq == max_freq]

    # 최빈값이 여러 개면 -1을 반환, 그렇지 않으면 최빈값을 반환
    if len(modes) > 1:
        return -1
    else:
        return modes[0]


# 예시 테스트
array = [1, 2, 2, 3, 3, 4]
print(solution(array))  # 출력: -1 (2와 3이 같은 빈도로 최빈값)
