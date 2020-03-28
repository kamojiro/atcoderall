import sys
input = sys.stdin.readline
def main():
    N = int( input())
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map( lambda x: int(x)-1, input().split())
        E[a].append(b)
        E[b].append(a)
    
if __name__ == '__main__':
    main()
