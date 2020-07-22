import sys
input = sys.stdin.readline
def main():
    N = int( input())
    S = [ int( input()) for _ in range(N)]
    Q = int( input())
    K = [ int( input()) for _ in range(Q)]
    S.sort(reverse=True)
    S.append(0)
    ANS = []
    # print(S)
    # print(K)
    if S[0] == 0:
        print("\n".join(["0"]*Q))
        return

    for k in K:
        if k == 0:
            ANS.append(S[0]+1)
            continue
        if S[k] == 0:
            ANS.append(0)
            continue
        ANS.append(S[k]+1)
    # accS = [0]*(10**6+10)
    # # t = 10**6
    # for s in S:
    #     accS[s] += 1
    #     # if s != 0:
    #     #     if s < t:
    #     #         t = s
    # zero = accS[0]
    # accS[0] = 0
    # m = max(S)
    
    # for i in range(10**6+5,0,-1):
    #     accS[i-1] += accS[i]
    # ANS = []
    # if m == 0:
    #     print("\n".join(["0"]*Q))
    #     return
    # for k in K:
    #     if k == 0:
    #         ANS.append(m+1)
    #         continue
    #     if k >= N - zero:
    #         ANS.append(0)
    #         continue
    #     # print("nibu")
    #     l = 0
    #     r = m+2
    #     while r-l > 1:
    #         # print(l, r)
    #         m = (l+r)//2
    #         if accS[m] <= k:
    #             r = m
    #         else:
    #             l = m
    #     ANS.append(r)
    print("\n".join( map( str, ANS)))
        
if __name__ == '__main__':
    main()
