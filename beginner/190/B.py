#import sys
#input = sys.stdin.readline
def main():
    N, S, D = map(int,input().split())
    XY = [tuple(map(int,input().split())) for _ in range(N)]
    for x, y in XY:
        if x < S and D < y:
            print("Yes")
            return
    print("No")
    
if __name__ == '__main__':
    main()
