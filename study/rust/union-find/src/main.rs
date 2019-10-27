#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let n:usize = sc.read();
    let q:usize = sc.read();
    let mut d:Vec<i32> = vec![];
    let mut ans = String::new();
    for i in 0..n {
        d.push(i as i32);
    }
    for _ in 0..q{
        let w: Vec<i32> = sc.vec(3);
        let (p, a, b) = (w[0], w[1], w[2]);
        if p == 0 {
            union(&mut d, a, b);
        }else{
            if find(&mut d, a) == find(&mut d,b) {
                // println!("Yes");
                ans.push_str("Yes");
            }else{
                // println!("No");
                ans.push_str("No");
            }
            ans.push('\n');
        }
    }
    println!("{}", ans);

}

fn find(v:&mut Vec<i32>, x: i32) -> i32{
    let p = v[x as usize];
    if p == x{
        return x
    }
    let a = find(v,p);
    v[x as usize] = a;
    a
}

fn union(v:&mut Vec<i32>, x: i32, y:i32) {
    let bx: i32;
    let by: i32;

    if find(v, x) > find(v,y) {
        bx = find(v,y);
        by = find(v,x);
    }else{
        bx = find(v,x);
        by = find(v,y);
    }
    v[y as usize] = bx;
    v[by as usize] = bx;
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

