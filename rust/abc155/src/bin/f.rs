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
use superslice::Ext;
use petgraph::unionfind::UnionFind;
// use proconio::marker::Bytes;
// use proconio::marker::Usize1;

#[fastout]
fn main() {
    input!{
        N: usize,
        M: usize,
        mut AB: [(usize,usize); N],
        LR: [(usize,usize); M],
    }
    AB.sort_by_key(|x| x.0);
    let mut vertex = vec![0; N+1];
    for (i, &(_,b)) in AB.iter().enumerate(){
        vertex[i+1] = b;
    }
    AB.push((1_000_000_001, 0));

    let mut tree = UnionFind::new(N+1);
    let mut edges = vec![vec![]; N+1];
    for (i, &(l,r)) in LR.iter().enumerate(){
        let p = AB.lower_bound_by_key(&l, |x| x.0);
        let q = AB.lower_bound_by_key(&(r+1), |x| x.0);
        if !tree.equiv(p, q){
            tree.union(p, q);
            edges[p].push((q, i+1));
            edges[q].push((p, i+1));
        }
    }
    for i in 0..N{
        vertex[i] ^= vertex[i+1];
    }
    let mut ans = Vec::new();
    for i in 0..N+1{
        if tree.find(i) != i{continue;}
        dfs(&edges, &mut vertex, i, i, &mut ans);
        if vertex[i] == 1{
            println!("-1");
            return;
        }
    }
    ans.sort();
    println!("{}", ans.len());
    for &a in &ans{
        print!("{} ", a)
    }
    println!()


}

fn dfs(edges: &Vec<Vec<(usize,usize)>>, vertex: &mut Vec<usize>, v: usize, prev: usize, ans: &mut Vec<usize>){
    for &(w,i) in &edges[v]{
        if w == prev{continue;}
        dfs(edges, vertex, w, v, ans);
        if vertex[w] == 1{
            ans.push(i);
            vertex[w] ^= 1;
            vertex[v] ^= 1;
        }
    }
}

// fn compress_coordinate(coordinate: &Vec<usize>) -> HashMap<usize,usize>{
//     let set: HashSet<_> = coordinate.iter().collect();
//     let sorted = set.into_iter().sorted();
//     let mut ret = HashMap::new();
//     for (i, &x) in sorted.into_iter().enumerate(){
//         ret.insert(x, i);
//     }
//     ret
// }
