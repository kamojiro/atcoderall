#import sys
#input = sys.stdin.readline
def main():
    S = input()
    ans = "Yes"
    T = [0]*30
    for s in S:
        T[ord(s)-ord("A")] += 1
    for i in range(30):
        if T[i] == 0 or T[i] == 2:
            pass
        else:
            ans = "No"
            break
    print(ans)
    
if __name__ == '__main__':
    main()
