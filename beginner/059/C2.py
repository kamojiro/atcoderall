N = int( input())
A = list( map( int, input().split()))
ans = 10**15
for i in [1, -1]:
    ansi, sums = 0, 0
    for a in A:
        sums += a
        if sums*i <= 0:
            ansi += abs(sums-i)
            sums = i
        i *= -1
    ans = min( ans, ansi)
print(ans)
