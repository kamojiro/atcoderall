#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    ans = sum(A)
    t = 0
    for a in A:
        if a > 0:
            t += 1
    if ans%t == 0:
        print(ans//t)
    else:
        print(ans//t+1)
if __name__ == '__main__':
    main()
