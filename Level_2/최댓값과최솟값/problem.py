s = "-1 -3 -2 -4"

# a = s.split()

answer = ''
answer = s.split()
answer.sort()
answer = answer[0],answer[-1]
print(answer)