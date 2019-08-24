#import sys
#input = sys.stdin.readline
def main():
    L, A, B, M = map( int, input().split())
    s = A
    ans = 0
    p = 0
    for i in range(L):
        ans = (ans*pow(10, len( str(s)), M) + s )%M
#        print(s, end = " ")
        if len( str(s)) < len( str(s+B)):
#            print("d", len( str(s)), i-p+1, end = " ")
            p = i+1
#        print(ans)
        s += B
    print(ans)
if __name__ == '__main__':
    main()
