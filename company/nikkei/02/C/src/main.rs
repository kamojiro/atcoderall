#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let mut A:Vec<usize> = sc.vec(N);
    let mut B:Vec<usize> = sc.vec(N);
    let mut check = false;
    for i in 0..N{
        if A[i] <= B[i] {
            check = true;
        }
    }
    let mut j:usize = 0;

    for i in 1..N{
        
    }
    A.sort();
    B.sort();
    for i in 0..N{
        if A[i] > B[i]{
            println!("No");
            return
        }
    }
    if check{
        println!("Yes");
    }else{
        println!("No");
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


