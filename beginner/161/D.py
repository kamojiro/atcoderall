#import sys
#input = sys.stdin.readline
from copy import deepcopy
def main():
    K = int( input())
    T = [[1,2,3,4,5,6,7,8,9]]
    for i in range(10):
        S = T[i]
        R = []
        for s in S:
            t = s%10
            if t == 0:
                R.append(s*10)
                R.append(s*10+1)
            elif t%10 == 9:
                R.append(s*10+9)
                R.append(s*10+8)
            else:
                R.append(s*10+t)
                R.append(s*10+t+1)
                R.append(s*10+t-1)
        T.append(R)
    ANS = []
    for t in T:
        ANS.extend(t)
    ANS.sort()
    print(ANS[K-1])
if __name__ == '__main__':
    main()
