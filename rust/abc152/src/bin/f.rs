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

use proconio::{fastout, input};
// use proconio::marker::Bytes;
use proconio::marker::Usize1;

#[fastout]
fn main() {
    input!{
        N: usize,
        AB: [(Usize1, Usize1); N-1],
        M: usize,
        UV: [(Usize1, Usize1); M],
    }
    let mut edges: Vec<Vec<usize>> = vec![vec![]; N];
    for &(a,b) in &AB{
        edges[a].push(b);
        edges[b].push(a);
    }
    let mut route: Vec<usize> = vec![0; M];
    for (j,&(u,v)) in UV.iter().enumerate(){
        let path = bfs(u, v, &edges);
        let mut cost = 0;
        for x in path{
            for (i,e) in AB.iter().enumerate(){
                if (x.0 == e.0 && x.1 == e.1) || (x.0 == e.1 && x.1 == e.0){
                    cost += 1 << i;
                    break
                }
            }
        }
        route[j] = cost;
    }
    let mut ans = 0;
    for p in 1usize..(1<<M){
        let mut e = 0;
        for i in 0..M{
            if p & (1 << i) > 0{
                e |= route[i];
            }
        }
        ans += 2i64.pow((N-1) as u32 - e.count_ones())*((p.count_ones() as i64)%2 *2 -1);
    }
    println!("{}", 2i64.pow((N-1) as u32) - ans);
}

fn bfs(s: usize, t: usize, edges: &Vec<Vec<usize>>) -> Vec<(usize,usize)>{
    let mut queue = std::collections::VecDeque::new();
    queue.push_back(s);
    let n = edges.len();
    let mut prev = vec![edges.len(); edges.len()];
    prev[s] = s;
    while let Some(v) = queue.pop_front(){
        if v == t{break}
        for &w in &edges[v]{
            if prev[w] == n{
                prev[w] = v;
                queue.push_back(w);
            }
        }
    }
    let mut ret = Vec::new();
    let mut r = t;
    while r != s{
        ret.push((r,prev[r]));
        r = prev[r];
    }
    ret
}
