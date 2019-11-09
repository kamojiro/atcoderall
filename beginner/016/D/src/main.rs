#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let ax:i32 = sc.read();
    let ay:i32 = sc.read();
    let bx:i32 = sc.read();
    let by:i32 = sc.read();
    let N:usize = sc.read();
    let mut XY: Vec<(i32, i32)> = Vec::new();
    for _ in 0..N {
        let xy:(i32, i32) = (sc.read(), sc.read());
        XY.push(xy);
    }
    let mut ans = 0;
    let a = ay - by;
    let b = bx - ax;
    let c = ay*bx - by*ax;
    let mut ax = ax as f64;
    let mut bx = bx as f64;
    if ax > bx{
        let x = ax;
        ax = bx;
        bx = x;
    }
    for i in 0..N{
        let j = (i+1)%N;
        let d = XY[i].1 - XY[j].1;
        let e = XY[j].0 - XY[i].0;
        let f = XY[i].1*XY[j].0 - XY[j].1 * XY[i].0;
        if e*a == b*d{
            continue;
        }
        let t:f64 = ((e as f64)*(c as f64) - (b as f64)*(f as f64))/((e as f64)*(a as f64) - (b as f64)*(d as f64));
        if (ax <= t) && (t <= bx){
            ans += 1;
        }
//        println!("{} {} {} {} {}", ans, XY[i].0, XY[i].1, XY[j].0, XY[j].1);
    }

    println!("{}", ans/2+1);

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


