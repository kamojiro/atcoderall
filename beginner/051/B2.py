#import sys
#input = sys.stdin.readline
def main():
    K, S = map(int,input().split())
    ans = 0
    for i in range(K+1):
        for j in range(K+1):
            if i+j <= S and S - (i+j) <= K:
                ans += 1
    print(ans)
if __name__ == '__main__':
    main()
