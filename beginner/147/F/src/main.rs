#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let mut X:i64 = sc.read();
    let mut D:i64 = sc.read();
    if D == 0{
        if X == 0{
            println!("1");
        }else{
            println!("{}", N+1);
        }
        return
    }
    if D < 0{
        X = -X;
        D = -D;
    }
    let mut map = std::collections::BTreeMap::<i64, Vec<(i64, i64)>>::new();
    for k in 0..(N+1){
        let t = k as i64;
        let tX = X*t;
        let minimum = tX/D + t*(t-1)/2;
        let maximum = tX/D + ((N as i64)*t - t*(t+1)/2);
//        println!("{} {} tX{} {} {}",N ,t ,tX/D,t*(t+1)/2 , ((N as i64)*t - t*(t+1)/2));
        let corresponding_vector = map.entry(tX%D).or_insert(vec![]);
        corresponding_vector.push((minimum, maximum));
    }

    let mut ans = 0;
    for (_,a) in map{
        let mut a = a;
        a.sort();
        let mut first = a[0].0;
        let mut second = a[0].1;
        for i in 1..a.len(){
//            println!("{} {}", a[i].0, a[i].1);
            if second < a[i].0{
                ans += second - first + 1;
                first = a[i].0;
                second = a[i].1;
            }else if second < a[i].1{
                second = a[i].1;
            }
        }
        ans += second - first + 1;
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


