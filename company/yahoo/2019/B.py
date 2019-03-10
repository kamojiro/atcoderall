A = [ list( map( int, input().split())) for _ in range(3)]
ans = "YES"
for t in range(1,5):
    for i in range(3):
        if A[i][1] == t or A[i][0] == t:
            pass
        else:
            break
    else:
        ans = "NO"
print(ans)
