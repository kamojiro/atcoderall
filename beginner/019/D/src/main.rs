#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    println!("? 1 2");
    let mut dist:usize = sc.read();
    if N == 2{
        println!("! {}", dist);
        return
    }
    let mut a:usize = 1;
    let mut b:usize = 2;
    
    for v in 3..(N+1){
        println!("? {} {}", v, a);
        let va:usize = sc.read();
        println!("? {} {}", v, b);
        let vb:usize = sc.read();
        let s = (dist + va + vb)/2;
        let x = s - vb;
        let y = s - va;
        let z = s - dist;
        if (x <= y) && (x <= z){
            dist = vb;
            a = v;
            continue
        }
        if (y <= x) && (y <= z){
            dist = va;
            b = v;
            continue
        }
    }
    println!("! {}", dist);

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


