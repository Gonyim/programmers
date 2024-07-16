def solution(myString, pat):
    for i in myString:
        if i == "A":
            i = "B"
        else:
            i = "A"
    if pat in myString:
        return 0
    else:
        return 1
