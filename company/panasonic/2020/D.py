#import sys
#input = sys.stdin.readline
from copy import deepcopy
def main():
    N = int( input())
    if N == 1:
        print('a')
        return
    ANS = [(1, 'a')]
    a = ord('a')
    for i in range(N-1):
        G = deepcopy(ANS)
        ANS = []
        for c, t in G:
            for j in range(c):
                ANS.append((c,t+chr(a+j)))
            ANS.append((c+1, t+chr(a+c)))
    ANS = [ t[1] for t in ANS]
    print('\n'.join(ANS))
if __name__ == '__main__':
    main()
