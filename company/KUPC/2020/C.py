#import sys
#input = sys.stdin.readline
def main():
    # N = 13
    # print(N)
    # a = ord("a")
    # ANS = []
    # for i in range(N-1):
    #     ans = ["a"]*(N-1)+[chr(a+i)]
    #     ANS.append(ans)
    # ANS.append([chr(a+i) for i in range(N-1,N+12)])
    # print("\n".join(["".join(ans) for ans in ANS]))
    # N = 5
    # print(N)
    # a = ord("a")
    # ANS = []
    # for i in range(N):
    #     ans = []
    #     for j in range(N):
    #         ans.append(chr(a+i*5+j))
    #     ANS.append(ans)
    # print("\n".join(["".join(ans) for ans in ANS]))
    N = 13
    print(N)
    a = ord("a")
    duplicate = set()
    ANS = []
    alph = 26
    first = [chr(a+i) for i in range(N)]
    for i in range(N-1):
        duplicate.add("".join(first[i:i+2]))
    ANS.append(first)
    alphabets = [[chr(a+i) for i in range(N)], [chr(a+i) for i in range(N,N*2)]]
    # print(duplicate)
    for i in range(1,N):
        alphs = alphabets[i%2]
        ans = []
        for j in range(N):
            if j == 0:
                for v in alphs:
                    if not (ANS[-1][j]+v) in duplicate:
                        duplicate.add(ANS[-1][j]+v)
                        ans.append(v)
                        break
            else:
                for v in alphs:
                    word0 = ANS[-1][j]+v
                    word1 = ans[-1]+v
                    if (not (word0 in duplicate)) and (not (word1 in duplicate)):
                        # if i == 1:
                        #     print("tate",ANS[-1][j]+v, (ANS[-1][j]+v) in duplicate)
                        #     print("yoko",ans[-1]+v,(ans[-1]+v) in duplicate)
                        #     print("no", "no" in duplicate)

                        # if i == 1:
                        #     print(ANS[-1][j]+v)
                        duplicate.add(ANS[-1][j]+v)
                        # if i == 1:
                        #     print("add", ans[-1]+v)
                        duplicate.add(ans[-1]+v)
                        ans.append(v)
                        # if i == 1:
                        #     print(ANS[-1][j]+v, ans[-1]+v)
                        #     print("oo","oo" in duplicate)
                        break
                
        ANS.append(ans)
    # print(duplicate)
    print("\n".join(["".join(ans) for ans in ANS]))
    
if __name__ == '__main__':
    main()
