#import sys
#input = sys.stdin.readline
def main():
    S = input()
    ans = ""
    if 0 <= ord(S[0])- ord("A") <= 25:
        ans = S[0]
    else:
        ans = chr( ord(S[0])- ord("a") + ord("A"))
    for s in S[1:]:
        if 0 <= ord(s)- ord("a") <= 25:
            ans += s
        else:
            ans += chr( ord(s)- ord("A") + ord("a"))
    print( ans)
if __name__ == '__main__':
    main()
