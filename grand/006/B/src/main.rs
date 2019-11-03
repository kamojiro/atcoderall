#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N :usize = sc.read();
    let x: usize = sc.read();
    if (2 <= x) && (x<= N*2-2) {
        println!("Yes");
    }else{
        println!("No");
        return;
    }

    if x == N {
        for i in 1..(N*2) {
            print!("{} ",i );
        }
        println!();
        return;
    }

    let mut ans = vec![0; N*2];
    let mut check = vec![0; N*2];
    ans[N] = x;
    check[x] = 1;
    if x < N{
        ans[N-1] = x-1;
        check[x-1] = 1;
        for i in (x+1)..(N+1){
            ans[i-2] = i;
            check[i] = 1;
        }

    }else{
        ans[N+1] = x+1;
        check[x+1] = 1;
        for i in (N+2)..(x+1){
            ans[i] = i-2;
            check[i-2] = 1;
        }
    }
    let mut t:usize = 1;
    // for i in 1..(N*2){
    //     println!("{} {}", ans[i], check[i]);
    // }
    for i in 1..(N*2){
        if check[i] != 0{
            continue;
        }
        while ans[t] > 0{
            t += 1;
        }
        ans[t] = i;
        check[i] = 1;
        t += 1;
    }

    for i in 1..(N*2){
        print!("{} ", ans[i]);
    }
    println!("");
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


