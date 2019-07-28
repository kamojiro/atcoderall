#import sys
#input = sys.stdin.readline
def main():
    a, b = map( int, input().split())
    if a > b:
        a, b = b, a
    if (b-a)%2 == 1:
        print("IMPOSSIBLE")
    else:
        print(a + (b-a)//2)
if __name__ == '__main__':
    main()
