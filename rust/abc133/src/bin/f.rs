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

use std::collections::{HashMap, HashSet};

use proconio::{fastout, input};
// use proconio::marker::Bytes;

#[fastout]
fn main() {
    input!{
        N: usize,
        Q: usize,
        ABCD: [(usize,usize,usize,usize); N-1],
        XYUV: [(usize,usize,usize,usize); Q],
    }
    let mut edges = vec![vec![];N];
    let mut full_edges = vec![vec![]; N];
    let mut color_distance = HashMap::new();
    for &(a,b,c,d) in &ABCD{
        edges[a-1].push(b-1);
        edges[b-1].push(a-1);
        full_edges[a-1].push((b-1, c, d));
        full_edges[b-1].push((a-1, c, d));
        color_distance.insert((a-1,b-1), (c,d));
        color_distance.insert((b-1,a-1), (c,d));
    }
    let mut dist = vec![0; N];
    let mut visited = vec![false; N];
    visited[0] = true;
    let mut queue = vec![0];
    while let Some(v) = queue.pop(){
        for &(w,_,d) in &full_edges[v]{
            if !visited[w]{
                visited[w] = true;
                dist[w] = dist[v]+d;
                queue.push(w);
            }
        }
    }
    let lca = LowestCommonAncestor::new(N, 0, &edges);
    let mut read_ahead = vec![HashSet::new(); N];
    for &(x,_,u,v) in &XYUV{
        let w = lca.query(u-1, v-1);
        read_ahead[w].insert(x);
        read_ahead[u-1].insert(x);
        read_ahead[v-1].insert(x);
    }
    let mut num: Vec<HashMap<usize, usize>> = vec![HashMap::new(); N];
    let mut sum = vec![HashMap::new(); N];
    let euler_tour = Tree::new(&edges).get_euler_tour(0);
    let mut color_num: Vec<usize> = vec![0; N];
    let mut color_sum: Vec<usize> = vec![0; N];
    let mut visited = vec![false; N];
    for &(v,w,t) in &euler_tour{
        let &(c,d) = color_distance.get(&(v,w)).unwrap();
        if t{
            color_num[c] += 1;
            color_sum[c] += d;
        }else{
            color_num[c] -= 1;
            color_sum[c] -= d;
        }
        if !visited[w]{
            visited[w] = true;
            for key in read_ahead[w].iter(){
                num[w].insert(*key, *color_num.get(*key).unwrap());
                sum[w].insert(*key, *color_sum.get(*key).unwrap());
            }
        }
    }
    let mut ans = Vec::new();
    for &(x,y,u,v) in &XYUV{
        let w = lca.query(u-1, v-1);
        let distu = dist[u-1] - sum[u-1].get(&x).unwrap() + num[u-1].get(&x).unwrap()*y;
        let distv = dist[v-1] - sum[v-1].get(&x).unwrap() + num[v-1].get(&x).unwrap()*y;
        let distw = dist[w] - sum[w].get(&x).unwrap() + num[w].get(&x).unwrap()*y;
        ans.push(distu + distv - distw*2);
    }
    for a in ans.iter(){
        println!("{}", a);
    }

}

#[derive(Clone, Debug)]
struct Tree{
    edges: Vec<Vec<usize>>,
}

#[allow(dead_code)]
impl Tree
{
    fn new(edges: &Vec<Vec<usize>>) -> Self {
        let edges = edges.clone();
        let this = Self {
            edges,
        };
        return this;
    }

    fn get_euler_tour(&mut self, root: usize) -> Vec<(usize, usize, bool)>{
        let mut route = Vec::new();
        let mut visited = vec![false;self.edges.len()];
        visited[root] = true;
        self.dfs(root, &mut visited, &mut route);
        route
    }


    fn dfs(&self, v: usize, visited: &mut Vec<bool>, route: &mut Vec<(usize,usize, bool)>){
        for &w in &self.edges[v]{
            if !visited[w]{
                visited[w] = true;
                route.push((v,w,true));
                self.dfs(w, visited, route);
                route.push((w,v,false));
            }
        }
    }
    
}



#[derive(Clone, Debug)]
struct LowestCommonAncestor{
    root: usize,
    depth: Vec<usize>,
    log_n: usize,
    ancestor: Vec<Vec<usize>>,
}
 
#[allow(dead_code)]
impl LowestCommonAncestor
{
    fn new(n: usize,root: usize, edges: &Vec<Vec<usize>>) -> Self {
        let mut log_n = 1;
        while (1 << log_n) < n {log_n += 1}
        let mut ancestor = vec![vec![n;log_n]; n];
        let mut stack = vec![root];
        let mut depth = vec![n; n];
        depth[root] = 0;
        while let Some(v) = stack.pop(){
            for &w in &edges[v]{
                if depth[w] == n{
                    depth[w] = depth[v] + 1;
                    ancestor[w][0] = v;
                    stack.push(w);
                }
            }
        }
        for k in 0..(log_n-1){
            for v in 0..n{
                if ancestor[v][k] == n{
                    ancestor[v][k+1] = n;
                }else{
                    ancestor[v][k+1] = ancestor[ancestor[v][k]][k];
                }
            }
        }
        let this = Self {
            root,
            depth,
            log_n,
            ancestor,
        };
        return this;
    }
 
    fn query(&self, vv: usize, ww: usize) -> usize {
        let mut v = vv;
        let mut w = ww;
        if self.depth[v] > self.depth[w]{
            std::mem::swap(&mut v, &mut w);            
        }
        for k in 0..self.log_n{
            if ((self.depth[w] - self.depth[v])>>k) & 1 == 1{
                w = self.ancestor[w][k];
            }
        }
        if v == w{
            return v
        }
        for k in (0..self.log_n).rev(){
            if self.ancestor[v][k] != self.ancestor[w][k]{
                v = self.ancestor[v][k];
                w = self.ancestor[w][k];
            }
        }
        self.ancestor[v][0]
    }
 
    fn distance(&self, v: usize, w: usize) -> usize{
        let common = self.query(v,w);
        self.depth[v] + self.depth[w] - self.depth[common]*2
    }
    
}
