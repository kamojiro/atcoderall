#import sys
#input = sys.stdin.readline
def main():
    S = input()
    T = input()
    if S == T[:len(S)] and len(S) + 1 == len(T):
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
