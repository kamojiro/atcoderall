#import sys
#input = sys.stdin.readline
def main():
    S = input()
    T = int(input())
    x = 0
    y = 0
    h = 0
    for s in S:
        if s == "L":
            x -= 1
        elif s == "R":
            x += 1
        elif s == "U":
            y += 1
        elif s == "D":
            y -= 1
        else:
            h += 1
    if T == 1:
        print( abs(x) + abs(y) +h)
    else:
        if abs(x) + abs(y) >= h:
            print(abs(x) + abs(y) - h)
        else:
            if ((abs(x)+abs(y)-h)%2 == 0):
                print(0)
            else:
                print(1)
if __name__ == '__main__':
    main()
