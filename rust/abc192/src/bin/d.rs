#![allow(non_snake_case)]
use proconio::{input, fastout};
use proconio::marker::{Chars};

#[fastout]
fn main() {
    input!{
        Y: Chars,
        M: u128,
    }
    let X: Vec<u128> = Y.into_iter().map(|x| x.to_digit(10).unwrap() as u128).collect();
    let d = X.iter().max().unwrap() + 1;
    if X.len() == 1{
        if X[0] <= M{
            println!("1");
            return
        }else{
            println!("0");
            return
        }
    }
    let mut x:u128 = 0;
    for i in 0..X.len(){
        x = x*d + &X[i];
        if x > M{
            println!("0");
            return
        }
    }
    let mut l:u128 = d;
    let mut r:u128 = 10_u128.pow(18)+1;
    while r > l+1{
        let m = (l+r)/2;
        let mut ok = true;
        let mut x:u128 = 0;
        for i in 0..X.len(){
            x = x*m + X[i];
            if x > M{
                ok = false;
                break
            }
        }
        if ok{
            l = m;
        }else{
            r = m;
        }
    }
    println!("{}", l-d+1);
    
}
