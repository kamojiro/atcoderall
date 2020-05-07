#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    ANS = []
    now = 0
    for i in range(1,N+1):
        now += i
        ANS.append(i)
        if now == N:
            break
        if N < now:
            ANS.remove(now-N)
            break
    print("\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
