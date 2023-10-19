def fibonacci3(n):
    if n<=0:
        return 0
    elif n<=3:
        return 1
    sequence = [1, 1, 1, 3]
    num = 0
    while num <= n:
        real_start = sum(sequence[-3:])
        
        if len(sequence) == n:
            return sequence[-1]
        else:
            sequence.append(real_start)
            num += 1
print(fibonacci3(9))