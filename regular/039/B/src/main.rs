#![allow(non_snake_case)]
fn main() {
    let Q:usize = 1000_000_007;
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let K:usize = sc.read();
    if N > K{
        println!("{}", comb(K+N-1,N-1,Q));
        return
    }
    let k = K-N;
    let t = k%N;
    // let mut ans:usize = 1;
    
    // for i in (N-t+1)..(N+1){
    //     ans *= i;
    //     ans %= Q;
    // }
    // for i in 1..(t+1){
    //     ans *= powmod(i, Q-2, Q);
    //     ans %= Q;
    // }
    println!("{}", comb(N,t,Q));


}

fn comb(n:usize, k:usize, Q:usize) -> usize{
    if n < k{
        return 0
    }
    let m = if k < n-k {k} else {n-k};
    let mut nu = 1;
    let mut de = 1;
    for i in 0..m{
        nu = nu*(n-i)%Q;
        de = de*(i+1)%Q;
    }
    nu*mod_pow(de, Q-2,Q)%Q
}

// fn comb(n:usize, k:usize, Q:usize) -> usize{
//     if n< k{
//         return 0
//     }
//     let mut ret:usize = 1;

//     for i in (n-k+1)..(n+1){
//         ret *= i;
//         ret %= Q;
//     }
//     for i in 1..(k+1){
//         ret *= mod_pow(i,Q-2,Q);
//         ret %= Q;
//     }
//     ret
// }

fn mod_pow(t:usize, power: usize, Q:usize) -> usize {
    let mut ret = 1;
    let mut a = t;
    let mut p = power;
    while p > 0{
        if (p&1) == 1{
            ret = ret*a%Q;
        }
        a = a*a%Q;
        p >>= 1;
    }
    ret
}


// fn powmod(t:usize, power: usize, Q:usize) -> usize {
//     let mut two_adic:Vec<usize> = vec![];
//     let mut p:usize = power;
//     let mut ret:usize = 1;

//     while p != (0 as usize){
//         two_adic.push(p%2);
//         p /= 2;
//     }
//     for i in (0..two_adic.len()).rev(){
//         ret *= ret;
//         ret %= Q;
//         if two_adic[i] == 1{
//             ret *= t;
//             ret %= Q;
//         }
//     }
//     ret
// }

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


