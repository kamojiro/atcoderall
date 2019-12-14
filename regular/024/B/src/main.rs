#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let colors:Vec<usize> = sc.vec(N);
    let mut start:usize = colors[0];
    for i in 1..N{
        if colors[0] != colors[i]{
            start = i;
            break
        }
    }
    if colors[0] == colors[start]{
        println!("-1");
        return
    }
    let mut state:usize = colors[start];
    let mut count:usize = 1;
    let mut max_count:usize = 1;

    for i in 1..N{
        if state == colors[(start + i)%N]{
            count += 1;
        }else{
            if count > max_count{
                max_count = count;
            }
            state = colors[(start + i)%N];
            count = 1;
        }
    }
    if count > max_count{
        max_count = count;
    }
    println!("{}", (max_count - 1)/2+1);

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


