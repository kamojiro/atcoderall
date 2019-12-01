#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let Q:usize = 1000_000_007;
    let mut R:usize = 0;
    let mut G:usize = 0;
    let mut B:usize = 0;
    let N:usize = sc.read();
    let A:Vec<usize> = sc.vec(N);
    if A[0] > 0{
        println!("0");
        return
    }
    let mut dp:Vec<usize> = vec![0;N];
    dp[0] = 3;
    R += 1;
    for i in 1..N{
        if (A[i] != R) && ( A[i] != G) && (A[i] != B){
            println!("0");
            return
        }
        if (R == G) && ( G == B ){
            dp[i] = dp[i-1]*3%Q;
            R += 1;
            continue
        }
        if (R == A[i]) && (G == A[i]){
            dp[i] = dp[i-1]*2%Q;
            R += 1;
            continue
        }
        if (G == A[i]) && (B == A[i]) {
            dp[i] = dp[i-1]*2%Q;
            G += 1;
            continue
        }
        if (B == A[i]) && (R == A[i]) {
            dp[i] = dp[i-1]*2%Q;
            B += 1;
            continue

        }
        if R == A[i]{
            dp[i] = dp[i-1];
            R += 1;
            continue
        }
        if G == A[i]{
            dp[i] = dp[i-1];
            G += 1;
            continue
        }
        if B == A[i]{
            dp[i] = dp[i-1];
            B += 1;
            continue
        }
    }
    println!("{}", dp[N-1]);


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


