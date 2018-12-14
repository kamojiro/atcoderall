N = int( input())
K = int( input())
X = int( input())
Y = int( input())
if N <= K:
    print(N*X)
else:
    print(X*K + Y*(N-K))
