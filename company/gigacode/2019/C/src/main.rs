#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let D:usize = sc.read();
    let A: Vec< usize> = sc.vec(D);
    let B: Vec<usize> = sc.vec(D);
    let mut now:usize = 0;
    let mut ans: usize = 3_000_000_000;
    for i in 0..D{
        now += A[i];
        if B[i] <= now{
            if B[i] < ans{
                ans = B[i];
            }
        }
    }
    if ans == 3_000_000_000{
        println!("-1");
    }else{
        println!("{}", ans);
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


