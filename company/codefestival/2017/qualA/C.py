from collections import Counter
H, W = map( int, input().split())
S = ''
for _ in range(H):
    S += input()
CS = Counter(S)
ans = 'Yes'
two = 0
one = 1
if H%2 == 1:
    two += W//2
if W%2 == 1:
    two += H//2
if H%2 == 1 and W%2 == 1:
    one = 1

nowtwo = 0
nowone = 0
for x in CS:
    if CS[x]%4 == 0:
        continue
    else:
        if CS[x]%2 == 0:
            nowtwo += 1
            if nowtwo > two:
                ans = 'No'
                break
        else:
            nowone += 1
            if nowone > one:
                ans = 'No'
                break
print(ans)
