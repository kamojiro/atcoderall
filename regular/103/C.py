from collections import Counter
n = int( input())
V = list( map( int, input().split()))
oddV = [ V[2*i+1] for i in range(n//2)]
evenV = [ V[2*i] for i in range(n//2)]
CoddV = Counter(oddV).most_common()
CevenV = Counter(evenV).most_common()
p, q = CoddV[0]
a, b = CevenV[0]
if p != a:
    ans = n-b-q
elif n == 2:
    ans = 1
else:
    if q == n//2 and b == n//2:
        ans = n//2
    elif q == n//2:
        ans = n//2 - CevenV[1][1]
    elif b == n//2:
        ans = n//2 - CoddV[1][1]
    else:
        r, s = CoddV[1]
        c, d = CevenV[1]
        if q + d >= s + b:
            ans = n-q-d
        else:
            ans = n-s-b
print(ans)
