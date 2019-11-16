#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let S:Vec<char> = sc.chars();
    let T:Vec<char> = sc.chars();
    let q:usize = sc.read();
    let mut query:Vec<Vec<usize>> = vec![];
    for _ in 0..q{
        let v: Vec<usize> = sc.vec(4);
        query.push(v);
    }
    let mut Saccumurate: Vec<usize> = vec![0];
    let mut Taccumurate: Vec<usize> = vec![0];
    for i in 0..S.len(){
        if S[i] == 'A'{
            Saccumurate.push(2);
        }else{
            Saccumurate.push(1);
        }
    }
    for i in 0..T.len(){
        if T[i] == 'A'{
            Taccumurate.push(2);
        }else{
            Taccumurate.push(1);
        }
    }
    for i in 0..S.len(){
        Saccumurate[i+1] += Saccumurate[i];
    }

    for i in 0..T.len(){
        Taccumurate[i+1] += Taccumurate[i];
    }
    for i in 0..q{
        if (Saccumurate[query[i][1]] - Saccumurate[query[i][0]-1])%3 == (Taccumurate[query[i][3]] - Taccumurate[query[i][2]-1])%3{
            println!("YES");
        }else{
            println!("NO");
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


