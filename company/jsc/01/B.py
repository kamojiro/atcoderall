import sys
input = sys.stdin.readline
Q = 10**9 + 7

def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    ans = 0

    for i in range(N):
        a = A[i]
        al = 0
        after = 0
        for i in range(i):
            if A[i] < a:
                al += 1
        for i in range(i+1, N):
            if A[i] < a:
                al += 1
                after += 1
        ans += K*(K-1)//2*al%Q + after*K%Q
        ans %= Q
    print(ans)
    
if __name__ == '__main__':
    main()
