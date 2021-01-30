#import sys
#input = sys.stdin.readline
def main():
    A, B, C = map(int, input().split())
    takahashi = "Takahashi"
    aoki = "Aoki"
    if C == 1:
        A, B = B, A
        takahashi, aoki = aoki, takahashi
    if A <= B:
        print(aoki)
    else:
        print(takahashi)
if __name__ == '__main__':
    main()
