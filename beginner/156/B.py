#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    for i in range(1,100):
        if N//pow(K,i) == 0:
            print(i)
            break
if __name__ == '__main__':
    main()
