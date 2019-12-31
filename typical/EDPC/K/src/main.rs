#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let K:usize = sc.read();
    let A:Vec<usize> = sc.vec(N);
    let mut dp = vec![vec![true;2];K+1];
    for i in 0..A[0]{
        dp[i][0] = false;
        dp[i][1] = true;
    }
    for k in A[0]..(K+1){
        let mut win = false;
        for i in 0..(A.len()){
            let a = A[i];
            if a <= k{
                if dp[k-a][1]{
                    win = true;
                    break
                }
            }
        }
        dp[k][0] = win;
        win = true;
        for i in 0..(A.len()){
            let a = A[i];
            if a <= k{
                if !dp[k-a][0]{
                    win = false;
                    break
                }
            }
        }
        dp[k][1] = win;
    }
    if dp[K][0]{
        println!("First");
    }
    else{
        println!("Second");
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


