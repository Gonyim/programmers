answer = []
n = 111
m = 333

if n > m:
    if n % m == 0:
        answer.append(m)
    elif m % n == 0:
        answer.append(n)
    else:
        answer.append(1)

if n > m:
    if n % m == 0:
        answer.append(n)
    else:
        answer.append(n*m)
elif m > n:
    if m % n == 0:
        answer.append(m)
    else:	
        answer.append(n*m)
else:
    answer.append(1)

print(answer)