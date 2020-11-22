#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    S = list(input())
    ANS = []
    t = 0
    for s in S:
        # print(t, ANS)
        if t <= 1:
            ANS.append(s)
            t += 1
            continue
        if s != "x":
            ANS.append(s)
            t += 1
            continue
        if ANS[-1] == "o" and ANS[-2] == "f":
            t -= 2
            ANS.pop()
            ANS.pop()
        else:
            ANS.append(s)
            t += 1
    print(len(ANS))
            
    
if __name__ == '__main__':
    main()
