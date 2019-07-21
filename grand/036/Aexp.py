#import sys
#input = sys.stdin.readline
def main():
    V = [0]*50
    for z in range(1, 8):
        for i in range(z+1):
            for j in range(z+1):
                print(i,j, z**2*2 - (z*i + z*j + (z-i)*(z-j)))
                V[ z**2*2 - (z*i + z*j + (z-i)*(z-j))] = 1
    print(V)
if __name__ == '__main__':
    main()
