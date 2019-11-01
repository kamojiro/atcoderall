#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let n:usize = sc.read();
    let m:usize = sc.read();

    let mut v: Vec<Vec<usize>> = vec![ vec![];n];
    for _ in 0..m {
        let a:usize = sc.read();
        let b:usize = sc.read();
        v[a-1].push(b-1);
    }
    
    let mut path: Vec<f64> = vec![0 as f64; n];
    for i in (0..(n-1)).rev(){
        let l:f64 = v[i].len() as f64;
        let mut mass :f64 = 0 as f64;
        for j in 0..(v[i].len()){
            mass += path[v[i][j]];
        }
        path[i] = mass/l+1f64;
    }
    let mut ans: f64 = path[0];

    for k in 0..(n-1) {
        if v[k].len() == 1{
            continue;
        }
        let mut max: f64 = path[v[k][0]];
        for j in 0..(v[k].len()){
            if max < path[v[k][j]]{
                max = path[v[k][j]];
            }
        }

        let mut road: Vec<f64> = vec![0 as f64; n];
        for i in (0..(n-1)).rev(){
            let mut mass :f64 = 0 as f64;
            for j in 0..(v[i].len()){
                mass += road[v[i][j]];
            }
            if i == k{
                mass -= max;
                mass /= (v[i].len()-1) as f64
            }else{
                mass /= v[i].len() as f64
            }
            road[i] = mass + 1f64;
        }
        if ans > road[0]{
            ans = road[0];
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


