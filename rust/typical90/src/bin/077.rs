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

use std::collections::HashMap;

use proconio::{fastout, input};
// use proconio::marker::Bytes;

#[fastout]
fn main() {
    input!{
        N: usize,
        T: i64,
        AXAY: [(i64,i64);N],
        BXBY: [(i64,i64);N],
    }
    let mut dinic = Dinic::new(N*2+2);
    // AXAY: 0~N-1
    // BXBY: N~N*2-1
    // s: N*2
    // t: N*2+1
    for i in 0..N{
        dinic.add_edge(N*2, i, 1);
        dinic.add_edge(N+i, N*2+1, 1);
    }
    let dxdy = vec![(1,0), (1,1), (0,1), (-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)];
    let mut hashmap: HashMap<(i64,i64), Vec<_>> = HashMap::new();
    for (i, &a) in AXAY.iter().enumerate(){
        for &(dx,dy) in &dxdy{
            let p = a.0+dx*T;
            let q = a.1+dy*T;
            if hashmap.contains_key(&(p,q)){
                hashmap.get_mut(&(p,q)).unwrap().push(i);
            }else{
                hashmap.insert((p,q), vec![i]);
            }

        }
    }
    for (j, b) in BXBY.iter().enumerate(){
        if let Some(neighbor) = hashmap.get(b){
            for &i in neighbor{
                dinic.add_edge(i, j+N, 1);
            }
        }else{
            println!("No");
            return;
        }
    }
    if dinic.max_flow(N*2, N*2+1) < (N as u64){
        println!("No");
        return;
    }
    // dinic.ans(N, &AXAY, &BXBY);
    let edges = dinic.get_edges();
    let mut ans = Vec::new();
    for i in 0..N{
        let p = AXAY[i];
        for &(v, cap, _) in &edges[i]{
            if v >= N*2{continue;}
            if cap == 0{
                let q = BXBY[v-N];
                if p.0 == q.0{
                    if p.1 < q.1{
                        ans.push(3)
                    }else{
                        ans.push(7)
                    }
                }else if p.1 == q.1{
                    if p.0 < q.0{
                        ans.push(1)
                    }else{
                        ans.push(5)
                    }
                }else if p.0 + p.1 == q.0 + q.1{
                    if p.0 < q.0{
                        ans.push(8)
                    }else{
                        ans.push(4)
                    }
                }else{
                    if p.0 < q.0{
                        ans.push(2)
                    }else{
                        ans.push(6)
                    }
                }
                break
            }
        }
    }
    println!("Yes");
    for a in ans{
        print!("{} ", a);
    }
    println!("");
}

// fn on_same_square(p: (i64, i64), q: (i64, i64), T: i64) -> bool{
//     if p.0 == q.0{
//         if (p.1 - q.1).abs() == T{
//             return true
//         }
//     }
//     if p.1 == q.1{
//         if (p.0 - q.0).abs() == T{
//             return true
//         }
//     }
//     if p.0 + p.1 == q.0 + q.1{
//         if (p.0 - q.0).abs() == T{
//             return true
//         }
//     }
//     if p.0 - p.1 == q.0 - q.1{
//         if (p.0 - q.0).abs() == T{
//             return true
//         }
//     }
//     false
// }

#[derive(Clone, Debug)]
struct Dinic {
    // to, cap, rev
    edges: Vec<Vec<(usize, u64, usize)>>,
    level: Vec<usize>,
}
 
impl Dinic
{
    fn new(n: usize) -> Self {
        let edges: Vec<Vec<(usize, u64, usize)>> = vec![vec![];n];
        let level = vec![n;n];
        let this = Self {
            edges,
            level,
        };
        return this;
    }
 
    fn add_edge(&mut self, from: usize, to: usize, cap: u64){
        let from_to_rev = self.edges[to].len() + if from == to {1} else {0};
        self.edges[from].push((to, cap, from_to_rev));
        let to_from_rev = self.edges[from].len()-1;
        self.edges[to].push((from, 0, to_from_rev));
    }

    fn get_edges(&self) -> Vec<Vec<(usize, u64, usize)>>{
        self.edges.clone()
    }
 
    fn bfs(&mut self, start: usize, goal: usize){
        let n = self.edges.len();
        (0..n).for_each(|i| self.level[i] = n);
        // self.level = std::iter::repeat(n).take(n).collect();
        let mut deque = std::collections::VecDeque::new();
        deque.push_back(start);
        self.level[start] = 0;
        while let Some(v) = deque.pop_front(){
            for (to, cap, _) in self.edges.get(v).unwrap(){
                if (self.level[*to] == n) && (*cap > 0){
                    self.level[*to] = self.level[v]+1;
                    if *to == goal{return}
                    deque.push_back(*to);
                }
            }
        }
    }
 
    fn dfs(&mut self, v: usize, t: usize, f: u64) -> u64{
        if v == t{ return f;}
        let n = self.edges.len();
        let mut res = 0;
        for i in 0..self.edges[v].len(){
            let (to, cap, rev) = self.edges[v][i];
            if cap > 0 && self.level[v] < self.level[to] && self.level[to] < n{
                let d = self.dfs(to, t, (f-res).min(cap));
                if d > 0{
                    self.edges[v][i].1 = cap - d;
                    self.edges[to][rev].1 += d;
                    res += d;
                    if res == f{return res}
                }
             }
        }
        self.level[v] = n;
        res
    }
 
    fn max_flow(&mut self, start: usize, goal: usize) -> u64{
        let n = self.edges.len();
        let mut flow = 0;
        loop {
            self.bfs(start, goal);
            if self.level[goal] == n{break}
            loop{
                let f = self.dfs(start, goal, std::u64::MAX);
                if f == 0{break}
                flow += f
            }
        }
        flow
    }

    // fn ans(&self, N: usize, AXAY: &Vec<(i64,i64)>, BXBY: &Vec<(i64,i64)> ){
    //     let mut ans = Vec::new();        
    //     for i in 0..N{
    //         let p = AXAY[i];
    //         for &(v, cap, _) in &self.edges[i]{
    //             if v >= N*2{continue;}
    //             if cap == 0{
    //                 let q = BXBY[v-N];
    //                 if p.0 == q.0{
    //                     if p.1 < q.1{
    //                         ans.push(3)
    //                     }else{
    //                         ans.push(7)
    //                     }
    //                 }else if p.1 == q.1{
    //                     if p.0 < q.0{
    //                         ans.push(1)
    //                     }else{
    //                         ans.push(5)
    //                     }
    //                 }else if p.0 + p.1 == q.0 + q.1{
    //                     if p.0 < q.0{
    //                         ans.push(8)
    //                     }else{
    //                         ans.push(4)
    //                     }
    //                 }else{
    //                     if p.0 < q.0{
    //                         ans.push(2)
    //                     }else{
    //                         ans.push(6)
    //                     }
    //                 }
    //                 break
    //             }
    //         }
    //     }
    //     println!("Yes");
    //     for a in ans{
    //         print!("{} ", a);
    //     }
    //     println!("");
    // }
}
