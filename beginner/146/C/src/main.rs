#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let A:i64 = sc.read();
    let B:i64 = sc.read();
    let X:i64 = sc.read();
    if A*1_000_000_000 + B*10 <= X{
        println!("1000000000");
        return
    }
    let mut ans:i64 = 0;

    for i in 1..10{
        if X < B*i{
            break
        }
        let mut t = (X - B*i)/A;
        if t > (10 as i64).pow(i as u32)-1{
            t = (10 as i64).pow(i as u32)-1;
        }
        if t > ans {
            ans = t;
        }
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


