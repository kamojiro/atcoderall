#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    if N == 2:
        print(A[0], A[1])
        return
    OddSum = [0]
    EvenSum = [0]
    for i in range(N):
        if i%2 == 0:
            OddSum.append(OddSum[-1] + A[i])
            EvenSum.append(EvenSum[-1])
        else:
            OddSum.append(OddSum[-1])
            EvenSum.append(EvenSum[-1] + A[i])
    if N%2 == 0:
        ans = max(OddSum[-1], EvenSum[-1])
        for i in range(1,N,2):
            t = EvenSum[-1] - EvenSum[i+1] + OddSum[i] - OddSum[0]
            if ans < t:
                ans = t
        print(ans)
        return

    ans = max( EvenSum[-1], OddSum[-1] - min(A[::2]))
    Head = [0]
    for i in range(1,N+1):
        if i%2 == 1:
            Head.append(Head[-1])
            continue
        if i == 2:
            Head.append(A[i-1])
            continue
        Head.append( max(Head[-1], OddSum[i-2]) + A[i-1])

    Back = [0]
    for i in range(N,0,-1):
        if i%2 == 1:
            Back.append(Back[-1])
            continue
        if i == N-1:
            Back.append(A[i-1])
            continue
        Back.append( max(Back[-1], OddSum[-1] - OddSum[i+2]) + A[i-1])

    # if ans < Head[-1]:
    #     ans = Head[-1]
    # if ans < Back[-1]:
    #     ans = Back[-1]
    for i in range(2,N+1,2):
        if ans < Head[i] + Back[N-1-i]:
            ans = Head[i] + Back[N-1-i]
        if ans < Head[i] + Back[N+1-i] - A[i-1]:
            ans = Head[i] + Back[N+1-i] - A[i-1]
    
    print(ans)
    
if __name__ == '__main__':
    main()
