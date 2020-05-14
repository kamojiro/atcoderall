#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    AB = [ tuple( map( int, input().split())) for _ in range(M)]
    V = [0]*(N+1)
    for a, b in AB:
        V[a] += 1
        V[b] += 1
    for v in V:
        if v%2 == 1:
            print("NO")
            return
    print("YES")
        
if __name__ == '__main__':
    main()
