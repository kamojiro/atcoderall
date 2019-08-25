# import sys
# input = sys.stdin.readline
Q = 10**9+7
def main():
    N = int( input())
    S = input()
    left = 0
    ans = 1
    # for i in range(N*2):
    #     s = S[i]
    for s in S:
        if s == "B":
            if left%2 == 0:
                left += 1
            else:
                ans *= left
                left -= 1
        else:
            if left%2 == 1:
                left += 1
            else:
                ans *= left
                left -= 1
        ans %= Q
    if left > 0 or ans == 0:
        print(0)
        return
    for i in range(1,N+1):
        ans *= i
        ans %= Q
    print(ans)
if __name__ == '__main__':
    main()
