#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    S = list( input())
    for i in range(len(S)):
        S[i] = chr( (ord(S[i]) - ord('A') + N)%26 + ord('A'))
    print("".join(S))
if __name__ == '__main__':
    main()
