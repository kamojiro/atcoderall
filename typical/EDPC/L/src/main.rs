#![allow(non_snake_case)]
use std::cmp::{min, max};

fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let A:Vec<usize> = sc.vec(N);
    let mut dp:Vec<Vec<i64>> = vec![vec![-1;N+1];N+1];
    for i in 0..(N+1){
        dp[i][i] = 0;
    }
    let mut s:i64 = 0;
    for i in 0..N{
        s += A[i] as i64;
    }

    println!("{}", 2*(rec(&mut dp, 0, N, N, &A) as i64) - s);

}

fn rec(dp: &mut Vec<Vec<i64>>, l:usize, r:usize, N:usize, A:&Vec<usize>) -> usize{
    if dp[l][r] >= 0{
        return dp[l][r] as usize
    }

    if (N-(r-l))%2 == 1{
        dp[l][r] = min(rec(dp, l+1,r,N,A), rec(dp, l, r-1,N,A)) as i64;
    }else{
        dp[l][r] = max(rec(dp, l+1, r,N,A)+A[l], rec(dp, l,r-1,N,A)+A[r-1]) as i64;
    }
    dp[l][r] as usize
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


