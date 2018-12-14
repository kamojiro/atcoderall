S = list(input())
t = input()
T = list(t)
NS = len(S)
NT = len(T)
j = -1
if NS < NT:
    pass
else:
    for i in range(NS - NT,-1,-1):
        j = i
        for k in range(NT):
            if S[i+k] == T[k] or S[i+k] == '?':
                pass
            else:
                j = -1
                break
        if j != -1:
            break
            
if j == -1:
    print('UNRESTORABLE')
else:
    k = 0
    ans = ''
    while k != NS:
        if k == j:
            ans += t
            k += NT
        else:
            if S[k] == '?':
                ans += 'a'
            else:
                ans += S[k]
            k += 1
    print(ans)
