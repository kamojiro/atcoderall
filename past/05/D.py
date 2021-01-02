#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    S = [ input() for _ in range(N)]
    # lenS = [len(s) for s in S]
    # LS = [ s.lstrip("0") for _ in range(N)]
    # lenLS = [len(s) for s in S
    P = []
    for i, s in enumerate(S):
        p = len(s)
        ls = s.lstrip("0")
        P.append((len(ls), ls, -p,i))
    P.sort()
    ANS = [ S[p[3]] for p in P]
    print("\n".join(ANS))
        
if __name__ == '__main__':
    main()
