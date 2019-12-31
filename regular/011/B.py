#import sys
#input = sys.stdin.readline
def main():
    d = dict()
    d["a"] = ""
    d["i"] = ""
    d["u"] = ""
    d["e"] = ""
    d["o"] = ""
    d["y"] = ""
    d["b"] = "1"
    d["c"] = "1"
    d["d"] = "2"
    d["w"] = "2"
    d["t"] = "3"
    d["j"] = "3"
    d["f"] = "4"
    d["q"] = "4"
    d["l"] = "5"
    d["v"] = "5"
    d["s"] = "6"
    d["x"] = "6"
    d["p"] = "7"
    d["m"] = "7"
    d["h"] = "8"
    d["k"] = "8"
    d["n"] = "9"
    d["g"] = "9"
    d["z"] = "0"
    d["r"] = "0"
    d[" "] = " "
    d["."] = ""
    d[","] = ""

    for i in range(26):
        d[chr(i + ord("A") )] = d[chr(i + ord("a"))]
    
    ans = []
    N = int( input())
    W = input()
    now = ""
    for w in W:
        if d[w] == "":
            continue
        if now == d[w] and d[w] == " ":
            now = d[w]
            continue
        ans.append(d[w])
        now = d[w]
        
    
    print("".join(ans).strip())

if __name__ == '__main__':
    main()
