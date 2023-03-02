N = int(input())
S = input()
log = ['00']
x, y = 0, 0
for s in S:
    if s == "R":
        x += 1
    if s == "L":
        x -= 1
    if s == "U":
        y += 1
    if s == "D":
        y -= 1
    log.append(str(x)+str(y))
if len(list(set(log))) != len(log):
    print("Yes")
else:
    print("No")
