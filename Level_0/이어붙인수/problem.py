def solution(num_list):
    answer = 0
    a = ''
    b = ''
    for i in range(0, len(num_list)):
        if num_list[i] % 2 == 0:
            a += str(num_list[i])
        else:
            b += str(num_list[i])

    answer = int(a) + int(b)
    return answer