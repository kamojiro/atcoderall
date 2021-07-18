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

use std::cmp::max;
use std::io::Write;
use std::io::stdout;

fn solve(){
    let N = read::<usize>();
    if N == 1{
        println!("? 1");
        stdout().flush().unwrap();
        let a: i64 = read::<i64>();
        println!("! {}", a);
        stdout().flush().unwrap();
        return;
    }
    let mut A: Vec<i64> = vec![-1; N+1];
    let mut l = 0;
    let mut r = N;
    while r-l > 1{
        let m = (l+r)/2;
        if A[m] == -1{
            println!("? {}", m);
            stdout().flush().unwrap();
            A[m] = read::<i64>();
        }
        if A[m+1] == -1{
            println!("? {}", m+1);
            stdout().flush().unwrap();
            A[m+1] = read::<i64>();
        }
        if A[m] < A[m+1]{
            l = m;
        }else{
            r = m;
        }
    }
    println!("! {}", max(A[l], A[r]));
    stdout().flush().unwrap();
    return;
}

fn main() {
    let t = read::<usize>();
    for _ in 0..t{
        solve()
    }
}

fn read<T: std::str::FromStr>() -> T {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    s.trim().parse().ok().unwrap()
}
