N = int( input())
H = list( map( int, input().split()))
h = H[0]
now = 0
for i in range(N):
    if h <= H[i]:
        now += 1
        h = H[i]
print(now)
