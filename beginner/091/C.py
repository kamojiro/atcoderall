N = int(input())
R = [list(map(int,input().split())) for i in range(N)]
B = [list(map(int,input().split())) for i in range(N)]
R.sort(key = lambda x:x[1], reverse=True)
B.sort(key = lambda x:x[0], reverse=False)
ans = 0
for b in B:
    for r in R:
        if r[0] < b[0] and r[1] < b[1]:
            ans += 1
            R.remove(r)
            break
print(ans)
    
