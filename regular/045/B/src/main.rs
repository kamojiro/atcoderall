#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let M:usize = sc.read();
    let mut intervals: Vec<(usize, usize)> = vec![];

    let mut rooms:Vec<i32> = vec![0;N+1];
    for _ in 0..M{
        let (s, t):(usize, usize) = (sc.read(), sc.read());
        rooms[s-1] += 1;
        rooms[t] -= 1;
        intervals.push((s-1, t-1));
    }
    
    for i in 0..N{
        rooms[i+1] += rooms[i];
    }
    let mut multirooms:Vec<i32> = vec![];
    for i in 0..N{
        multirooms.push(i as i32);
    }
    let mut now:i32 = -1;
    for i in 0..N{
        if rooms[i] > 1 {
            if now >= 0{
                union( &mut multirooms, now, i as i32);
            }else{
                now = i as i32;
            }
        }else{
            now = -1;
        }
    }
    
    let mut ans:usize = 0;
    let mut ANS:Vec<usize> = vec![];

    for i in 0..M{
        if (find(&mut multirooms, intervals[i].0 as i32) == find(&mut multirooms, intervals[i].1 as i32)) && (rooms[find(&mut multirooms, intervals[i].0 as i32) as usize] > 1){
            ans += 1;
            ANS.push(i+1);
        }
    }
    println!("{}", ans);
    for i in 0..ANS.len(){
        println!("{}", ANS[i]);
    }
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


