#import sys
#input = sys.stdin.readline
def main():
    N = list( map( int, list( input())))
    nine = sum(N)
    if nine%9 == 0:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
