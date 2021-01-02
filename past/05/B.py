#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    S = list( input())
    a = ord("a")
    Alpha = [-1]*26
    C = [0]*26
    for i, s in enumerate(S):
        Alpha[ord(s)-a] = i
        # C[ord(s)-a] += 1
    P = []

    for i, t in enumerate(Alpha):
        if t > -1:
            P.append((t,i))
    P.sort()
    ANS = []
    for _, i in P:
        ANS.append(chr(i+a))
    print("".join(ANS))
        
if __name__ == '__main__':
    main()
    
