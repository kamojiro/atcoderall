#import sys
#input = sys.stdin.readline
def main():
    p, a = map(int,input().split())
    x = a
    while True:
        print(x)
        x *= a
        x %= p
        if x == 1:
            break
        
if __name__ == '__main__':
    main()
