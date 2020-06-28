#import sys
#input = sys.stdin.readline

def able_to_get(X,M,N,m):
    # if X[0]-1 > m:
    #     return False
    # now = max(m - (X[0]-1)+1,(m-X[0])//2 , X[0])+1
    # # 戻っていく
    # # 行って戻る
    # # yだけ進むなら、m = y*2+x
    # if now >= N:
    #     return True
    now = 1
    for x in X:
        # print(now)
        if x < now:
            now = x+m+1
            continue
        if x-now > m:
            return False
        now = max(m-(x-now)+now, (m-(x-now))//2+x ,x)+1
    # print(now)
    if now < N:
        return False
    else:
        return True

def main():
    N, M = map( int, input().split())
    X = [ int( input()) for _ in range(M)]
    if M == 1:
        print( min((X[0]-1)*2+(N-X[0]), (X[0]-1)+(N-X[0])*2))
        return
    l = -1
    r = N
    while r-l > 1:
        m = (l+r)//2
        # print("start", m)
        if able_to_get(X,M,N,m):
            r = m
            # print(True)
        else:
            l = m
    print(r)
if __name__ == '__main__':
    main()
