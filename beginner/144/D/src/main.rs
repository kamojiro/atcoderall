#![allow(non_snake_case)]
//use std::f64::consts;
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let a:f64 = sc.read();
    let b:f64 = sc.read();
    let x:f64 = sc.read();
//    let angle = consts::PI * (180 as f64);
    if (a as usize)*(a as usize)*(b as usize) <= (x as usize)*(2 as usize) {
        println!("{}", ((a*a*b - x)*(2 as f64)/(a*a*a)).atan().to_degrees());
    }else{
        
        println!("{}", ((a*b*b)/((2 as f64)*x)).atan().to_degrees());
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


