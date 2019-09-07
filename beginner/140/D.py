#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    S = input()
    now = S[0]
    cnt = 0
    for s in S[1:]:
        if s == now:
            continue
        now = s
        cnt += 1
    if cnt%2 == 0:
        cnt //= 2
        if cnt <= K:
            print(N-1)
            return
        print(N-1-(cnt-K)*2)
    else:
        cnt //= 2
        if cnt + 1 <= K:
            print(N-1)
            return
        print(N-1-(cnt-K)*2-1)
if __name__ == '__main__':
    main()
