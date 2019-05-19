N, K = map( int, input().split())
ANS = [0]*(N+1)
for i in range(1,N+1):
    if i >= K:
        ANS[i] = 1
    a = i
    t = 0
    while a < K:
        a *= 2
        t += 1
    ANS[i] = 2**(-t)
print(sum(ANS)/N)
