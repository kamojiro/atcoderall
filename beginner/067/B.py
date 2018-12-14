N, K = map( int, input().split())
L = list( map( int, input().split()))
L.sort(key = None, reverse = True)
LL = L[0:K]
print(sum(LL))










