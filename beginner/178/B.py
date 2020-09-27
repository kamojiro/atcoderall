#import sys
#input = sys.stdin.readline
def main():
    a, b ,c, d = map( int, input().split())
    A = [a*c, a*d, b*c, b*d]
    if a < b:
        A.append((a+1)*c)
        A.append((b-1)*c)
        A.append((a+1)*d)
        A.append((b-1)*d)

    if c < d:
        A.append(a*(c+1))
        A.append(a*(d-1))
        A.append(b*(c+1))
        A.append(b*(d-1))

    if a < b and c < d:
        A.append((a+1)*(c+1))
        A.append((a+1)*(d-1))
        A.append((b-1)*(c+1))
        A.append((b-1)*(d-1))

    print(max(A))
        
            


if __name__ == '__main__':
    main()
