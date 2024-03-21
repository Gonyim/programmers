def solution(n):
    sqrt_n = int(n ** 0.5)  # n의 제곱근을 정수형으로 계산
    if sqrt_n * sqrt_n == n:  # 제곱근이 정수인 경우
        return (sqrt_n + 1) ** 2
    else:
        return -1  # 제곱근이 정수가 아닌 경우