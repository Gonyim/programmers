def solution(arr, n):
    # arr의 길이가 홀수일 경우
    if len(arr) % 2 != 0:
        for i in range(0, len(arr), 2):
            arr[i] += n
    # arr의 길이가 짝수일 경우
    else:
        for i in range(1, len(arr), 2):
            arr[i] += n
    return arr
