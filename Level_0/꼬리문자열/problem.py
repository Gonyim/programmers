def solution(str_list, ex):
    answer = ''
    for i in range(0, len(str_list)):
        if ex in str_list[i]:
            pass
        else:
            answer += str_list[i]
    return answer