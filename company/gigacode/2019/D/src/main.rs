#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let H:usize = sc.read();
    let W:usize = sc.read();
    let K:usize = sc.read();
    let V:usize = sc.read();

    let A: Vec< Vec<usize>> = (0..H).map(|_| sc.vec(W)).collect();
    let mut B: Vec< Vec< usize>> = vec![ vec![0;W+1]; H+1];
    for i in 1..(H+1){
        for j in 0..W{
            B[i][j+1] = B[i][j] + A[i-1][j];
        }
    }

    for j in 1..(W+1){
        for i in 0..H{
            B[i+1][j] += B[i][j];
        }
    }
    let mut ans:usize = 0;

    for i in 0..H{
        for j in 0..W{
            if (H-i)*(W-j) < ans{
                break
            }
            let mut e:usize = 1;
            if ans/(W-j) > 1{
                e = ans/(W-j);
            }
            for k in (i+e)..(H+1){
                let mut d:usize = 1;
                if ans/(k-i) < 1{
                    d = ans/(k-i);
                }
                for l in (j+d)..(W+1){
                    if B[k][l]  + B[i][j] - B[i][l] - B[k][j] + (k-i)*(l-j)*K <= V{
                        if ans < (k-i)*(l-j){
                            ans = (k-i)*(l-j);
                        }
                    }else{
                        break
                    }
                }
            }
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


