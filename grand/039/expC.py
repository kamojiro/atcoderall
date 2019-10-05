#import sys
#input = sys.stdin.readline
Q = 998244353
def ope(x, N):
    if x%2 == 1:
        return x//2
    else:
        return x//2+pow(2, N-1)
def main():
    N = int( input())
    X = int( input())
    # V = [0]*(pow(2, N))
    # V[0] = 1
    # t = 0
    # while True:
    #     c = ope(t, N)
    #     if V[c] == 1:
    #         print(c)
    #         break
    #     print(c)
    #     V[t] = 1
    #     t = c
    for i in range(X+1):
        V = [0]*(pow(2,N)+1)
        now = i
        V[i] = 1
        cnt = 0
        while True:
#            print( bin(now)[2:], end=' ')
            neo = ope(now,N)
            cnt += 1
            if neo == i:
                print(i, cnt)
                break
            if V[neo] > 0:
                print(bin(neo)[2:], 'bad', cnt)
                break
            V[neo] = V[now]+1
            now = neo


if __name__ == '__main__':
    main()
