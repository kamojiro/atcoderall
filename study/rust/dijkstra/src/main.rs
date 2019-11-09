use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Copy, Clone, Eq, PartialEq)] //トレイトを自動実装している
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
    let n:usize = sc.read();
    let m:usize = sc.read();
    let mut s:usize = sc.read();
    let mut t:usize = sc.read();
    s -= 1; t -= 1;
    let mut yen_graph = vec![vec![];n];
    let mut snuuk_graph = vec![vec![];n];
    for _ in 0..m{
        let mut u:usize = sc.read();
        let mut v:usize = sc.read();
        let a:i64 = sc.read();
        let b:i64 = sc.read();
        u -= 1; v -= 1;
        yen_graph[u].push(Edge{
            node: v,
            cost: a,
        });
        yen_graph[v].push(Edge{
            node: u,
            cost: a,
        });
        snuuk_graph[u].push(Edge{
            node: v,
            cost: b,
        });
        snuuk_graph[v].push(Edge{
            node: u,
            cost: b,
        });
    }
    
    let yen_shortest_path: Vec<_> = dijkstra(&yen_graph, s);
    let snuuk_shortest_path: Vec<_> = dijkstra(&snuuk_graph, t);
    let mut sum_shortest_path = Vec::new();
    for i in 0..n {
        sum_shortest_path.push((i, yen_shortest_path[i] + snuuk_shortest_path[i]));
    }
    sum_shortest_path.sort_by(|a, b| (a.1).cmp(&b.1));
    let mut years: usize = 0;
    let mut ans: Vec<i64> = Vec::new();
    for i in 0..n{
        while sum_shortest_path[years].0 < i{
            years += 1;
        }
        while sum_shortest_path[years].0 < i{
            years += 1;
        }

        ans.push(sum_shortest_path[years].1);
    }
    let start_money = 1e15 as i64;
    for i in 0..n {
        println!("{}", start_money - ans[i]);
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


