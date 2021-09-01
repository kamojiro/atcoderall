// -*- coding:utf-8-unix -*-
#![allow(non_snake_case)]

use proconio::{fastout, input};
use superslice::Ext;

#[fastout]
fn main() {
    input!{
        N: usize,
        K: usize,
        A: [i64; N],
    }
    let mut plus = Vec::new();
    let mut zero = Vec::new();
    let mut minus = Vec::new();
    for &a in &A{
        if a == 0{
            zero.push(a)
        }else if a > 0{
            plus.push(a)
        }else{
            minus.push(-a)
        }
    }
    plus.sort();
    zero.sort();
    minus.sort();
    let mut l: i64 = -1_000_000_000_000_000_001;
    let mut r: i64 = 1_000_000_000_000_000_000;
    while r - l > 1{
        let m = if l+r >= 0{(l+r)/2}else{(l+r-1)/2};
        let count = get_count(m, &plus, &zero, &minus);
        if count < K{
            l = m
        }else{
            r = m
        }
    }
    println!("{}", r);
}

fn get_count(m: i64, plus: &Vec<i64>, zero: &Vec<i64>, minus: &Vec<i64>) -> usize{
    let mut count: usize = 0;
    let N = plus.len() + zero.len() + minus.len();
    if m >= 0{
        count += zero.len()*(N - zero.len());
        count += if zero.len() == 0{0}else{zero.len()*(zero.len() -1)/2};
        count += plus.len() * minus.len();
    }
    if m > 0{
        let mut ppcount = 0;
        for (i, &a) in plus.iter().enumerate(){
            let p = plus.upper_bound(&(m/a));
            ppcount += if i < p{p-1}else{p};
        }
        count += ppcount/2;
        let mut mmcount = 0;
        for (i, &a) in minus.iter().enumerate(){
            let p = minus.upper_bound(&(m/a));
            mmcount += if i < p{p-1}else{p};
        }
        count += mmcount/2;
    }
    if m < 0{
        let n = -m;
        for &a in plus{
            let p = minus.lower_bound(&((n+a-1)/a));
            count += minus.len()-p;
        }
    }
    count
}
