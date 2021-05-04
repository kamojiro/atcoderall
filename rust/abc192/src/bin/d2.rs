#![allow(non_snake_case)]
use proconio::{input, fastout};
use proconio::marker::{Chars};

#[fastout]
fn main() {
    input!{
        Y: Chars,
        M: u64,
    }
    let X: Vec<u64> = Y.into_iter().map(|x| x.to_digit(10).unwrap() as u64).collect();
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
    let mut x:u64 = 0;
    for i in 0..X.len(){
        let (y, p) = x.overflowing_mul(d);
        // println!("{} {} {} {}",x,m,y,p );
        if !p{
            x = y;
        }else{
            println!("0");
            return
            }
        let (y, p) = x.overflowing_add(X[i]);
        if !p{
            x = y;
        }else{
            println!("0");
            return
        }
        if x > M{
            println!("0");
            return
        }
    }
    let mut l:u64 = d;
    let mut r:u64 = 10_u64.pow(18)+1;
    while r > l+1{
        let m = (l+r)/2;
        let mut ok = true;
        let mut x:u64 = 0;
        for i in 0..X.len(){
            let (y, p) = x.overflowing_mul(m);
            // println!("{} {} {} {}",x,m,y,p );
            if !p{
                x = y;
            }else{
                ok = false;
                break
            }
            let (y, p) = x.overflowing_add(X[i]);
            if !p{
                x = y;
            }else{
                ok = false;
                break
            }
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
