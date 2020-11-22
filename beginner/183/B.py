#import sys
#input = sys.stdin.readline
def main():
    sx,sy, gx, gy = map(int,input().split())
    if sx == gx:
        print(sx)
        return
    print((sx*gy+gx*sy)/(gy+sy))
if __name__ == '__main__':
    main()
