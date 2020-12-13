#import sys
#input = sys.stdin.readline
# from math import gcd
def main():
    N, M = map( int, input().split())
    if M == 0:
        print(1)
        return
    A = list( map( int, input().split()))
    if N == M:
        print(0)
        return
    A.sort()
    A.append(N+1)
    ans = 0
    now = 1
    for a in A:
        diff = a-now
        now = a+1
        if diff == 0:
            continue
        if ans == 0:
            ans = diff
        else:
            ans = min(ans, diff)
    # print(ans)
    now = 1
    aaa = 0
    for a in A:
        aaa += (a-now+ans-1)//ans
        now = a+1
    print(aaa)
            
    
    
if __name__ == '__main__':
    main()
