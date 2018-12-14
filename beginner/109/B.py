N = int(input())
W = input()
L = []
L.append(W)
last = W[-1]
ans = 'Yes'
for _ in range(N-1):
    w = input()
    if w in L:
        ans = 'No'
    if last == w[0]:
        last = w[-1]
        L.append(w)
    else:
        ans = 'No'
print(ans)
