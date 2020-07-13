#import sys
#input = sys.stdin.readline
from collections import Counter
def func(x):
    cnt = 0
    y = x
    while x > 0:
        if x%2 == 1:
            cnt += 1
        x //= 2
    return y%cnt
        
def main():
    N = int( input())
    X = list( map( int, list( input())))
    base_plus = 0
    base_minus = 0
    r = 1
    one = Counter(X)[1]
    for x in X[::-1]:
        base_plus += r*x
        base_plus %= one+1
        r *= 2
        r %= one+1
    r = 1
    if one > 1:
        for x in X[::-1]:
            base_minus += r*x
            base_minus %= one-1
            r *= 2
            r %= one-1

    ANS = [0]*N
    # print(base)
    # print(bin(base))
    for i in range(N):
        if one == 1:
            if X[i] == 1:
                ANS[i] = 0
                continue
        if X[i] == 1:
            xi = (base_minus -  pow(2,N-1-i,one-1))%(one-1)
            # print(i, bin(base -  pow(2,N-1-i)), one-1)
        else:
            xi = (base_plus +  pow(2,N-1-i,one+1))%(one+1)
            # print(i, bin(base +  pow(2,N-1-i)), one+1)
        # print(i,xi)
        if xi == 0:
            ANS[i] = 1
            continue
        ans = 1
        while xi > 0:
            ans += 1
            xi = func(xi)
        ANS[i] = ans
    print("\n".join( map( str, ANS)))
    
    
if __name__ == '__main__':
    main()
