N = int( input())
L = list( map( int, input().split()))
L.sort()
if sum(L[:-1]) > L[-1]:
    print("Yes")
else:
    print("No")
