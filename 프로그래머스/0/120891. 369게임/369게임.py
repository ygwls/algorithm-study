def solution(order):
    return sum(num in "369" for num in str(order))