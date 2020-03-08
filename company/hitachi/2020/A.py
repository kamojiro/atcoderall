#import sys
#input = sys.stdin.readline
def main():
    S = input()
    hi = 'hi'
    for i in range(1,6):
        if S == hi*i:
            print('Yes')
            return
    print('No')
if __name__ == '__main__':
    main()
