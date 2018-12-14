def prime(K):
    for i in range(2,K):
        if K%i == 0:
            return 0
    return 1
N = int( input())
ANS = []
K = 0
for i in range(11, 55555):
    if i%5 == 1:
        if prime(i) == 1:
            ANS.append(i)
            K += 1
    if K == N:
        break
for i in range(N-1):
    print(ANS[i], end = ' ')
print(ANS[N-1])
    
