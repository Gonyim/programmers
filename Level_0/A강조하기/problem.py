def solution(myString):
    myString = myString.lower()  # 문자열을 모두 소문자로 변환
    answer = list(myString)  # 문자열을 리스트로 변환
    for i in range(len(answer)):
        if answer[i] == 'a':
            answer[i] = 'A'
    return ''.join(answer)  # 리스트를 다시 문자열로 변환