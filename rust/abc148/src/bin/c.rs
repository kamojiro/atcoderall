// -*- coding:utf-8-unix -*-
#![allow(non_snake_case)]

use proconio::{fastout, input};

#[fastout]
fn main() {
    input!{
        A: usize,
        B: usize,
    }
    println!("{}", A*B/gcd(A,B))
}

use num_traits::PrimInt;
#[allow(dead_code)]
fn gcd<T>(a: T, b: T) -> T
where
    T: PrimInt,
{
    if a < b {
        return gcd(b, a);
    } else if b == T::zero() {
        return a;
    } else {
        return gcd(b, a % b);
    }
}
