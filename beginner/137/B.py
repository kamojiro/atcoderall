#import sys
#input = sys.stdin.readline
def main():
    k, x = map( int, input().split())
    ANS = []
    for i in range(1,k):
        ANS.append(x-k+i)
    ANS.append(x)
    for i in range(1,k):
        ANS.append(x+i)
    print(" ".join( map( str, ANS)))
if __name__ == '__main__':
    main()
