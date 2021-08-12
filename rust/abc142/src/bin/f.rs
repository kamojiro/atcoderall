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

use proconio::marker::Usize1;
use proconio::{fastout, input};
// use proconio::marker::Bytes;
// use proconio::marker::Usize1;

#[fastout]
fn main() {
    input!{
        N: usize,
        M: usize,
        AB: [(Usize1, Usize1); M],
    }
    let mut edges = vec![vec![]; N];
    let mut reverse_edges = vec![vec![]; N];
    for &(a,b) in &AB{
        edges[a].push(b);
        reverse_edges[b].push(a);
    }
    let mut ans = vec![0; N+1];
    for v in 0..N{
        let cycle = minimal_cycle(v, &edges, &reverse_edges);
        if cycle.len() < ans.len(){
            ans = cycle;
        }
    }
    if ans.len() == N+1{
        println!("-1")
    }else{
        println!("{}", ans.len());
        for &c in &ans{
            println!("{}", c+1);
        }
    }
}

fn minimal_cycle(start: usize, edges: &Vec<Vec<usize>>, reverse_edges: &Vec<Vec<usize>>) -> Vec<usize>{
    let n = edges.len();
    let mut visited = vec![std::i64::MAX; n];
    let mut queue = VecDeque::new();
    queue.push_back(start);
    visited[start] = 0;
    let mut goal = n;
    while let Some(x) = queue.pop_front(){
        for &y in &edges[x]{
            if y == start{
                goal = x;
                break;
            }
            if visited[y] < std::i64::MAX{continue;}
            visited[y] = visited[y].min(visited[x]+1);
            queue.push_back(y);
        }
    }
    if goal == n{
        return vec![0; n+1]
    }
    let mut ret = Vec::new();
    let mut v = goal;
    for _ in 0..visited[goal]{
        ret.push(v);
        for &w in &reverse_edges[v]{
            if visited[v] == visited[w]+1{
                v = w;
                if v == start{
                    ret.push(start);
                    break
                }
                continue;
            }
        }
    }
    ret
}
