#import sys
#input = sys.stdin.readline
def main():
    N, M, K = map( int, input().split())
    A = list( map( int, input().split()))
    B = list( map( int, input().split()))
    indb = M-1
    now = sum(B)
    count = M
    while now > K:
        now -= B[indb]
        count -= 1
        indb -= 1

    ans = count
    for a in A:
        # print(ans, now)
        now += a
        count += 1
        while now > K and indb >= 0:
            now -= B[indb]
            count -= 1
            indb -= 1
        if now <= K:
            if ans < count:
                ans = count
    print(ans)
if __name__ == '__main__':
    main()
