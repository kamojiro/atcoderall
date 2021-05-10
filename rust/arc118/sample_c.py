#import sys
#input = sys.stdin.readline
def main():
    A = set()
    for i in range(1,10**4+1):

        if i%6 == 0 or i%10 == 0 or i%15 == 0:
            A.add(i)
    print(len(A))
if __name__ == '__main__':
    main()
