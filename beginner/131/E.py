#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    t = (N-2)*(N-1)//2
    if K > t:
        print(-1)
        return
    print(N-1+t-K)
    for i in range(1,N):
        print(i, N)
    s = t - K
    cnt = 0
    for i in range(1,N):
        if cnt == s:
            break
        for j in range(i+1, N):
            if cnt == s:
                break
            print(i,j)
            cnt += 1
    return
if __name__ == '__main__':
    main()
