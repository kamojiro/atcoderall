#import sys
#input = sys.stdin.readline
def main():
    A = list(map(int,list(input())))
    N = len(A)
    mod = [0]*3
    for a in A:
        mod[a%3] += 1
    p = sum(A)%3
    if p == 0:
        print(0)
        return
    if p == 1:
        if mod[1] >= 1 and N >= 2:
            print(1)
            return
        if mod[2] >= 2 and N >= 3:
            print(2)
            return
    if p == 2:
        if mod[2] >= 1 and N >= 2:
            print(1)
            return
        if mod[1] >= 2 and N >= 3:
            print(2)
            return
    print(-1)
            
if __name__ == '__main__':
    main()
