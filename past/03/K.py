#import sys
#input = sys.stdin.readline
def main():
    N, Q = map( int, input().split())
    FTX = [ tuple( map( int, input().split())) for _ in range(Q)]
    Above = [i for i in range(N+1)]
    Succ = [[-1,-1] for _ in range(N+1)]
    F = [i for i in range(N+1)]
    for f, t, x in FTX:
        if Above[t] == -1:
            F[t] = x
        else:
            Succ[Above[t]][1] = x
        xb = Succ[x][0]
        Succ[x][0] = Above[t]
        Above[t] = Above[f]
        if xb == -1:
            Above[f] = -1
            F[f] = -1
        else:
            Succ[xb][1] = -1
            Above[f] = xb
        # print("Succ",Succ)
        # print("Above",Above)
        # print("F",F)
    ANS = [0]*(N+1)
    FF = [0]*(N+1)
    for i in range(1,N+1):
        if F[i] > 0:
            FF[F[i]] = i
    # print("FF", FF)
    for i in range(1,N+1):
        if Succ[i][0] > 0:
            continue
        now = i
        f = FF[i]
        while now != -1:
            ANS[now] = f
            # if Succ[now][1] == -1:
            #     break
            now = Succ[now][1]
            # print(now, i)
    print( "\n".join( map( str, ANS[1:])))
    
if __name__ == '__main__':
    main()
