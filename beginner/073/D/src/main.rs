#![allow(non_snake_case)]

//use itertools::Itertools as _;
use permutohedron::LexicalPermutation as _;
use num::traits::One; // One is an unit for multipolication
use petgraph::graph::{IndexType, NodeIndex, UnGraph};
use proconio::input;
use proconio::source::{Readable, Source};

// use std::collections::HashMap;
use std::io::BufRead;
use std::marker::PhantomData;
use std::ops::Sub;

fn main() {
    input! {
        _: usize,
        m: usize,
        r: usize,
        rs: [NodeIndex1<u32>; r],
        abcs: [(NodeIndex1<u32>, NodeIndex1<u32>,u32);m],
    }
    // for abc in abcs{
    //     let (a,b,c) = abc;
    //     println!("{} {} {}", a.index(),b.index(),c);
    // }
    let graph = UnGraph::<(),u32>::from_edges(&abcs);
    let mut towns: Vec<Vec<u32>> = vec![vec![0;r];r];
    for i in 0..r{
        let dijkstra = petgraph::algo::dijkstra(&graph, rs[i], None, |e| *e.weight());
        for j in 0..r{
            towns[i][j] = dijkstra[&rs[j]];
        }
    }
    // for &s in &rs{
    //     let dijkstra = petgraph::algo::dijkstra(&graph, s, None, |e| *e.weight());
    //     for &t in &rs{
    //         towns[s.index()][t.index()] = dijkstra[&t];
    //     }
    // }
    let mut ans:u32 = 1000000000;
    // if m == 1{
    //     ans = 0;
    // }
    let mut values:Vec<usize> = (0..r).collect();
    loop {
        let mut temp_ans: u32 = 0;
        for i in 0..(r-1){
            temp_ans += towns[values[i]][values[i+1]];
        }
        if temp_ans < ans{
            ans = temp_ans;
        }
        if !values.next_permutation() {
            break
        }
    }
    println!("{}", ans);
}


struct NodeIndex1<Ix>(PhantomData<fn() -> Ix>);
// Ix型

impl<Ix: IndexType + Readable<Output = Ix> + One + Sub<Output = Ix>> Readable for NodeIndex1<Ix> {
    // input!でR読み込むには、eadable traitを実装する必要がある
    // https://docs.rs/proconio/0.3.4/proconio/source/trait.Readable.html
    type Output = NodeIndex<Ix>;

    fn read<R: BufRead, S: Source<R>>(source: &mut S) -> NodeIndex<Ix> {
        NodeIndex::from(Ix::read(source) - Ix::one())
    }
}
