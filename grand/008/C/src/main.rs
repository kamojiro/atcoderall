#![allow(non_snake_case)]

fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let mut v: Vec<usize> = sc.vec(7);
    let mut ans:usize = v[1];
    let mut even:usize = 0;
    if v[0]%2 == 0{
        even += 1;
    }
    if v[3]%2 == 0{
        even += 1;
    }
    if v[4]%2 == 0{
        even += 1
    }
    if even <= 1{
        if (v[0] > 0) && (v[3] > 0) && (v[4] > 0){
            ans += 3;
            v[0] -= 1;
            v[3] -= 1;
            v[4] -= 1;
        }
    }
    ans += v[0]/2*2;
    ans += v[3]/2*2;
    ans += v[4]/2*2;
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


