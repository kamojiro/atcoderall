s = input()
l = len(s)
V = [0]*l
ans = 0
two = 0
five = 0
for i in range(l):
    if s[i] == "2":
        two += 1
    else:
        five += 1
    if two < five:
        ans = -1
        break
    ans = max( ans, two-five)
if two == five:
    print(ans)
else:
    print(-1)
