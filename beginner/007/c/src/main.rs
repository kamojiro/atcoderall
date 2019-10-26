#![allow(non_snake_case)]
use std::collections::VecDeque;
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let r :usize = sc.read();
    let c :usize = sc.read();
    let mut sy:usize = sc.read();
    let mut sx:usize = sc.read();
    let mut gy:usize = sc.read();
    let mut gx:usize = sc.read();
    let mut path:Vec<Vec<char>> = Vec::new();
    for _ in 0..r{
        let path_line = sc.chars();
        path.push(path_line);
    }
    
    sy -= 1;
    sx -= 1;
    gy -= 1;
    gx -= 1;
    let mut q = VecDeque::new();
    q.push_front((sy, sx));
    let mut b = vec![vec![-1; c];r];
    b[sy][sx] = 0;
    let mut ans = 0;
    while q.len() > 0{
        let (y,x) = q.pop_back().unwrap();
        if (y == gy) && (x == gx) {
            ans = b[y][x];
            break;
        }
        let t = b[y][x] + 1;
        if y > 0{
            if (b[y-1][x] == -1) && (path[y-1][x] == '.'){
                b[y-1][x] = t;
                q.push_front((y-1, x))
            }
        }
        if y < r-1{
            if (b[y+1][x] == -1) && (path[y+1][x] == '.'){
                b[y+1][x] = t;
                q.push_front((y+1, x))
            }
        }
        if x > 0{
            if (b[y][x-1] == -1) && (path[y][x-1] == '.'){
                b[y][x-1] = t;
                q.push_front((y, x-1))
            }
        }
        if x < c-1{
            if (b[y][x+1] == -1) && (path[y][x+1] == '.'){
                b[y][x+1] = t;
                q.push_front((y, x+1))
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


