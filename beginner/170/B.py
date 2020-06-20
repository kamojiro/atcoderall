#import sys
#input = sys.stdin.readline
def main():
    X, Y = map( int, input().split())
    if Y < X*2:
        print("No")
        return
    if (Y-X*2)%2 == 0:
        if (Y-X*2)//2 <= X:
            print("Yes")
            return
    print("No")
        
    
if __name__ == '__main__':
    main()
