#import sys
#input = sys.stdin.readline
def main():
    ANS = []
    for p in range(10):
        a = [10001,0,10002]
        ANS.append("< "+ " ".join( map( str, a)))
        g = [10001,10002,10001]
        ANS.append("+ "+ " ".join( map( str, g)))
        for _ in range(10):
            b = [10003+10*p,1,10004]
            ANS.append("< "+ " ".join( map( str, b)))
            h = [10003+10*p,10004,10003+10*p]
            ANS.append("+ "+ " ".join( map( str, h)))
            i = [10002,10004,10005]
            ANS.append("< "+ " ".join( map( str, i)))
            j = [10005,10004,10004]
            ANS.append("< "+ " ".join( map( str, j)))
            k = [2,10004,2]
            ANS.append("+ "+ " ".join( map( str, k)))
    print(len(ANS))
    print("\n".join(ANS))

if __name__ == '__main__':
    main()
