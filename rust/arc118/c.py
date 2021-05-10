#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    A = [6,10,15]
    T = set()
    for i in range(1,10**4+1):
        if i%6 == 0 or i%10 == 0 or i%15 == 0:
            T.add(i)
    T = list(T)
    T.sort()
    for t in T[4:N+1]:
        A.append(t)
    print(" ".join(map(str, A)))
if __name__ == '__main__':
    main()
