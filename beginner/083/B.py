N, A, B = map( int, input().split())
ans = 0
for i in range(1,N+1):
    X = sum(list( map(int, list(str(i)))))
    if A <= X and X <= B:
        ans += i
print(ans)
    
