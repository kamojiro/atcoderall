#import sys
#input = sys.stdin.readline
from copy import deepcopy
def main():
    X = list( map( int, input().split()))
    Y = []
    N = len(X)
    for i in range(N-1):
        Y.append( abs(X[i]-X[i+1]))
    #print(Y)
    for i in range(N-2):
        X = deepcopy(Y)
        Y = []
        print(X)
        #print(X,Y,i, N-2-i)
        for j in range(N-2-i):
            Y.append( abs(X[j] - X[j+1]))

    print(Y[0])
if __name__ == '__main__':
    main()
