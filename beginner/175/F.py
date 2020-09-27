#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N = int( input())
    Ss = []
    Cs = []
    for _ in range(N):
        s, c = input().split()
        Ss.append(s)
        Cs.append(int(c))
    RSs = [ s[::-1] for s in S]
    Head = defaultdict( lambda : [])
    Tail = defaultdict( lambda : [])
    for i in range(N):
        s = Ss[i]
        L = len(s)
        for j in range(1,L+1):
            Head[s[:j]].append((i, j))
        for j in range(L-1,-1,-1):
            Tail[s[j:]].append((i, j))
    
        
if __name__ == '__main__':
    main()
