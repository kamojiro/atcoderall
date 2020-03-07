#import sys
#input = sys.stdin.readline
def main():
    A, B = map( int, input().split())
    ans = -1
    for i in range(100000):
        if i*8//100 == A and i*10//100 == B:
            ans = i
            break
    print(ans)
if __name__ == '__main__':
    main()
