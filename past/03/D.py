#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    S = [ input() for _ in range(5)]
    Nums = [".###..#..###.###.#.#.###.###.###.###.###.", 
    ".#.#.##....#...#.#.#.#...#.....#.#.#.#.#.",
    ".#.#..#..###.###.###.###.###...#.###.###.",
    ".#.#..#..#.....#...#...#.#.#...#.#.#...#.",
    ".###.###.###.###...#.###.###...#.###.###."]
    ANS = []
    for i in range(1,N+1):
        for j in range(10):
            check = True
            for k in range(5):
                # print(4*j+1,4*j+4, j , k,len(Nums[0]))
                # print(Nums[k][4*j+1:4*j+4])
                if S[k][4*i-3:4*i] == Nums[k][4*j+1:4*j+4]:
                    pass
                else:
                    check = False
            if check:
                ANS.append(j)
                break

    print("".join( map( str, ANS)))
    
if __name__ == '__main__':
    main()
