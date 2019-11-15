#![allow(non_snake_case)]

fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let M:usize = sc.read();
    let mut tree:Vec<usize> = (0..(M+1)).collect();
    let mut person:Vec<usize> = vec![];
    for _ in 0..N{
        let k:usize = sc.read();
        let t:usize = sc.read();
        person.push(t);
        for _ in 1..k{
            let s:usize = sc.read();
            union(&mut tree, t, s);
        }
    }
    let mut ans = true;
    let f = find(&mut tree, person[0]);
    for i in 1..N{
        if f != find(&mut tree, person[i]) {
            ans = false;
            break
        }
    }
    if ans{
        println!("YES");
    }else{
        println!("NO");
    }

}

fn find(v:&mut Vec<usize>, x: usize) -> usize{
    let p = v[x];
    if p == x{
        return x
    }
    let a = find(v,p);
    v[x] = a;
    a
}

fn union(v:&mut Vec<usize>, x:usize, y:usize) {
    let bx: usize;
    let by: usize;

    if find(v, x) > find(v,y) {
        bx = find(v,y);
        by = find(v,x);
    }else{
        bx = find(v,x);
        by = find(v,y);
    }
    v[y] = bx;
    v[by] = bx;
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


