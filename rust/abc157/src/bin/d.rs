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

use std::collections::HashSet;

use proconio::{fastout, input};
// use proconio::marker::Bytes;
use proconio::marker::Usize1;
use petgraph::unionfind::UnionFind;

#[fastout]
fn main() {
    input!{
        N: usize,
        M: usize,
        K: usize,
        AB: [(Usize1,Usize1);M],
        CD: [(Usize1,Usize1);K],
    }
    let mut neighbor = HashSet::new();
    let mut count = vec![0;N];
    let mut tree = UnionFind::new(N);
    let mut weight = vec![1;N];
    for &(a,b) in &AB{
        neighbor.insert((a,b));
        neighbor.insert((b,a));
        count[a] += 1;
        count[b] += 1;
        if tree.equiv(a, b){continue;}
        let w = weight[tree.find(a)] + weight[tree.find(b)];
        tree.union(a, b);
        weight[tree.find(a)] = w;
    }
    let mut ans = vec![0;N];
    for i in 0..N{
        ans[i] = weight[tree.find(i)]
    }
    for i in 0..N{
        ans[i] -= count[i];
    }
    for &(c,d) in &CD{
        if neighbor.contains(&(c,d)){continue;}
        if tree.equiv(c, d){
            ans[c] -= 1;
            ans[d] -= 1;
        }
    }
    for &a in &ans{
        print!("{} ", a-1)
    }
    println!()
        
}
