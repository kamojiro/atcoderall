#import sys
#input = sys.stdin.readline
def main():
    S = list( map( int, list( input())))
    N = len(S)
    A = [0]*2019
    Q = 2019
    now = 0
    A[0] = 1
    for i in range(N-1,-1,-1):
        now = (S[i]*pow(10,N-1-i,Q)+now)%Q
        A[now] += 1

    ans = 0
    for a in A:
        ans += a*(a-1)//2
    print(ans)
if __name__ == '__main__':
    main()
