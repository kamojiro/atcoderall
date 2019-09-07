#import sys
#input = sys.stdin.readline
def main():
    A, B = map( int, input().split())
    ans = 0
    if B == 1:
        print(0)
        return
    for i in range(30):
        if A*i - (i-1) >= B:
            print(i)
            break
    
if __name__ == '__main__':
    main()
