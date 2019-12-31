#![allow(non_snake_case)]

fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let mut dp:Vec<Vec<Vec<f64>>> = vec![vec![vec![-1 as f64;301];301];301];
    let N:usize = sc.read();
    let A:Vec<usize> = sc.vec(N);
    let mut count:Vec<usize> = vec![0;4];
    for a in A{
        count[a] += 1;
    }
    println!("{}", memodp(&mut dp, count[1], count[2], count[3], N));


}

fn memodp(dp:&mut Vec<Vec<Vec<f64>>>, i:usize, j:usize, k:usize, N:usize) -> f64{
    if dp[i][j][k] >= 0.0{
        return dp[i][j][k]
    }
    if (i == 0) && (j == 0) && (k == 0){
        return 0f64
    }
    let mut res = N as f64;
    if i > 0{
        res += memodp(dp,i-1,j,k,N)*(i as f64)
    }
    if j > 0{
        res += memodp(dp,i+1,j-1,k,N)*(j as f64)
    }
    if k > 0{
        res += memodp(dp,i,j+1,k-1,N)*(k as f64)
    }
    dp[i][j][k] = res/((i+j+k) as f64);
    dp[i][j][k]
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


