n = int( input())
A = list( map( int, input().split()))
ansp = 0
sums = A[0]
if sums == 0:
    ansp += 1
    sums += 1
for i in range(1,n-1):
    sums += A[i]
    if i%2 == 1:
        if sums < 0:
            pass
        else:
            ansp += abs(-1-sums)
            sums = -1
    else:
        if sums > 0:
            pass
        else:
            ansp += abs(1 - sums)
            sums = 1
if (n-1)%2 == 0:
    if A[n-1] > 0:
        sums += A[n-1]
        pass
    else:
        ansp += abs(1-A[n])
        sums += 1
else:
    if A[n-1] < 0:
        sums += A[n-1]
        pass
    else:
        ansp += abs(-1-A[n-1])
        sums -= 1
if sums == 0:
    ansp += 1

sums = A[0]
ansm = 0
if sums == 0:
    ansm += 1
    sums -= 1
for i in range(1,n-1):
    sums += A[i]
    if i%2 == 0:
        if sums < 0:
            pass
        else:
            ansm += abs(-1-sums)
            sums = -1
    else:
        if sums > 0:
            pass
        else:
            ansm += abs(1 - sums)
            sums = 1
if (n-1)%2 == 1:
    if A[n-1] > 0:
        sums += A[n-1]
        pass
    else:
        ansm += abs(1-A[n-1])
        sums += 1
else:
    if A[n-1] < 0:
        sums += A[n-1]
        pass
    else:
        ansm += abs(-1-A[n-1])
        sums -= 1
if sums == 0:
    ansm += 1
print( min(ansp, ansm))
