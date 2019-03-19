n = int( input())
A = list( map( int, input().split()))
ans = 0
for a in A:
    if a%6 == 2:
        ans += 1
    elif a%6 == 1 or a%6 == 3:
        pass
    elif a%6 == 4:
        ans += 1
    elif a%6 == 5:
        ans += 2
    else:
        ans += 3
print(ans)
