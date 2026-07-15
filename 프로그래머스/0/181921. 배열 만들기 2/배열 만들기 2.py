def solution(l, r):
    answer = [i for i in range(l, r + 1) if set(str(i)) <= set("05")]
    return answer or [-1]