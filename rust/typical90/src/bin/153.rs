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

use std::io::Write;
use std::io::stdout;

fn solve(){
    let N = read::<usize>();
    let mut A = vec![0;N];
    for i in 0..N{
        println!("? {}", i+1);
        stdout().flush().unwrap();
        A[i] = read::<i64>();
    }
    println!("! {}", A.iter().max().unwrap());
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
