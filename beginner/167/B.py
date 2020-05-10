#import sys
#input = sys.stdin.readline
def main():
    A, B, C, K = map( int, input().split())
    if A >= K:
        print(K)
        return
    ans = A
    K -= A
    if B >= K:
        print(ans)
        return
    K -= B
    print(ans - K)
if __name__ == '__main__':
    main()








