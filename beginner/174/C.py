#import sys
#input = sys.stdin.readline
def main():
    K = int( input())
    now = 7
    now %= K
    for i in range(10**7):
        if now == 0:
            print(i+1)
            return
        now = (now*10+7)%K
    print("-1")
if __name__ == '__main__':
    main()
