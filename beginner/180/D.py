#import sys
#input = sys.stdin.readline
def main():
    X, Y, A, B = map(int,input().split())
    experience = 0
    while X < Y:
        if X*A >= Y and X+B >= Y:
            break
        if X*A >= Y:
            experience += max((Y-X-1)//B,0)
            break
        if X*A >= X+B:
            experience += max((Y-X-1)//B,0)
            break
        X *= A
        experience += 1
    print(experience)
        
if __name__ == '__main__':
    main()
