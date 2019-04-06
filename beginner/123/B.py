from itertools import permutations
A = [ int( input()) for _ in range(5)]
ans = 1000
for p in permutations( range(5)):
    now = A[p[0]]
    for i in range(4):
        if now%10 == 0:
            now += A[p[i+1]]
        else:
            now = (now//10+1)*10
            now += A[p[i+1]]
    ans = min( ans, now)
print( ans)
