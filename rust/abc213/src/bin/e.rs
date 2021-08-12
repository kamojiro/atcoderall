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

use std::cmp::Reverse;
use std::collections::BinaryHeap;

use proconio::{fastout, input};
use proconio::marker::Bytes;
// use proconio::marker::Usize1;

#[fastout]
fn main() {
    input!{
        mut H: usize,
        mut W: usize,
        T: [Bytes; H],
    }
    let sx = 3;
    let sy = 3;
    let gx = H+2;
    let gy = W+2;
    let mut S = Vec::new();
    for _ in 0..3{
        S.push(vec![b'#'; W+6]);
    }
    for t in T.into_iter(){
        let mut s = vec![b'#'; 3];
        let mut z = t.clone();
        s.append(&mut z);
        let mut ss = vec![b'#'; 3];
        s.append(&mut ss);
        S.push(s);
    }
    for _ in 0..3{
        S.push(vec![b'#'; W+6]);
    }
    H += 6;
    W += 6;
    // for i in 0..H{
    //     println!("{:?}", S[i]);
    // }
    let mut queue = BinaryHeap::new();
    let mut ret = vec![vec![std::u64::MAX; W];H];
    queue.push((Reverse(0), sx, sy));
    // let destroy: Vec<(i64,i64)> = vec![(-2, -1), (-2, 0), (-1,-2), (0, -2), (1,-1), (1,0), (-1,1), (0,1)];
    while let Some((Reverse(cost), x, y)) = queue.pop(){
        if ret[x][y] < std::u64::MAX{
            continue;
        }
        
        ret[x][y] = cost;
        if x == gx && y == gy{break}
        if S[x-1][y] == b'.' && ret[x-1][y] == std::u64::MAX{
            queue.push((Reverse(cost), x-1,y))
        }
        if S[x+1][y] == b'.' && ret[x+1][y] == std::u64::MAX{
            queue.push((Reverse(cost), x+1,y))
        }
        if S[x][y-1] == b'.' && ret[x][y-1] == std::u64::MAX{
            queue.push((Reverse(cost), x,y-1))
        }
        if S[x][y+1] == b'.' && ret[x][y+1] == std::u64::MAX{
            queue.push((Reverse(cost), x,y+1))
        }
        for i in (x-2)..=(x+2){
            for j in (y-2)..=(y+2){
                if (i == x-2 || i == x+2) && (j == y-2 || j == y+2){
                    continue;
                }
                if 3 <= i && i < H-3 && 3 <= j && j < W-3{
                    if ret[i][j] == std::u64::MAX{
                        queue.push((Reverse(cost+1), i, j));
                    }
                }
                
            }                
        }
    }
    println!("{}", ret[gx][gy])
}
