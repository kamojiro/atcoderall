#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    root = 1
    if A[0] == 1:
        if N == 0:
            print(1)
        else:
            print(-1)
        return
    B = A[::-1]
    low = high = B[0]
    # Low = []
    Hight = [high]
    Low = [low]
    for b in B[1:]:
        low = max(1, (low+1)//2) + b
        high = high + b
        Hight.append(high)
        Low.append(low)
    if low > 1:
        print(-1)
        return
    ans = 1
    now = 1
    BHight = Hight[::-1]
    BLow = Low[::-1]
    for i in range(1,N+1):
        high = BHight[i]
        low = BLow[i]
        if high < now or now*2 < low:
            print(-1)
            return
        leaf = A[i]
        now = min(high, now*2)
        ans += now
        now -= leaf
    print(ans)
if __name__ == '__main__':
    main()
