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

use std::collections::BTreeSet;

use proconio::{fastout, input};
// use proconio::marker::Bytes;
// use proconio::marker::Usize1;

#[fastout]
fn main() {
    input!{
        L: usize,
        Q: usize,
        CX: [(usize, usize); Q],
    }
    let mut set = BTreeSet::new();
    set.insert(0);
    set.insert(L);
    for &(c,x) in &CX{
        if c == 1{
            set.insert(x);
        }else{
            let l = set.range(..x).next_back().unwrap();
            let r = set.range(x..).next().unwrap();
            println!("{}", *r-*l)
        }
    }
    
}
