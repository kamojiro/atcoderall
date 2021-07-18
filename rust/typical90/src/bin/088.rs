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

#[fastout]
fn main() {
    input!{
        N: usize,
        Q: usize,
        A: [usize; N],
        XY: [(usize, usize); Q],
    }
    let Z = 8888;
    let mut edges = vec![vec![]; Z+1];
    for &(x,y) in &XY{
        edges[x].push(y)
    }
    let mut c = vec![0; N+1];
    let mut answer = vec![vec![]; Z+1];
    let mut flag = vec![false];
    let mut vec = Vec::new();
    dfs(N, &A, &edges, &mut answer, &mut c, &mut flag, &mut vec,1, 0);
    for i in 0..=Z{
        if answer[i].len() == 2{
            println!("{}", answer[i][0].len());
            for j in 0..answer[i][0].len(){
                print!("{} ", answer[i][0][j]);
            }
            println!();
            println!("{}", answer[i][1].len());
            for j in 0..answer[i][1].len(){
                print!("{} ", answer[i][1][j]);
            }
            println!();
            return;
        }
    }
    
    
}

fn dfs(N: usize, A: &Vec<usize>, edges: &Vec<Vec<usize>>, answer: &mut Vec<Vec<Vec<usize>>>, c: &mut Vec<usize>,flag: &mut Vec<bool>,vec: &mut Vec<usize>,  position: usize, depth: usize){
    if flag[0]{return}
    if position == N+1{
        answer[depth].push(vec.clone());
        if answer[depth].len() == 2{
            flag[0] = true;
        }
        return;
    }

    dfs(N, A, edges, answer, c, flag, vec, position+1, depth);

    if c[position] == 0{
        vec.push(position);
        for &i in &edges[position]{c[i] += 1;}
        dfs(N, A, edges, answer, c, flag, vec, position+1, depth+A[position-1]);
        for &i in &edges[position]{c[i] -= 1;}
        vec.pop();
    }
    
    
}

