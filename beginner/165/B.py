#import sys
#input = sys.stdin.readline
def main():
    X = int( input())
    now = 100
    for i in range(100000):
        now = now*101//100
        if now >= X:
            print(i+1)
            return
if __name__ == '__main__':
    main()
