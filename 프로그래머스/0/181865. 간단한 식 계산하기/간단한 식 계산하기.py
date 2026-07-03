def solution(binomial):
    a, op, b = binomial.split()
    a, b = map(int, (a, b))
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b