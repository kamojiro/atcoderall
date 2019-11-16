#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let K:usize = sc.read();
    let H: Vec<usize> = sc.vec(N);
    let mut h:usize = 0;
    let mut cnt:usize = 0;
    let mut A:Vec<usize> = vec![];
    let mut B:Vec<usize> = vec![];
    for i in 0..N{
        if h <= H[i]{
            cnt += 1;
        }else{
            cnt = 0
        }
        h = H[i];
        A.push(cnt);
    }
    h = 1000_000_000;
    for i in (0..N).rev(){
        if h >= H[i]{
            cnt += 1;
        }else{
            cnt = 0
        }
        h = H[i];
        B.push(cnt);
    }
    for i in 0..(N-1){
        if A[i] > A[i+1]{
            A[i+1] = A[i];
        }
        if B[i] > B[i+1]{
            B[i+1] = B[i];
        }
    }
    let mut ans: usize = A[N-1];
    if ans < B[N-1]{
        ans = B[N-1];
    }
    for i in 0..(N-1){
        if ans < A[i] + B[N-2-i]{
            ans = A[i] + B[N-2-i]
        }
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


