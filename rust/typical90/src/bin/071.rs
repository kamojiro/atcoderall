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
        M: usize,
        K: usize,
        AB: [(usize, usize);M],
    }

    let mut edges = vec![vec![];N];
    let mut sink = vec![vec![0;N];1];
    for &(a,b) in &AB{
        edges[a-1].push(b-1);
        sink[0][b-1] += 1;
    }

    let mut stack = vec![vec![];1];
    let mut order = vec![vec![N;N];1];
    for i in 0..N{
        if sink[0][i] == 0{
            stack[0].push(i);
        }
    }
    let mut start = vec![0;K];
    for k in 0..K{
        if stack.len()-1 < k{
            println!("-1");
            return;
        }
        for i in start[k]..N{
            if stack[k].len() == 0{
                println!("-1");
                return;
            }
            if stack.len() < K && stack[k].len() > 1{
                for j in 0..(stack[k].len()-1){
                    let v = stack[k][j];
                    stack.push(stack[k].clone());
                    order.push(order[k].clone());
                    sink.push(sink[k].clone());
                    let L = stack.len()-1;
                    stack[L].remove(j);
                    order[L][v] = i;
                    start[L] = i+1;
                    for &w in &edges[v]{
                        sink[L][w] -= 1;
                        if sink[L][w] == 0{
                            stack[L].push(w);
                        }
                    }
                    if stack.len() >= K{break;}
                }
            }
            let v = stack[k].pop().unwrap();
            order[k][v] = i;
            for &w in &edges[v]{
                sink[k][w] -= 1;
                if sink[k][w] == 0{
                    stack[k].push(w);
                }
            }
        }
    }
    let mut ans = vec![vec![0;N];K];
    for i in 0..K{
        for j in 0..N{
            ans[i][order[i][j]] = j+1;
        }
    }
    for i in 0..K{
        for j in 0..N{
            print!("{} ", ans[i][j]);
        }
        println!();
    }
}
