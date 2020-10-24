#import sys
#input = sys.stdin.readline
def main():
    S = input()
    T = input()
    if S == "Y":
        if T == "a":
            print("A")
        elif T == "b":
            print("B")
        else:
            print("C")
    else:
        print(T)
            
if __name__ == '__main__':
    main()
