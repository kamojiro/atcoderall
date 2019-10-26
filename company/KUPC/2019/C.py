#import sys
#input = sys.stdin.readline
def main():
    M, K = map( int, input().split())
    ans = 0
    if M == 1:
        print(1)
        return
    for i in range(50):
        if M == pow(K+1, i):
            ans = i+1
            break
        if M < pow(K+1, i):
            ans = i
            break
    print(ans)
if __name__ == '__main__':
    main()
