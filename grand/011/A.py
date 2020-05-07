import sys
input = sys.stdin.readline
def main():
    N, C, K = map( int, input().split())
    T = [ int( input()) for _ in range(N)]
    T.sort()
    deadline = -1
    ans = 0
    count = 0
    for t in T:
        if deadline < t or count >= C:
            ans += 1
            deadline = t+K
            count = 1
            continue
        count += 1

    print(ans)
if __name__ == '__main__':
    main()
