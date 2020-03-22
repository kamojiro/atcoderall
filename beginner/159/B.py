#import sys
#input = sys.stdin.readline
def main():
    S = input()
    N = len(S)
    V = S[:(N-1)//2]
    W = S[(N+1)//2:]
    ans = "Yes"
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            ans = "No"
    M = len(V)
    L = len(W)
    for i in range(M//2):
        if V[i] != V[M-1-i]:
            ans = "No"
    for i in range(L//2):
        if W[i] != W[L-1-i]:
            ans = "No"
    print(ans)
if __name__ == '__main__':
    main()
