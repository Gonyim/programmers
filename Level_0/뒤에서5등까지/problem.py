def solution(num_list):
    num_list.sort()
    while len(num_list) > 5:
        num_list.pop()
    return num_list
