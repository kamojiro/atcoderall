#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let X:usize = sc.read();
    let Y:usize = sc.read();
    let mut ans:usize = 0;
    if X == 1{
        ans += 300_000;
    }else if X == 2{
        ans += 200_000;
    }else if X == 3{
        ans += 100_000;
    }
    if Y == 1{
        ans += 300_000;
    }else if Y == 2{
        ans += 200_000;
    }else if Y == 3{
        ans += 100_000;
    }

    if (X == 1) && (Y == 1) {
        ans += 400_000;
    }
    println!("{}", ans);
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


