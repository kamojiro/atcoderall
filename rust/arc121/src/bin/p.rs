// -*- coding:utf-8-unix -*-
#![allow(non_snake_case)]

use proconio::{input};

// #[fastout]
fn main() {
    input!{
        N: usize,
        A: [i128;N],
    }
    println!("{:?}", A);
    // for i in (0..N).map(|x| x*2){
    //     println!("{} {}",i, nearest_distance(&A, i as i128) );
    // }
    println!("0 {}", nearest_distance(&A, 0 as i128) );
    
}


fn nearest_distance(A: &Vec<i128>, a: i128)-> i128 {
    let N = A.len();
    if A[N-1] <= a{return (a - A[N-1]).abs()}
    if a <= A[0]{return (a - A[0]).abs()}
    let mut l = 0;
    let mut r = N;
    while r - l > 1{
        let m = (l+r)/2;
        if A[m] < a{
            l = m
        }else{
            r = m
        }
        println!("{} {}",l ,r );
    }
    println!("{} a:{}", l, a);
    let mut ret = (a - A[l]).abs();
    if l+1 < N{
        ret = std::cmp::min(ret, (a - A[l+1]).abs());
    }
    if l > 0{
        ret = std::cmp::min(ret, (a - A[l-1]).abs());
    }
    ret
}
