#![allow(non_snake_case)]
use std::collections::VecDeque;

fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let n:usize = sc.read();
    let mut x:usize = sc.read();
    x -= 1;
    let h:Vec<usize> = sc.vec(n);
    let mut edge:Vec< Vec< usize>> = vec![vec![]; n];
    for _ in 0..(n-1){
        let mut a: usize = sc.read();
        let mut b:usize = sc.read();
        a -= 1;
        b -= 1;
        edge[a].push(b);
        edge[b].push(a);
    }
    let mut reverse_edge: Vec< Option<usize>>= vec![None; n];
    let mut q = VecDeque::new();
    let mut ex = Vec::new();
    reverse_edge[x] = Some(x);
    q.push_back(x);
    while let Some(v) = q.pop_front(){
        for i in 0..edge[v].len(){
            if reverse_edge[edge[v][i]] == None {
                reverse_edge[edge[v][i]] = Some(v);
                if edge[edge[v][i]].len() == (1 as usize){
                    ex.push(edge[v][i]);
                }else{
                    q.push_back(edge[v][i]);
                }
            }
        }
    }
    let mut ans:Vec<usize> = vec![0;n];
    let mut visit:Vec<bool> = vec![false; n];
    for i in 0..ex.len(){
        let v = ex[i];
        let mut t = v;
        let mut check = false;
        while !visit[t]{
            if h[t] == 1{
                check = true;
            }
            if check{
                visit[t] = true;
                ans[t] = 2;
            }
            if let Some(w) = reverse_edge[t]{
                t = w;
            }
            if t == x{
                break;
            }
        }
    }
    // for i in 0..n{
    //     println!("{} {}",i+1, ans[i] );
    // }
    let mut a: usize = 0;
    for t in &ans{
        a += *t;
    }
//    a -= 2;
    println!("{}", a);

    
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


