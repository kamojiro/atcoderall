#import sys
#input = sys.stdin.readline
def main():
    N, X = map( int , input().split())
    S = list( input())
    for s in S:
        if s == "o":
            X += 1
            continue
        if X == 0:
            continue
        X -= 1
    print(X)
if __name__ == '__main__':
    main()
 
