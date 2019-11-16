#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let T:usize = sc.read();
    let mut A: Vec<usize> = vec![];
    let mut B:Vec<usize> = vec![];
    for _ in 0..N{
        let a:usize = sc.read();
        let b:usize = sc.read();
        A.push(a);
        B.push(b);
    }
    let mut ans:usize = 0;


    for j in 0..N{
    let mut dp: Vec< Vec<usize>> = vec![ vec![0; T]; N+1];
        for i in 0..N{
            if i == j{
                for t in 0..T{
                    dp[i+1][t] = dp[i][t];
                }
            }
            let a = A[i];
            let b = B[i];
            for t in 0..a{
                if t >= T{
                    break
                }
                dp[i+1][t] = dp[i][t];
            }
            for t in a..T{
                if dp[i][t] < dp[i][t-a]+b{
                    dp[i+1][t] = dp[i][t-a]+b;
                }else{
                    dp[i+1][t] = dp[i][t];
                }
            }
            
            // for t in T..(T+3000){
            //     if t < a{
            //         continue
            //     }
            //     if dp[i][t] < dp[i][t-a]+b{
            //         dp[i+1][t] = dp[i][t-a]+b;
            //     }else{
            //         dp[i+1][t] = dp[i][t];
            //     }            
            // }
        }
        if ans < dp[N][T-1] + B[j]{
            ans = dp[N][T-1] + B[j];
        }
    }
    // let mut ans:usize = 0;
    // for i in 0..(N+1){
    //     for j in 0..60{
    //         print!("{}", dp[i][j]);
    //     }
    //     println!("");
    // }
    // for i in 0..T{
    //     if ans < dp[N][i]{
    //         ans = dp[N][i];
    //     }
    // }
    // println!("{}", ans);
    // let mut plus:usize = 0;
    // let mut check:Vec<bool> = vec![false; N];
    // let mut a:usize = 0;
    // let mut b:usize = 0;
    // let mut dela:usize = 0;
    // let mut delb:usize = 0;


    // for i in 0..T{
    //     if dp[N][i] > b{
    //         dela = i - a;
    //         delb = dp[N][i] - b;
    //         a = i;
    //         b = dp[N][i];
    //     }
    //     if a == i{
    //         for i in 0..N{
    //             if !check[i]{
    //                 if (A[i] == dela) && (B[i] == delb){
    //                     check[i] = true;
    //                     break
    //                 }
    //             }
    //         }
    //     }
    // }
    // for i in 0..N{
    //     if !check[i]{
    //         if plus < B[i]{
    //             plus = B[i];
    //         }
    //     }
    // }
    
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


