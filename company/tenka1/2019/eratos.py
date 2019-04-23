def eratosththenes(N):
    if N == 0:
        return [0]
    work = [True] * (N+1)
    work[0] = False
    work[1] = False
    for i in range(N+1):
        if work[i]:
            for j in range(2* i, N+1, i):
                work[j] = False
    return work

print( sum( eratosththenes(10000)))
