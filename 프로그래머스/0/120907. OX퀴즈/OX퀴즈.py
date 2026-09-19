def solution(quiz):
    answer = []
    
    for q in quiz:
        x, op, y, _, z = q.split()
        x, y, z = map(int, (x, y, z))
        
        if op == "+":
            result = x + y
        else:
            result = x - y
            
        answer.append("O" if result == z else "X")
        
    return answer