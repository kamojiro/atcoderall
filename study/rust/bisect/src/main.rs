#![allow(non_snake_case)]
fn main() {

    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let n:usize = sc.read();
    let mut l:Vec<i32> = sc.vec(n);
    let t:i32 = sc.read();
    let mut ans:i64 = 0;
    l.sort();
    println!("{}", bisect_left(&l,t,n));
    println!("{}", bisect_right(&l,t,n));    
}


fn bisect_left(v: &[i32], t: i32, n: usize)->i32{
    if v[0] > t{
        return 0
    }
    let mut l:usize =0;
    let mut r:usize =n;
    let mut m;
    while r-l >= 2{
        m = (l+r)/2;
        if v[m] >= t{
            r = m;
        }else{
            l = m;
        }
    }
    r as i32
}

fn bisect_right(v: &[i32], t: i32, n: usize)->i32{
    if v[0] > t{
        return 0
    }
    let mut l:usize =0;
    let mut r:usize =n;
    let mut m;
    while r-l >= 2{
        m = (l+r)/2;
        if v[m] <= t{
            l = m;
        }else{
            r = m;
        }
    }
    r as i32
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


