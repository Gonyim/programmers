def solution(my_string, is_prefix):
    answer = 0
    if len(is_prefix) > len(my_string):
        return 0
    elif len(is_prefix) <= len(my_string):
        for i in range(0, len(is_prefix)):
            if my_string[i] == is_prefix[i]:
                answer = 1
            else:
                return 0
    return answer