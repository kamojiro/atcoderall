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
    if N <= 5{
        let mut ans = -1;
        for i in 1..=N{
            println!("? {}",i);
            stdout().flush().unwrap();
            ans = ans.max(read::<i64>());
        }
        println!("! {}", ans);
        stdout().flush().unwrap();
        return;
    }
    let mut A: Vec<i64> = vec![-1; N+2];
    let mut l = 0;
    let mut r = N+1;
    let s = 382;
    let t = 618;
    let mut a = l + (r-l)*s/1000;
    let mut b = l + (r-l)*t/1000;
    loop{
        if A[a] == -1{
            println!("? {}", a);
            stdout().flush().unwrap();
            A[a] = read::<i64>();
        }
        if A[b] == -1{
            println!("? {}", b);
            stdout().flush().unwrap();
            A[b] = read::<i64>();
        }
        if r - l <= 3{
            let ans = max(max(A[a], A[b]), max(A[l], A[r]));
            println!("! {}", ans);
            stdout().flush().unwrap();
            return;
        }
        if A[a] == A[b]{
            l = a;
            r = b;
            a = l + (r-l)*s/1000;
            b = l + (r-l)*t/1000;
            if l == a{
                a = l+1;
            }
            if r == b{
                if r > 0{
                    b = r-1
                }
            }
            if a > b{
                let t = a;
                a = b;
                b = t;
            }
        }else if A[a] < A[b]{
            l = a;
            a = b;
            b = l + (r-l)*t/1000;
            if b == a{
                b = a+1;
            }
        }
        else{
            r = b;
            b = a;
            a = l + (r-l)*s/1000;
            if a == b{
                if b >= 2{
                    a = b-1;
                }
            }
        }
        if a == 0{
            a = 1
        }
        if b == N+1{
            b = N;
        }
    }
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
