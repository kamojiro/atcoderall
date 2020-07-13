#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    H = [ int( input()) for _ in range(N)]
    L = [0]*N
    stack = []
    for i in range(N):
        h = H[i]
        if not stack:
            stack.append((h,i))
            continue
        while stack:
            if h >= stack[-1][0]:
                stack.pop()
            else:
                break
        if not stack:
            stack.append((h,i))
            continue
        L[i] = stack[-1][1]+1
        stack.append((h,i))
    R = [N-1]*N
    stack = []
    for i in range(N-1,-1,-1):
        h = H[i]
        if not stack:
            stack.append((h,i))
            continue
        while stack:
            if h >= stack[-1][0]:
                stack.pop()
            else:
                break
        if not stack:
            stack.append((h,i))
            continue
        R[i] = stack[-1][1]-1
        stack.append((h,i))
    # print(L)
    # print(R)
    print("\n".join( map( str, [R[i]-L[i] for i in range(N)])))
        
if __name__ == '__main__':
    main()
