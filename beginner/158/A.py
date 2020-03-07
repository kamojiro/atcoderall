#import sys
#input = sys.stdin.readline
def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print('No')
        return
    print('Yes')
    
if __name__ == '__main__':
    main()
