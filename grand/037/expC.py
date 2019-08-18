#import sys
#input = sys.stdin.readline
import heapq
def main():
    N = int( input())
    A = list( map( int, input().split()))
    B = list( map( int, input().split()))
    C = [(-B[i],i) for i in range(N)]
    heapq.heapify(C)
    ans = 0
    check = 0
    while check < N:
        a,i = heapq.heappop(C)
        a *= -1

        if B[i] == A[i]:
            check += 1
            continue
        cnt = (B[i] - A[i])//(B[i-1] + B[(i+1)%N])
        if cnt == 0:
            print(-1)
            return
        ans += cnt        
        a -= (B[i-1] + B[(i+1)%N])*cnt
        B[i] = a
        if B[i] == A[i]:
            check += 1
        elif B[i] > A[i]:
            heapq.heappush(C, (-a, i))
        else:
            print(-1)
            return

    print(ans)
        
if __name__ == '__main__':
    main()
