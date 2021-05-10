#import sys
#input = sys.stdin.readline
def main():
    t, N = map(int, input().split())
    print(((100+t)*N-1)//t)
if __name__ == '__main__':
    main()
