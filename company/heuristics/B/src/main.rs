#![allow(non_snake_case)]

fn main() {
    // let s = std::io::stdin();
    // let mut sc = Scanner { stdin: s.lock() };
    let (r, w) = (std::io::stdin(), std::io::stdout());
    let mut sc = IO::new(r.lock(), w.lock());
    //let n: usize = sc.read();
    //let a: Vec<u64> = sc.vec(n);
    //let s = sc.chars();
    //let mut A: Vec<Vec<u64>> = (0..n).map(|_| sc.vec(n)).collect();
    let D:usize = sc.read();
    let C:Vec<i64> = sc.vec(26);
    let S: Vec<Vec<i64>> = (0..D).map(|_| sc.vec(26)).collect();
    let T: Vec<usize> = (0..D).map(|_| sc.read()).collect();
    let mut past: Vec<i64> = (0..26).map(|_| -1).collect();
    let mut ans:i64 = 0;
    for i in 0..D{
        ans += S[i][T[i]-1];
        past[T[i]-1] = i as i64;
        for j in 0..26{
            ans -= C[j]*((i as i64)-past[j]);
        }
        println!("{}", ans);
    }
}

struct IO<R, W: std::io::Write>(R, std::io::BufWriter<W>);


impl<R: std::io::Read, W: std::io::Write> IO<R, W> {
    pub fn new(r: R, w: W) -> Self {
        Self(r, std::io::BufWriter::new(w))
    }
    pub fn read<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        let buf = self
            .0
            .by_ref()
            .bytes()
            .map(|b| b.unwrap())
            .skip_while(|&b| b == b' ' || b == b'\n' || b == b'\r' || b == b'\t')
            .take_while(|&b| b != b' ' && b != b'\n' && b != b'\r' && b != b'\t')
            .collect::<Vec<_>>();
        unsafe { std::str::from_utf8_unchecked(&buf) }
        .parse()
            .ok()
            .expect("Parse error.")
    }
    pub fn vec<T: std::str::FromStr>(&mut self, n: usize) -> Vec<T> {
        (0..n).map(|_| self.read()).collect()
    }
}


