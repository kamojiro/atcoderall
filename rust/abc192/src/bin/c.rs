#![allow(non_snake_case)]
use proconio::{input, fastout};

fn f(x: i64) -> i64 {
    let mut t = x;
    let mut p:Vec<i64> = vec![0;10];
    while t > 0 {
        p[(t%10) as usize] += 1;
        t /= 10;
    }
    let mut q = p.clone();
    let mut g1:i64 = 0;
    let mut g2:i64 = 0;

    for i in 0..10{
        while p[i] > 0{
            g2 = g2*10 + (i as i64);
            p[i] -= 1;
        }
    }

    for i in (0..10).rev(){
        while q[i] > 0{
            g1 = g1*10 + (i as i64);
            q[i] -= 1;
        }
    }
    g1 - g2
}

#[fastout]
fn main() {
    input!{
        N: i64,
        K: usize,
    }
    let mut a = N;
    for _ in 0..K{
        a = f(a);
    }
    println!("{}", a);
}
