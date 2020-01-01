#import sys
#input = sys.stdin.readline
def main():
    x = int(input())
    if x <= 59:
        print("Bad")
    elif x <= 89:
        print("Good")
    elif x <= 99:
        print("Great")
    else:
        print("Perfect")
if __name__ == '__main__':
    main()
