N, L = map( int, input().split())
A = list( map( int, input().split()))
ans = "Impossible"
for i in range(N-1):
    if A[i] + A[i+1] >= L:
        ans = "Possible"
        t = i
        break
if ans == "Impossible":
    print(ans)
else:
    print(ans)
    for i in range(t):
        print(i+1)
    for i in range(N-2,t,-1):
        print(i+1)
    print(t+1)








