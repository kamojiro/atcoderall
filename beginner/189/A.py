#import sys
#input = sys.stdin.readline
def main():
    C = input()
    if C[0] == C[1] == C[2]:
        print("Won")
    else:
        print("Lost")
if __name__ == '__main__':
    main()
