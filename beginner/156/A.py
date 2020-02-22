#import sys
#input = sys.stdin.readline
def main():
    N, R = map( int, input().split())
    if N >= 10:
        print(R)
        return
    print(R+100*(10-N))
if __name__ == '__main__':
    main()








