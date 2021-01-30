#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.append(0)
    stack = []
    ans = 0
    for i, a in enumerate(A):
        if not stack:
            stack.append((a,i))
            continue
        if stack[-1][0] <= a:
            stack.append((a,i))
            continue
        now_i = i
        # print(stack)
        while stack[-1][0] > a:
            now_a, now_i = stack.pop()
            # print(now_a, now_i)
            # print((i-now_i)*now_a)
            if ans < (i-now_i)*now_a:
                ans = (i-now_i)*now_a
            if not stack:
                break
        stack.append((a,now_i))
        # print(ans)
        
    print(ans)
            
if __name__ == '__main__':
    main()
