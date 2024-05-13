def solution(num_list):
    answer = []
    a = 0
    b = 0
    for i in num_list:
        if i % 2 == 0:
            b += 1
        else:
            a += 1

    answer.append(b)
    answer.append(a)
    return answer