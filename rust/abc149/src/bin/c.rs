// -*- coding:utf-8-unix -*-
#![allow(non_snake_case)]

#[cfg(debug_assertions)]
#[allow(unused)]
macro_rules! eprintln {
    ($p:tt, $($x:expr),*) => {
        std::eprintln!($p, $($x,)*);
    };
}

#[cfg(not(debug_assertions))]
#[allow(unused)]
macro_rules! eprintln {
    ($p:tt, $($x:expr),*) => {};
}

use proconio::{fastout, input};
// use proconio::marker::Bytes;
// use proconio::marker::Usize1;

#[fastout]
fn main() {
    input!{
        mut X: usize,
    }
    loop{
        if is_prime(X){
            println!("{}", X);
            return;
        }
        X += 1;
    }
}

fn is_prime(x: usize) -> bool{
    if x == 1{return false}
    let mut n = 2;
    while n*n <= x{
        if x%n == 0{
            return false;
        }
        n += 1;
    }
    true
}
