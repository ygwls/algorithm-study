def solution(a, b):
    ab = int(str(a) + str(b))
    x = 2 * a * b
    
    return max(ab, x)