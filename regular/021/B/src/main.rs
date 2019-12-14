#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let L:usize = sc.read();
    let B:Vec<usize> = sc.vec(L);
    let mut binaryB:Vec< Vec<usize>> = vec![vec![]; L];
    let mut Ans: Vec< Vec< usize>> = vec![vec![0; 31]; L];
    for i in 0..L{
        let mut b = B[i];
        for _ in 0..31{
            binaryB[i].push(b%2);
//            print!("{}", b%2);
            b /= 2;
        }
//        println!("");
    }
    let mut ans = true;
    for i in 0..31{
        if !ans{
            break
        }
        let mut now:usize = 0;
        for j in 0..L{
            now ^= binaryB[j][i];
        }
        if now == 0{
            Ans[0][i] = 0;
            continue;
        }
        now = 1; 

        for j in 0..L{
            now ^= binaryB[j][i];
        }
        if now == 1{
            Ans[0][i] = 1;
            continue;
        }else{
            ans = false;
        }
    }
    if !ans{
        println!("-1");
        return
    }
    for i in 0..31{
        for j in 1..L{
            Ans[j][i] = Ans[j-1][i]^binaryB[j-1][i];
        }
    }
    // for i in 0..L{
    //     for j in 0..31{
    //         print!("{}", Ans[i][j]);
    //     }
    //     println!("");
    // }
    for i in 0..L{
        let mut s = 0;
        let mut power = 1;

        for j in 0..31{
            s += Ans[i][j]*power;
            power *= 2;
        }
        println!("{}", s);
    }
}

pub struct Scanner<R> {
    stdin: R,
}

impl<R: std::io::Read> Scanner<R> {
    pub fn read<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        let buf = self
            .stdin
            .by_ref()
            .bytes()
            .map(|b| b.unwrap())
            .skip_while(|&b| b == b' ' || b == b'\n')
            .take_while(|&b| b != b' ' && b != b'\n')
            .collect::<Vec<_>>();
        unsafe { std::str::from_utf8_unchecked(&buf) }
        .parse()
            .ok()
            .expect("Parse error.")
    }
    pub fn vec<T: std::str::FromStr>(&mut self, n: usize) -> Vec<T> {
        (0..n).map(|_| self.read()).collect()
    }
    pub fn chars(&mut self) -> Vec<char> {
        self.read::<String>().chars().collect()
    }
}


