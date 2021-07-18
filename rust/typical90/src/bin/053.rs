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
    let mut A: Vec<i64> = vec![-1; N+1];
    let Z = 1598;
    for i in (N+1)..=Z{
        A.push(-(i as i64));
    }
    if N <= 5{
        let mut ans = -1;
        for i in 1..=N{
            ans = ans.max(ask(i, &mut A));
        }
        println!("! {}", ans);
        stdout().flush().unwrap();
        return;
    }
    let f: usize = 1000_000_000_000_0;
    let g: i64 = -1;
    let fibonacci = vec![1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597];
    let mut ans = 0;
    let mut cl = 0;
    let mut cr = 1597;
    let mut dl = 610;
    let mut dr = 987;
    let mut el = ask(dl, &mut A);
    let mut er = ask(dr, &mut A);
    ans = ans.max(el).max(er);
    if el < er{
        cl = dl;
        dl = dr;
        dr = f;
        el = er;
        er = g;
    }else{
        cr = dr;
        dr = dl;
        dl = f;
        er = el;
        el = g;
    }
    for i in (0..=12).rev(){
        if dl == f{
            dl = cl + fibonacci[i];
            el = ask(dl, &mut A)
        }else if dr == f{
            dr = cr - fibonacci[i];
            er = ask(dr, &mut A)
        }
        ans = ans.max(el).max(er);
        if el < er{
            cl = dl;
            dl = dr;
            dr = f;
            el = er;
            er = g;
        }else{
            cr = dr;
            dr = dl;
            dl = f;
            er = el;
            el = g;
        }
    }
    for &a in &A{
        ans = ans.max(a);
    }
    println!("! {}", ans);
        
    
}

fn ask(i: usize, A: &mut Vec<i64>) -> i64{
    if A[i] == -1{
        println!("? {}",i);
        stdout().flush().unwrap();
        A[i] = read::<i64>();
    }
    A[i]
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
