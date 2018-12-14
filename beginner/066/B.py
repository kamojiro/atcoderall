S = input()
L = len(S)
if L%2 == 0:
    for i in range(L-2,0,-2):
        if S[:i//2] == S[i//2:i]:
            ans = i
            break
else:
    for i in range(L-1,0,-2):
        if S[:i//2] == S[i//2:i]:
            ans = i
            break
print(i)
