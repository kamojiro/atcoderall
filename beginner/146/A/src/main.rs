#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let S:String = sc.read();
    let mut ans:usize = 0;

    if S == "SUN"{
        ans = 7;
        println!("{}", ans);
    }else if S == "MON" {
        ans = 6;
        println!("{}", ans);
    }else if S == "TUE" {
        ans = 5;
        println!("{}", ans);

    }else if S == "WED" {
        ans = 4;
        println!("{}", ans);

    }else if S == "THU" {
        ans = 3;
        println!("{}", ans);

    }else if S == "FRI" {
        ans = 2;
        println!("{}", ans);

    }else if S == "SAT" {
        ans = 1;
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


