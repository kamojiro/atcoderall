#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let n:usize = sc.read();
    let k:i64 = sc.read();
    let mut a:Vec<i64> = sc.vec(n);
    let mut f:Vec<i64> = sc.vec(n);
    a.sort();
    f.sort();

    let mut l: i64 = 0;
    let mut r: i64 = 1000000000001;
    while r - l >= 2{
        let m = (l+r)/2;
        let mut t: i64 = 0;
        for i in 0..n{
            if a[i]*f[n-1-i] <= m{
                continue
            }
            t += (a[i]*f[n-1-i]-m+f[n-1-i]-1)/f[n-1-i];
        }
//        println!("{} {} {} {}", t,l, m,r );
        if t <= k{
            r = m
        }else{
            l = m
        }
    }
    // if l == 0 {
    //     println!("{}", l);
    // }else{
    //     println!("{}", l+1);
    // }
    let mut g:i64 = 0;
    for i in 0..n {
        g += a[i];
    }

    if g <= k{
        println!("0");
    }else{
        println!("{}", r);
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


