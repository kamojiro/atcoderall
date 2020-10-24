#![allow(non_snake_case)]

use std::collections::BinaryHeap;

use proconio::{input, fastout};

#[fastout]
fn main() {
    input!{
        N: usize,
        K: usize,
        X: [usize; N],
        //array: [(usize,usize);N],
    }
    let mut heapq = BinaryHeap::new();
    for i in 0..K{
        heapq.push((X[i],i+1));
    }
    let mut ANS = Vec::new();
    ANS.push(heapq.peek().unwrap().1);
    for i in K..N{
        let x = X[i];
        if x < heapq.peek().unwrap().0{
            heapq.pop();
            heapq.push((x,i+1));
        }
        ANS.push(heapq.peek().unwrap().1);
    }
    for ans in ANS{
        println!("{}", ans);
    }
}
