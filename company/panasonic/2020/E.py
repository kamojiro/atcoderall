#import sys
#input = sys.stdin.readline
from itertools import permutations
def main():
    C = [ input() for _ in range(3)]
    LC = [ len(c) for c in C]
    ans = sum(LC)
    for P in permutations( range(3)):
        now = sum(LC)
        a, b, c = P[0], P[1], P[2]
        X, Y, Z = C[a], C[b], C[c]
        x, y, z = LC[a], LC[b], LC[c]
        for i in range(x):
            # if x - i > y:
            #     continue
            check = True
            for j in range(i, min(x,i+y)):
                if X[j] == '?' or Y[j-i] == '?' or X[j] == Y[j-i]:
                    continue
                check = False
                break
            if check:
                if i+y <= x:
                    W = X[:i]
                    for j in range(i,i+y):
                        if X[j] == '?' or Y[j-i] == '?':
                            W += '?'
                        else:
                            W += X[j]
                    W += X[i+y:]
                    now -= y
                    y = x
                else:
                    W = X[:i]
                    for j in range(i,x):
                        if X[j] == '?' or Y[j-i] == '?':
                            W += '?'
                        else:
                            W += X[j]
                    W += Y[x-i:]
                    now -= x-i
                    y = now-z
                break
        else:
            W = X+Y
            y += x
        second = now
        for i in range(y):
            check = True
            for j in range(i, min(y,i+z)):
                if W[j] == '?' or Z[j-i] == '?' or W[j] == Z[j-i]:
                    continue
                check = False
                break
            if check:
#                print(i)
                if i+z <= y:
                    now -= z
                else:
                    now -= y-i
                break
        if y < z:
            y, z = z, y
            W, Z = Z, W
        for i in range(1,z):
            check = True
            for j in range(i):

                if W[j] == '?' or Z[z-j-1] == '?' or W[j] == Z[z-j-1]:
                    continue
                check = False
                break
            if check:
                second -= i
                break
#        print(X, Y, W, Z, y, now)
        if now < ans:
            ans = now
        if second < ans:
            ans = second
    print(ans)
        
if __name__ == '__main__':
    main()
