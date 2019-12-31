#![allow(non_snake_case)]
use std::collections::VecDeque;

fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let mut u:usize = sc.read();
    let mut v:usize = sc.read();
    u -= 1;
    v -= 1;
    let mut edges:Vec< Vec<usize>> = vec![vec![]; N];
    for _ in 0..(N-1){
        let a:usize = sc.read();
        let b:usize = sc.read();
        edges[a-1].push(b-1);
        edges[b-1].push(a-1);
    }
    let mut shortest:Vec<i64> = vec![-1; N];
    let mut q:VecDeque<usize> = VecDeque::new();
    q.push_back(v);
    shortest[v] = 0;
    while let Some(t) = q.pop_front(){
        let cnt = shortest[t];
        for i in 0..(edges[t].len()){
            if shortest[edges[t][i]] == -1{
                shortest[edges[t][i]] = cnt + 1;
                if edges[t][i] == u{
                    break
                }
                q.push_back(edges[t][i]);
            }
        }
    }
    let ac = shortest[u] as usize;
    let startc = ac - (ac - 1)/2;
    let mut count:usize = ac;
    let mut start = u;
    let ans:usize = startc;
    while count > startc{
        for i in 0..(edges[start].len()){
            if shortest[edges[start][i]] as usize == count-1{
                count -= 1;
                start = edges[start][i];
            }
        }
    }
    let mut aoki:usize = v;
    for i in 0..(edges[start].len()){
        if shortest[edges[start][i]] as usize == count-1{
            aoki = edges[start][i];
        }
    }

    let mut shortest:Vec<i64> = vec![-1; N];
    let mut q:VecDeque<usize> = VecDeque::new();
    q.push_back(start);
    shortest[start] = 0;
    shortest[aoki] = 0;
//    println!("{} s{}", aoki, start);
    while let Some(t) = q.pop_front(){
        let cnt = shortest[t];
        for i in 0..(edges[t].len()){
            if shortest[edges[t][i]] == -1{
                shortest[edges[t][i]] = cnt + 1;
                q.push_back(edges[t][i]);
            }
        }
    }
    let mut saidai:i64 = 0;
    for i in 0..N{
        if saidai < shortest[i]{
            saidai = shortest[i];
        }
    }
//    println!("{} {}",ans, saidai );
    println!("{}", (ans as i64) + saidai-1);
    




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



