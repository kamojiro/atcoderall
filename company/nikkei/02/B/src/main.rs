#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let Q: usize = 998244353;
    let N:usize = sc.read();
    // if N == 1{
    //     let t:usize = sc.read();
    //     if t == 0{
    //         println!("1");
    //     }else{
    //         println!("0");
    //     }
    //     return
    // }
    let V:Vec<usize> = sc.vec(N);
    let mut now:usize = 1;
    let mut VC:Vec<usize> = vec![0;N];
    for i in 0..N{
        VC[V[i]] += 1;
    }
    if V[0] != 0{
        println!("0");
        return        
    }
    if VC[0] != 1{
        println!("0");
        return
    }

    // let mut check:usize = 0;
    
    // for i in 0..N{
    //     // if VC[i] >= N{
    //     //     println!("0");
    //     //     return
    //     // }
    //     if VC[i] == 0{
    //         println!("0");
    //         return
    //     }
    //     check += VC[i];
    //     if check == N{
    //         break;
    //     }
    // }
    // // for i in 0..4{
    // //     println!("{} {}",i, VC[i] );
    // // }
    let mut ans :usize = 1;
    for i in 1..N{
        for _ in 0..VC[i]{
            ans *= now;
            ans %= Q;
        }
        now = VC[i];
        // if now == 0{
        //     break;
        // }
    }

    println!("{}", ans%Q);
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


