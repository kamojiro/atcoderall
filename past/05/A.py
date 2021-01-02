#import sys
#input = sys.stdin.readline
def main():
    S = input()
    o = "o"
    x = "x"
    for i in range(3):
        if S[i:i+3] == o*3:
            print("o")
            return
        elif S[i:i+3] == x*3:
            print("x")
            return
    print("draw")
            
if __name__ == '__main__':
    main()
