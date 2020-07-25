#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    ans = 1000
    stock = 0
    stock_price = 1000
    for i in range(N-1):
        a = A[i]
        # print(i, stock_price,a)
        if stock > 0 and stock_price <= a:
            ans += stock*a
            stock = 0
        # print("ans", ans)
        if A[i+1] < a:
            pass
        else:
            stock += ans//a
            ans -= ans//a*a
            stock_price = a
        print(ans, stock)
    if stock_price < A[N-1]:
        ans += stock*A[N-1]
    else:
        ans += stock*stock_price
    print(ans)
            
        
if __name__ == '__main__':
    main()
