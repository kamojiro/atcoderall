#![allow(non_snake_case)]
use std::collections::HashMap;
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let K:usize = sc.read();
    let A:Vec<usize> = sc.vec(N);
    let mut ans:usize = 0;
    let mut Acc:Vec<usize> = vec![0;N+1];
    Acc.push(0);
    for i in 0..N{
        Acc[i+1] = (Acc[i]+A[i]-1)%K
    }
    let mut S = HashMap::new();
    for i in 0..(N+1){
        *S.entry(Acc[i]).or_insert(0) += 1;

        if K <= i{
            *S.entry(Acc[i-K]).or_insert(0) -= 1;
        }
        ans += S[&Acc[i]]-1;
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


