import sys
input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    if sum(A)%(N*(N+1)//2) != 0:
        print("NO")
        return
    t = sum(A)//(N*(N+1)//2)
    d = [0]*N
    for i in range(N):
        d[i] = A[i] - A[i-1] - t
    for i in range(N):
        if d[i] > 0 or d[i]%N != 0:
            print("NO")
            return
    print("YES")
    
if __name__ == '__main__':
    main()
