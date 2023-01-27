from collections import deque

problem = deque([])
while True:
    string = input()
    if string == "문제":
        problem.append("1")
    if len(problem) > 0 and string == "고무오리":
        problem.popleft()
    elif string == "고무오리":
        problem.append("1")
        problem.append("1")
    if string == "고무오리 디버깅 끝":
        break
if len(problem) == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")