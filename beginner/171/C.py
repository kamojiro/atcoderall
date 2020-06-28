#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    t = 26
    ANS = []
    a = ord("a")
    # if N == 1:
    #     print("a")
    #     return
    # N -= 1
    while True:
        # if N%t == 0:
        #     ANS.append("z")
        # else:
        ANS.append( chr((N-1)%t+a))
        N = (N-1)//t
        if N == 0:
            break
    print("".join( ANS[::-1]))
if __name__ == '__main__':
    main()
