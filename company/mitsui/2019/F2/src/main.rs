#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let T1:i64 = sc.read();
    let T2:i64 = sc.read();
    let A1:i64 = sc.read();
    let A2:i64 = sc.read();
    let B1:i64 = sc.read();
    let B2:i64 = sc.read();
    if T1*A1 + T2*A2 == T1*B1 + T2*B2 {
        println!("infinity");
        return
    }
    let mut F = A1 - B1;
    let mut S = A2 - B2;
    if (F > 0) && ( S > 00){
        println!("0");
        return
    }
    if ( F < 0) && (S < 0){
        println!("0");
        return
    }
    if F < 0{
        F = -F;
        S = -S;
    }
    if F*T1 + S*T2 > 0{
        println!("0");
        return
    }
    let M = F*T1;
    let m = -(F*T1+S*T2);
    if M%m > 0{
        println!("{}", M/m*2+1);
    }else{
        println!("{}", M/m*2);
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



