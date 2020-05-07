#import sys
#input = sys.stdin.readline
def main():
    x, y = map( int, input().split())
    if x == 0:
        if y > 0:
            print(y-x)
        else:
            print(x-y+1)
    elif x > 0:
        if y > x:
            print(y-x)
        elif y > 0:
            print(x-y+2)
        else:
            print(abs(x+y)+1)
    else:
        if y == 0:
            print(-x)
        elif y > 0:
            print( abs(x+y)+1)
        elif x < y:
            print(y-x)
        else:
            print(x-y+2)
            
if __name__ == '__main__':
    main()
