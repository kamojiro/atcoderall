#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    now = 1
    for i in range(40):
        now *= 3
        x = N-now
        j = 0
        if x == 0:
            continue
        while x%5 == 0:
            x //= 5
            j += 1
        if j > 0 and x == 1:
            print(i+1, j)
            return
    print(-1)
if __name__ == '__main__':
    main()
