#import sys
#input = sys.stdin.readline
def main():
    S = list( map( int, list( input())))
    N =len(S)
    A = [0]*2019
    P = 2019
    num = [0] * P
    num[0] = 1
    now, ans = 0, 0
    _10 = 1
    for i in range(N-1, -1, -1):
        now = (now + int(S[i]) * _10) % P
        _10 *= 10
        _10 %= P
        ans += num[now]
        num[now] += 1
    print(ans)
if __name__ == '__main__':
    main()
