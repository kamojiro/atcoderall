#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    for i in range(N+1):
        print(i, i - (max(0, i**2-N))**(1/2))
if __name__ == '__main__':
    main()
