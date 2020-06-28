#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    C = [0]*(10**5+1)
    ans = 0
    now = 0
    for i in range(N):
        a = A[i]
        C[a] += 1
        if C[a] >= 2:
            for j in range(now, N):
                C[A[j]] -= 1
                if a == A[j]:
                    now = j+1
                    break
        if ans < i-now+1:
            ans = i-now+1
    print(ans)
if __name__ == '__main__':
    main()
