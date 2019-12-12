#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let mut A:Vec< Vec< usize>> = vec![ vec![]; N];
    let mut T:Vec< Vec< usize>> = sc.read();

    for i in 0..N{
        let a:usize = sc.read();
        for _ in 0..a{
            let (x, y): (usize, usize) = (sc.read(), sc.read());
            A[i].append((x-1, y));
        }
    }
    let mut ans:usize = 0;

    for p in 0..(1 << N){
        let mut cnt: usize = 0;
        for i in 0..N{
            if (p & (1 << i)) == 0{
                continue
            }
            cnt += 1;
            for j in 0..N{
//                println!("{} {} {} a{}",p,j, ((p & (1 << j)) >> j) , A[i][j]);
                if A[i][j] == 0{
                    continue
                }
                if ((p & (1 << j))>>j) == {
                    cnt = 0;
                    break
                }
            }
            if cnt == 0{
                break
            }
        }
        println!("{} {}", ans, cnt);
        if ans < cnt{
            ans = cnt;
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


