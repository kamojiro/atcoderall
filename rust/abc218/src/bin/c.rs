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
use proconio::marker::Bytes;
// use proconio::marker::Usize1;

#[fastout]
fn main() {
    input!{
        N: usize,
        S: [Bytes; N],
        T: [Bytes; N],
    }
    let mut SS = S.clone();
    for _ in 0..4{
        if check(&SS, &T){
            println!("Yes");
            return;
        }
        let T = rotate(&SS);
        SS = T.clone();
    }
    println!("No")
}

fn check(S: &Vec<Vec<u8>>, T: &Vec<Vec<u8>>) -> bool{
    let n = S.len();
    for t in 0..n{
        // eprintln!("{}", t);
        if jcheck(t, S, T){
            return true
        }
        if jcheck(t, T, S){
            return true
        }

    }
    false
}

fn jcheck(t: usize, S: &Vec<Vec<u8>>, T: &Vec<Vec<u8>>) -> bool{
    let n = S.len();
    'kkk: for k in 0..n{
        for i in 0..(n+k){
            for j in 0..(n+t){
                if k <= i && i < n && t <= j && j < n{
                    // eprintln!("st {} {}", i, j);
                    if S[i][j] != T[i-k][j-t]{
                        continue 'kkk;
                    }
                }else if i < n && j < n{
                    // eprintln!("s {} {}", i, j);
                    if S[i][j] == b'#'{
                        continue 'kkk;
                    }
                }else if k <= i && t <= j{
                    // eprintln!("t {} {}", i, j);
                    if T[i-k][j-t] == b'#'{
                        continue 'kkk;
                    }
                }
            }
        }
        return true
    }
    false
}

fn rotate(S: &Vec<Vec<u8>>) -> Vec<Vec<u8>>{
    let n = S.len();
    let mut ret = vec![vec![b'.'; n]; n];
    for i in 0..n{
        for j in 0..n{
            ret[i][j] = S[n-1-j][i]
        }
    }
    ret
}
