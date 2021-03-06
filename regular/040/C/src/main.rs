#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let S:Vec< Vec< char>> = (0..N).map(|_| sc.chars()).collect();
    let mut V: Vec< Vec< usize>> = vec![ vec![0;N];N];
    let mut ans:usize = 0;

    for i in 0..N{
        for j in (0..N).rev(){
            if (S[i][j] == '.') && (V[i][j] == 0){
                break
            }
            V[i][j] = 2;
        }
        let mut m:usize = 0;
        let mut used = false;
        for j in 0..N{
            if V[i][j] == 0{
                used = true;
            }
        }
        if used{
            ans += 1
        }
        for j in 0..N{
            if used{
                V[i+m][j] = 1;
            }
            if (j < N-1) && (m == 0){
                if V[i][j+1] == 2{
                    if i < N-1{
                        m = 1;
                        V[i+1][j] = 1;
                    }
                }
            }
        }
        if (i < N-1) && used{
                V[i+1][N-1] = 1;
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


