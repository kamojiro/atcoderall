N = list( map( int, list( input())))
check = 0
ans = 0
for n in range( len(N)):
    if check == 1:
        ans += 9
        continue
    if N[n] == 9:
        ans += 9
        continue
    if n == 0:
        ans += N[0]-1
        check = 1
        continue
    ans += 8
    check = 1
print( max(ans, sum(N)))
