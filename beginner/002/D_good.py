from itertools import combinations
N, M = map( int, input().split())
X = set([tuple(map(int, input().split())) for i in range(M)])
Flag = False
for k in range(N,0,-1):
    for people in combinations(range(1,N+1),k):
        if set(combinations(people,2)) <= X:
            print(k)
            Flag = True
            break
    if Flag:
        break

