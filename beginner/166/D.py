#import sys
#input = sys.stdin.readline
def main():
    X = int( input())
    for i in range(-200, 201):
        for j in range(-200, 201):
            if i**5 - j**5 == X:
                print(i, j)
                return
if __name__ == '__main__':
    main()
