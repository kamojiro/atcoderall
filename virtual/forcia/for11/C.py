import sys
input = sys.stdin.readline
def main():
    N = int( input())
    A = [ int( input()) for _ in range(N)]
    if A[0] > 0:
        print(-1)
        return
    ans = 0
    for i in range(1,N):
        # print(i, A[i])
        if A[i] == 0:
            continue
        if A[i] == 1:
            ans += 1
            continue
        if A[i] == A[i-1]+1:
            ans += 1
            continue
        if A[i] <= A[i-1]:
            ans += A[i]
            continue
        print(-1)
        return
    print(ans)
if __name__ == '__main__':
    main()
