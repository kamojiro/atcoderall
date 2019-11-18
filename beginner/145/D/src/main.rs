#![allow(non_snake_case)]
const MOD: usize = 1_000_000_007;
//https://atcoder.jp/contests/abc145/submissions/8503758
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let X:usize = sc.read();
    let Y:usize = sc.read();
    if (X+Y)%3 != 0{
        println!("0");
        return
    }
    let N = (X+Y)/3;
    if (X < N) || (Y < N){
        println!("0");
        return
    }
    if (X+Y)%3 != 0{
        println!("0");
        return
    }
    let x = X - N;
    let y = Y - N;
    println!("{}", comb(x+y,x));
}

fn comb(n: usize, k:usize) -> usize{
    let mut t = 1;
    let mut s = n%MOD;
    
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


