#![allow(non_snake_case)]
use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    cost: i64,
    position: usize,
}

impl Ord for State {
    fn cmp(&self, other: &State) -> Ordering{
        other.cost.cmp(&self.cost)
    }
}


impl PartialOrd for State {
    fn partial_cmp(&self, other: &State) -> Option<Ordering>{
        Some(self.cmp(other))
    }
}

#[derive(Clone)]
struct Edge {
    node: usize,
    cost: i64,
}

fn dijkstra(adj_list: &Vec<Vec<Edge>>, start: usize) -> Vec<i64>{
    let mut dist: Vec<_> = (0..adj_list.len()).map(|_| i64::max_value()).collect();

    let mut heap = BinaryHeap::new();

    dist[start] = 0;
    heap.push(State {
        cost: 0,
        position: start,
    });

    while let Some(State {cost, position}) = heap.pop() {
        if cost > dist[position]{
            continue;
        }
        for edge in &adj_list[position] {
            let next = State{
                cost: cost + edge.cost,
                position: edge.node,
            };
            if next.cost < dist[next.position]{
                heap.push(next);
                dist[next.position] = next.cost;
            }
        }
    }

    dist
        
}


fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    
}

pub struct Scanner<R> {
    stdin: R,
}

impl<R: std::io::Read> Scanner<R> {
    pub fn read<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        let buf = self
            .stdin
            .by_ref()
            .bytes()
            .map(|b| b.unwrap())
            .skip_while(|&b| b == b' ' || b == b'\n')
            .take_while(|&b| b != b' ' && b != b'\n')
            .collect::<Vec<_>>();
        unsafe { std::str::from_utf8_unchecked(&buf) }
        .parse()
            .ok()
            .expect("Parse error.")
    }
    pub fn vec<T: std::str::FromStr>(&mut self, n: usize) -> Vec<T> {
        (0..n).map(|_| self.read()).collect()
    }
    pub fn chars(&mut self) -> Vec<char> {
        self.read::<String>().chars().collect()
    }
}


