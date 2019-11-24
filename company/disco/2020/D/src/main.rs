#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let M:usize = sc.read();
    let nums:Vec<(usize, usize)> = (0..M).map(|_| (sc.read(), sc.read())).collect();
    let mut red:Vec<usize> = vec![];
    let mut ans:usize = 0;
    for i in 0..M{
        let d = nums[i].0;
        let mut c = nums[i].1;
        ans += (c-1)/9*(d+9);
        c = c - (c-1)/9*9;
        for _ in 0..c{
            red.push(d);
        }
    }
    let mut now = red[0];
    for i in 1..(red.len()){
        now += red[i];
        ans += 1;
        if now > 9{
            now = (now/10)+(now%10);
            ans += 1;
        }
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


