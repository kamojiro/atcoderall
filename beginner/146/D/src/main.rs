#![allow(non_snake_case)]
use std::collections::VecDeque;
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let mut E:Vec<Vec<(usize, usize)>> = vec![vec![];N];
    for i in 0..(N-1){
        let mut a: usize = sc.read();
        let mut b: usize = sc.read();
        a -= 1;
        b -= 1;
        E[a].push((b,i));
        E[b].push((a,i));    
    }
    let mut d:VecDeque<usize> = VecDeque::new();
    let mut Ans:Vec<usize> = vec![0;N];
    
    d.push_back(0);
    while let Some(v) = d.pop_front(){
        let mut num:usize = 1;
        let mut before:usize = 0;
        for i in 0..(E[v].len()){
            if Ans[E[v][i].1] > 0{
                before = Ans[E[v][i].1];
                break
            }
        }
//        println!("{}", v);
        for i in 0..(E[v].len()){
            if num == before{
                num += 1;
            }
            if Ans[E[v][i].1] == 0{
                Ans[E[v][i].1] = num;
//                println!("hoge {}", E[v][i].0);
                d.push_back(E[v][i].0);
                num += 1;
            }
        }
    }
    let mut ans:usize = 1;
    for i in 0..(N-1){
        if Ans[i] > ans{
            ans = Ans[i];
        }
    }
    println!("{}", ans);
    for i in 0..(N-1){
        println!("{}", Ans[i]);
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


