S = input()
T = input()
ans = "You can win"
A = "atcoder"
l = len(S)
for i in range(l):
    if S[i] == T[i]:
        pass
    elif S[i] == "@":
        if T[i] in A:
            pass
        elif T[i] == "@":
            pass
        else:
            ans = "You will lose"
    elif S[i] in A:
        if T[i] == "@":
            pass
        else:
            ans = "You will lose"
    else:
        ans = "You will lose"
print( ans)
