#![allow(non_snake_case)]
struct UnionFind {
    p: Vec<i32>,
}
 
impl UnionFind {
    pub fn new (n: usize) -> UnionFind {
        UnionFind {
            p: vec![-1; n],
        }
    }
    pub fn root (&mut self, x: usize) -> usize {
        if self.p[x] < 0 {
            return x;
        }
        let p = self.p[x] as usize;
        let y = self.root (p);
        self.p[x] = y as i32;
        y
    }
    pub fn same (&mut self, x: usize, y: usize) -> bool {
        self.root (x) == self.root (y)
    }
    pub fn unite (&mut self, mut x: usize, mut y: usize) {
        x = self.root (x);
        y = self.root (y);
        if x == y {
            return;
        }
        if self.p[x] > self.p[y] {
            std::mem::swap (&mut x, &mut y);
        }
        self.p[x] += self.p[y];
        self.p[y] = x as i32;
    }
}

fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let n:usize = sc.read();
    let q:usize = sc.read();
    let mut u = UnionFind::new(n+1);
    for _ in 0..q{
        let w: Vec<i32> = sc.vec(3);
        let (p, a, b) = (w[0], w[1], w[2]);
        if p == 0 {
            u.unite(a as usize,b as usize);
        }else{
            if u.same(a as usize,b as usize){
                println!("Yes");
            }else{
                println!("No");
            }
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


