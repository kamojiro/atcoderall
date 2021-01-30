def pp(x,n):
    if x < 0:
        return 10**19,10**19
    ret = 0
    p = 2**n
    y = x//p
    for _ in range(n):
        if x%2 == 1:
            ret += 1
        x //= 2
    return y, ret
        
def main():
    X, Y = map(int,input().split())
    if X >= Y:
        print(X-Y)
        return
    ans = 10**20
    ans = abs(X-Y)

    for i in range(80):
        p = pow(2,i)
        xp = X*p
        if abs(xp-Y)+i < ans:
            ans = abs(xp-Y)+i
        if Y == xp:
            if i < ans:
                ans = i
            continue
        if Y > xp:
            a = Y-xp
            y, r = pp(a,i)
            pans = i+r+y
            if pans < ans:
                ans = pans
            continue
        y, r = pp(xp-Y,i)
        pans = i+y+r
        if pans < ans:
            ans = pans
    print(ans)
            
        
    
if __name__ == '__main__':
    main()
