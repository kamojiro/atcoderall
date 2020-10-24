import sys
input = sys.stdin.readline

def solveD(N):
    ANS = []
    for i in range(1,N+1):
        ANS.append((i,i+N*1))
    return ANS

def solveT(N,M):
    ANS = []
    for  i in range(N):
        if i == 0:
            ANS.append((1,N*4+1))
            continue
        if i <= M:
            ANS.append((i*2,i*2+1))
            continue
        ANS.append((i*2,i*2+N*2))
    return ANS

# def solveA(N,M):
#     ANS = []
#     while True:
#         continue
#     return ANS   

def main():
    N, M = map(int,input().split())
    if N == 1:
        if M == 0:
            print("1 2")
        else:
            print(-1)
        return
    if N-1 <= abs(M):
        print(-1)
        return
    if M < 0:
        print(-1)
        return
    if M == 0:
        ANS = solveD(N)
    else:
        ANS = solveT(N,M)

    print("\n".join([ " ".join(map(str,ans)) for ans in ANS]))
        
if __name__ == '__main__':
    main()
