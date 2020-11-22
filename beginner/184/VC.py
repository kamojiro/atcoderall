#import sys
#input = sys.stdin.readline
def main():
    r2, c2 = map( int,input().split())
    for x in range(r2-4,r2+5):
        for y in range(c2-4,c2+5):
            print(x,y)

if __name__ == '__main__':
    main()
