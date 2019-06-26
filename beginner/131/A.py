#import sys
#input = sys.stdin.readline
def main():
    S = input()
    ans= "Good"
    for i in range(3):
        if S[i] == S[i+1]:
            ans = "Bad"
    print(ans)

if __name__ == '__main__':
    main()
