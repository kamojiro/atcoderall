#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    // let mut A:Vec<usize> = vec![];
    // let mut B:Vec<usize> = vec![];
    let mut ans:usize = 1_000_000_000;
//    let mut same = true;
    let mut sum:usize = 0;
    for _ in 0..N{
        let a:usize = sc.read();
        let b:usize = sc.read();
        // if a ! b{
        //     same = false;
        // }
        sum += b;
        if a > b{
            if b < ans{
                ans = b;
            }
        }
       // A.push(a);
       // B.push(b);
    }
    if ans == 1_000_000_000{
        println!("0");
    }else{
        println!("{}", sum - ans);
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


