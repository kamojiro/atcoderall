from collections import defaultdict
def collatz(a):
    if a % 2 == 0:
        return a//2
    return 3*a+1

s = int( input())
d = defaultdict( int)
d[s] = 1
for i in range(2, 1000000):
    s = collatz(s)
    if d[s] == 0:
        d[s] = 1
    else:
        ans = i
        break
print( ans)
