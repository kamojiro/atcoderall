
#![allow(non_snake_case)]
use std::collections::VecDeque;

fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let M:usize = sc.read();
    let mut E: Vec< Vec<usize>> = vec![vec![];N];
    let mut Vcount:Vec<usize> = vec![0;N];

    for _ in 0..(N+M-1) {
        let mut a:usize = sc.read();
        let mut b:usize = sc.read();
        a -= 1;
        b -= 1;
        E[a].push(b);
        Vcount[b] += 1;
    }
    let mut q:VecDeque<usize> = VecDeque::new();
    for i in 0..N{
        if Vcount[i] == 0{
            q.push_back(i);
        }
    }
    let mut ans:Vec<usize> = vec![N;N];

    while let Some(v) = q.pop_front(){
        for &w in E[v].iter(){
            Vcount[w] -= 1;
            if Vcount[w] == 0{
                q.push_back(w);
                ans[w] = v;
            }

        }
    }
    for i in 0..N{
        if ans[i] == N{
            println!("0");
        }else{
            println!("{}", ans[i]+1);
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


