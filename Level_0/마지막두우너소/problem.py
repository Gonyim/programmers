def solution(num_list):
    if num_list[len(num_list) - 1] > num_list[len(num_list) - 2]:
        num_list.append(num_list[len(num_list) - 1] - num_list[len(num_list) - 2])
    else:
        num_list.append((num_list[len(num_list) - 1]) * 2)

    return num_list


# 진짜 그지같이 풀었네

def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)

    return num_list

# 뇌좀 열어라!!!!!