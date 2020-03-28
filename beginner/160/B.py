#import sys
#input = sys.stdin.readline
def main():
    X = int( input())
    print(X//500*1000 + X%500//5*5)
if __name__ == '__main__':
    main()
