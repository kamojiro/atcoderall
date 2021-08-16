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
use proconio::marker::Usize1;
use superslice::Ext;

#[fastout]
fn main() {
    input!{
        N: usize,
        A: [Usize1;N],
    }
    let mut C = vec![0;N];
    for &a in &A{
        C[a] += 1;
    }
    C.sort();
    let mut accC = vec![0; N+1];
    (0..N).for_each(|x| accC[x+1] = accC[x] + C[x]);
    let mut length = vec![0; N+1];
    for i in 1..=N{
        let x = C.lower_bound(&i);
        length[i] = (accC[x] + i*(N-x))/i;
    }
    let mut index = N;
    for i in 1..=N{
        while length[index] < i && index >= 1{
            index -= 1;
        }
        println!("{}", index);
    }

    
}
