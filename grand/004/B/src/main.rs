#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let x:usize = sc.read();
    let mut A:Vec<(usize, usize)> = vec![];
    let V:Vec<usize> = sc.vec(N);
    for i in 0..N{
        A.push((V[i], i));
    }
    
    for _ in 0..N{
        for i in 0..N{
            let next = (i+1)%N;
            if A[next].0 > A[i].0 + x{
                A[next] = (A[i].0 + x, A[i].1);
            }
        }
    }
    let mut ans:usize = 0;
    for i in 0..N{
        if ans < (A[i].0 - V[A[i].1])/x{
            ans = (A[i].0 - A[i].1)/x;
        }
    }
    ans *= x;
    for i in 0..N{
        ans += V[A[i].1]
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


