// -*- coding:utf-8-unix -*-
#![allow(non_snake_case)]

use proconio::{fastout, input};
use proconio::marker::Bytes;

#[fastout]
fn main() {
    input!{
        N: usize,
        S: Bytes,
        T: Bytes,
    }
    let mut ans = Vec::new();
    for i in 0..N{
        ans.push(S[i]);
        ans.push(T[i]);
    }
    println!("{}", ans.iter().map(|&s| s as char).collect::<String>());
}
