#![allow(non_snake_case)]
use std::collections::{VecDeque};

// #[derive(Copy, Clone, Eq, PartialEq)]
// struct State {
//     cost: i64,
//     position: usize,
// }

// impl Ord for State {
//     fn cmp(&self, other: &State) -> Ordering{
//         other.cost.cmp(&self.cost)
//     }
// }


// impl PartialOrd for State {
//     fn partial_cmp(&self, other: &State) -> Option<Ordering>{
//         Some(self.cmp(other))
//     }
// }


fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let mut edge: Vec< Vec< usize>> = vec![ vec![]; N+1];
    let mut bedge: Vec< Vec< usize>> = vec![ vec![]; N+1];
    for i in 2..(N+1){
        let a:usize = sc.read();
        edge[a].push(i);
        bedge[i].push(a);
    }
    let mut q:VecDeque<usize> = VecDeque::new();
    q.push_back(1usize);
    while !edge[q[0]].is_empty(){ //In this algorithm, this "q" is never empty.
        if let Some(t) = q.pop_front(){//これがいいのよくわからんな。
            for i in 0..edge[t].len(){
                if edge[edge[t][i]].is_empty(){
                    q.push_back(edge[t][i]);
                }else{
                    q.push_front(edge[t][i]);
                }
            }
        }
    }
    let mut check: Vec<usize> = vec![0;N+1];
    let mut path: Vec<usize> = vec![0;N+1];
    solve(1usize ,&mut path, &edge, &mut check);
    println!("{}", path[1]);
//     let mut h = BinaryHeap::new();
//     for v in q.into_iter(){
//         h.push(State{
//             cost: 0,
//             position: v,
//         })
//     }
//     let mut check = vec![0; N+1];
//     while !h.is_empty(){
//         let mut hash = HashMap::new();
//         while !h.is_empty(){
//             if let Some( State {cost, position}) = h.pop(){
//                 for v in edge[position].iter(){
//                     hash.insert(v, hash.entry(v).or_insert(cost)+1i64);
//                 }
// //                hash.insert(cost + hash.entry(position).or_insert(0), v: V);
//             }
            
//         }        
        
//     }
}

fn solve(t:usize, v:&mut Vec<usize>, w: &Vec<Vec<usize>>, c: &mut Vec<usize>){
    let mut f:Vec<(usize, usize)> = Vec::new();

    for i in 0..(w[t].len()){
        solve(w[t][i], v, w, c);
        c[w[t][i]] = 1;
        f.push((v[w[t][i]] ,w[t][i]));
    }
    f.sort();
    let mut x:usize = 0;
    let a = w[t].len();
    for i in 0..a{
        v[w[t][f[i].1]] = f[i].0;
        if x < f[i].0 + (a-i) + 1 {
            x = f[i].0 + (a-i) + 1;
        }
    }
    

    
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


