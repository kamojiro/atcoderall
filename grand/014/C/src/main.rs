#![allow(non_snake_case)]
use std::collections::VecDeque;
use std::cmp::min;
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let H:usize = sc.read();
    let W:usize = sc.read();
    let K:usize = sc.read();
    let A: Vec< Vec<char>> = (0..H).map(|_| sc.chars()).collect();

    let mut V: Vec< Vec<usize>> = vec![ vec![K+1;W];H];
    let mut q: VecDeque< (usize, usize)> = VecDeque::new();
    let mut m:usize = H;
    for i in 0..H{
        for j  in 0..W{
            if A[i][j] == 'S' {
                V[i][j] = 0;
                q.push_back((i, j));
                m = min(m, i);
                m = min(m, H-1-i);
                m = min(m, j);
                m = min(m, W-1-j); 
                break;
            }
        }
        if !q.is_empty(){
            break;
        }
    }
    while let Some((u, v)) = q.pop_front(){
        let t = V[u][v];
        if 0 < u{
            if (A[u-1][v] == '.') && (V[u-1][v] == K+1){
                V[u-1][v] = t+1;
                m = min(m, u-1);
                if t+1 < K{
                    q.push_back((u-1,v))
                }
            }
        }
        if u < H-1{
            if (A[u+1][v] == '.')&&(V[u+1][v] == K+1) {
                V[u+1][v] = t+1;
                m = min(m, H-1-(u+1));
                if t+1 < K{
                    q.push_back((u+1,v));
                }
            }
        }
        if 0 < v{
            if (A[u][v-1] == '.') && (V[u][v-1] == K+1){
                V[u][v-1] = t+1;
                m = min(m, v-1);
                if t+1 < K{
                    q.push_back((u,v-1))
                }
            }
        }
        if v < W-1{
            if (A[u][v+1] == '.')&&(V[u][v+1] == K+1) {
                V[u][v+1] = t+1;
                m = min(m, W-1-(v+1));
                if t+1 < K{
                    q.push_back((u,v+1));
                }
            }
        }
    }
    if m == 0{
        println!("1");
        return
    }else{
        println!("{}", (m+(K-1))/K+1);
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


