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

use std::collections::VecDeque;

use proconio::{fastout, input};
// use proconio::marker::Bytes;
use proconio::marker::Usize1;

#[fastout]
fn main() {
    input!{
        N: usize,
        M: usize,
    }
    let mut A = Vec::new();
    for _ in 0..M{
        input!{
            k: usize,
            a: [Usize1; k],
        }
        A.push(a.into_iter().collect::<VecDeque<usize>>());
    }
    let mut color = vec![vec![]; N];
    let mut queue = VecDeque::new();
    for i in 0..M{
        color[A[i][0]].push(i);
        if color[A[i][0]].len() == 2{
            queue.push_back(A[i][0])
        }
    }
    while let Some(x) = queue.pop_front(){
        let p = color[x][0];
        let q = color[x][1];
        A[p].pop_front();
        A[q].pop_front();
        if ! A[p].is_empty(){
            color[A[p][0]].push(p);
            if color[A[p][0]].len() == 2{
                queue.push_back(A[p][0])
            }

        }
        if ! A[q].is_empty(){
            color[A[q][0]].push(q);
            if color[A[q][0]].len() == 2{
                queue.push_back(A[q][0])
            }
        }
    }
    if A.iter().map(|a| a.len()).fold(0, |s,x| s+x) == 0{
        println!("Yes")
    }else{
        println!("No")
    }
    

}
