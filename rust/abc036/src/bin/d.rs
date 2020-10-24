#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {
        N: usize,
        edges: [(usize, usize);N-1],
        //array: [(usize,usize);N],
    }
    let Q:u64 = 10u64.pow(9) + 7;
    let mut E: Vec<Vec<usize>> = vec![vec![]; N];
    for (a, b) in edges {
        let am = a - 1;
        let bm = b - 1;
        E[am].push(bm);
        E[bm].push(am);
    }
    let mut stack: Vec<usize> = Vec::new();
    stack.push(0);
    let mut visited = vec![false; N];
    let mut root = vec![0; N];
    let mut turn = Vec::new();
    let mut dp: Vec<Vec<u64>> = vec![vec![1,1];N];
    while let Some(v) = stack.pop() {
        if visited[v] {
            continue;
        }
        visited[v] = true;
        turn.push(v);
        for &w in &E[v]{
            if visited[w]{
                continue
            }
            root[w] = v;
            stack.push(w);
            // if E[w].len() == 1{
            //     dp[w][0] = 1;
            //     dp[w][1] = 1;
            // }
        }
    }
    for &v in turn.iter().rev(){
        if v == 0usize{
            break
        }
        let w = root[v];
        dp[w][0] = (dp[w][0]*dp[v][1])%Q;
        dp[w][1] = (dp[w][1]*((dp[v][0] + dp[v][1])%Q))%Q;
    }
    // println!("{:?}", E);
    // println!("{:?}", dp);
    println!("{}", (dp[0][0] + dp[0][1])%Q);   
}
