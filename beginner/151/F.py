#import sys
#input = sys.stdin.readline
# https://tjkendev.github.io/procon-library/python/geometry/line_cross_point.html
# https://drken1215.hatenablog.com/entry/2020/01/12/224200

def is_on_same_line(a,b,c):
    # a,b,c:(int,int)
    return (b[1]-a[1])*(c[0]-a[0]) == (c[1]-a[1])*(b[0]-a[0])

def vertical_bisector(a,b):
    # a,b:(int,int)
    vertical_vector = (a[1]-b[1], b[0]-a[0])
    # vector equation
    return (((a[0]+b[0])/2, (a[1]+b[1])/2),(a[1]-b[1], b[0]-a[0]))

def intersection_with_two_lines(l, m):
    # assume not l // m
    lp, lv = l
    mp, mv = m
    

def main():
    N = int( input())
    Z = [ tuple( map( int, input().split())) for i in range(N)]
    



if __name__ == '__main__':
    main()
