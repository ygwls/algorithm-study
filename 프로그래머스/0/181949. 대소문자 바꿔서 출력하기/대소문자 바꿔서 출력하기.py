str = input()

answer = ""

for ch in str:
    if ch.isupper():
        answer += ch.lower()
    else:
        answer += ch.upper()
        
print(answer)