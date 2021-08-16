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
        N: usize,
        mut L: [usize; N],
    }
    let mut ans = 0;
    L.sort();
    for i in 0..(N-2){
        for j in (i+1)..(N-1){
            for k in (j+1)..N{
                if L[k] < L[i] + L[j]{
                    ans += 1;
                }
            }
        }
    }
    
    println!("{}", ans);
}
