A = int(input())
S = list(input())
L = len(S)
ans = True
if A == 0:
    ans = False
else:
    for i in range(L):
        if S[i] == '+':
            A += 1
        else:
            A -= 1
            if A == 0:
                ans = False
if ans == False:
    print('Yes')
else:
    print('No')
