#import sys
#input = sys.stdin.readline
def main():
    S = input()
    ANS = []
    now = S[0]
    cnt = 1
    for s in S[1:]:
        if now == s:
            cnt += 1
        else:
            ANS.append( now+str(cnt))
            now = s
            cnt = 1
    ANS.append( now+str(cnt))
    print( "".join(ANS))
    
if __name__ == '__main__':
    main()
