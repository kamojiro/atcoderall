def shiriai_right(X,Y,x):
    Z = []
    index_X = [i for i, a in enumerate(X) if a == x]
    for i in index_X:
        X.remove(i)
        Z.append(Y[i])
    return Z

def shiriai_left(Y,X,y):
    Z = []
    
    return Z
N, M = map( int, input().split())
X = []
Y = []
for i in range(M):
    S = list(input())
    X.appned(S[0])
    Y.append(S[1])
ans = 0

for x in X:
    Z = []
    
    
    
