#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    T = input()
    if N == 1:
        if T == "0":
            print(10**10)
        elif T == "1":
            print(2*10**10)
        else:
            print(0)
        return
    if N == 2:
        if T == "11" or T == "10":
            print(10**10)
        elif T == "01":
            print(10**10-1)
        else:
            print(0)
        return
    NT = list(map(int, list(T)))
    NS = [1,1,0]*(10**5)
    check = False
    for p in range(3):
        cc = True
        for i,t in enumerate(NT):
            if t != NS[i+p]:
                cc = False
                break
        if cc:
            check = True
            break
    # print(p)
    if check:
        print(10**10-(p+N+2)//3+1)
    else:
        print(0)
            
        
if __name__ == '__main__':
    main()
