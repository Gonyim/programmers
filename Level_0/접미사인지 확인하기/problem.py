def solution(my_string, is_suffix):
    answer = 0
    if len(is_suffix) > len(my_string):
        return 0
    else:
        for i in range(1, len(is_suffix)):
            if my_string[-i] == is_suffix[-i]:
                answer = 1
            else:
                return 0
    return answer