#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    // if prime(N){
    //     println!("Deficient");
    //     return
    // }
    let factors = factors(N);
    let mut sum:usize = factors.iter().sum::<usize>();
//     for &f in &factors{
// //        println!("{}", f);
//         sum += &f;
//     }
    sum -= N;
    if sum == N{
        println!("Perfect");
    }else if sum < N{
        println!("Deficient");
    }else{
        println!("Abundant");
    }
}

// fn prime(n:usize) -> bool{
//     if n == 1{
//         return false
//     }
//     let possible = ((n as f64).sqrt() as usize) + 1;
//     for i in 2..possible{
//         if n%i == 0{
//             return false
//         }
//     }
    
//     true
// }

fn factors(n: usize) -> Vec<usize>{
    //random sort
    if n == 1{
        return vec![1]
    }
    let possible = ((n as f64).sqrt() as usize) + 1;
    let mut ret:Vec<usize> = vec![];

    for i in 1..possible{
        if n%i == 0{
            if i == n/i{
                ret.push(i)
            }else{
                ret.push(i);
                ret.push(n/i);
            }
        }
    }
    ret
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


