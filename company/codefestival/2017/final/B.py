from collections import Counter
S = input()
CS = Counter(S)
a = CS["a"]
b = CS["b"]
c = CS["c"]
a, b, c = sorted([a,b,c])
if a == 0 and b == 0:
    if c == 1:
        print("YES")
    else:
        print("NO")
elif a == 0:
    if c <= 1:
        print("YES")
    else:
        print("NO")
else:
    if c-a<=1:
        print("YES")
    else:
        print("NO")
