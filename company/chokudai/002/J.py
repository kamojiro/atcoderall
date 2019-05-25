def factors(N): #約数を全て求める。ただし、順不同
    from collections import deque
    ret = deque()
    middle = int( N**(1/2))
    for i in range(1, middle):
        if N%i == 0:
            ret.append(i)
            ret.append(N//i)
            
    if N%middle == 0:
        ret.append(middle)
        if middle != N//middle:
            ret.append(N//middle)
    return ret

N = int( input())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = map( int, input().split())
G = list( factors(A[0]))
H = list( factors(B[0]))
G.sort( reverse = True)
H.sort( reverse = True)
gans = 1
hans = 1
for g in G:
    check = 1
    for i in range(N):
        if A[i]%g != 0 and B[i]%g != 0:
            check = 0
            break
    if check == 1:
        gans = g
        break
for h in H:
    check = 1
    for i in range(N):
        if A[i]%h != 0 and B[i]%h != 0:
            check = 0
            break
    if check == 1:
        hans = h
        break
print( max(hans, gans))
