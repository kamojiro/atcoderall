import sys
input = sys.stdin.readline
def main():
    N = int( input())
    A = [ int( input()) for _ in range(N)]
    C = [0]*(10**5+1)
    ans = 0
    for a in A:
        if C[a] > 0:
            ans += 1
        C[a] = 1
    print(ans)
if __name__ == '__main__':
    main()
