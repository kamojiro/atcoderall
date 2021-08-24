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

use itertools::Itertools;
use permutohedron::LexicalPermutation;
use proconio::{fastout, input};
// use proconio::marker::Bytes;
// use proconio::marker::Usize1;

#[fastout]
fn main() {
    input!{
        N: usize,
        P: [usize;N],
        Q: [usize;N],
    }
    let mut data = (1..=N).collect_vec();
    let mut p = 0;
    let mut q = 0;
    let mut count = 0;
    loop{
        let mut t = true;
        for i in 0..N{
            if data[i] != P[i]{
                t = false
            }
        }
        if t{p = count}
        let mut t = true;
        for i in 0..N{
            if data[i] != Q[i]{
                t = false
            }
        }
        if t{q = count}

        if !data.next_permutation(){break}
        count += 1;
    }
    println!("{}", ((p as i64) - (q as i64)).abs())
}
