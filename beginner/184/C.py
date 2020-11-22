#import sys
#input = sys.stdin.readline

def one_move(a,b,c,d):
    if a+b == c+d:
        return True
    if a-b == c-d:
        return True
    if abs(a-c) + abs(b-d) <= 3:
        return True
    return False

def main():
    r1, c1 = map( int, input().split())
    r2, c2 = map( int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if one_move(r1,c1,r2,c2):
        print(1)
        return
    if (r1+c1)%2==(r2+c2)%2:
        print(2)
        return
    for x in range(r1-4,r1+5):
        for y in range(c1-4,c1+5):
            if one_move(r1,c1,x,y):
                if one_move(x,y,r2,c2):
                    print(2)
                    return
    for x in range(r2-4,r2+5):
        for y in range(c2-4,c2+5):
            if one_move(x,y,r2,c2):
                if one_move(r1,c1,x,y):
                    print(2)
                    return
    print(3)
    
if __name__ == '__main__':
    main()
