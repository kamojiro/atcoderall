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

#[fastout]
fn main() {
    input!{
        N: usize,
        P: u64,
        Q: u64,
        A: [u64;N],
    }
    // let ans = (0..N).combinations(5).map(|v| (0..5).map(|i| A[v[i]]).fold(1, |sum,x| sum*x%P)).filter(|&x| x == Q).count();
    // let mut ans = 0;
    // for v in (0..N).combinations(5){
    //     if (0..5).map(|i| A[v[i]]).fold(1, |sum,x| sum*x%P) == Q{
    //         ans += 1;
    //     }
    // }
    // これが一番速い
    let mut ans = 0;
    for i in 0..(N-4){
        for j in (i+1)..(N-3){
            for k in (j+1)..(N-2){
                for l in (k+1)..(N-1){
                    for m in (l+1)..N{
                        if A[i]*A[j]%P*A[k]%P*A[l]%P*A[m]%P == Q{
                            ans += 1;
                        }
                    }
                }
            }
        }
    }
    println!("{}", ans);
}
