#import sys
#input = sys.stdin.readline
def main():
    X = list( map( int, input().split()))
    for i in range(5):
        if X[i] == 0:
            print(i+1)
            return
if __name__ == '__main__':
    main()
