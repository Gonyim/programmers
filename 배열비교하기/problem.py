def solution(arr1, arr2):
    arr1_sum = 0
    arr2_sum = 0
    if len(arr1) > len(arr2):
        return -1
    elif len(arr1) == len(arr2):
        for i in range(0, len(arr1)):
            arr1_sum += arr1[i]
            arr2_sum += arr2[i]
            if arr1_sum >= arr2_sum:
                return 1
            elif arr1_sum <= arr2_sum:
                return -1
            else:
                return 0
    else:
        return 1
