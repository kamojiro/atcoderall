use::std::cmp;

const INF: i64 = 1e18 as i64;

fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let n:usize = sc.read();
    let m: usize = sc.read();
    let l: i64 = sc.read();
    let mut dist = vec![vec![INF; n]; n];
    for i in 0..n {
        dist[i][i] = 0;
    }
    for _ in 0..m{
        let a = sc.read::<usize>() - 1;
        let b = sc.read::<usize>() - 1;
        let c = sc.read();
        dist[a][b] = c;
        dist[b][a] = c;
    }

    for u in 0..n{
        for v in 0..n{
            for w in 0..n{
                dist[v][w] = cmp::min(dist[v][w], dist[v][u] + dist[u][w]);
            }
        }
    }

    
    let mut ans = vec![vec![n; n]; n];
    for i in 0..n {
        ans[i][i] = 0;
    }
    for u in 0..n{
        for v in 0..n{
            if u == v{
                ans[u][v] = 0;
                continue;
            }
            if dist[u][v] <= l{
                ans[u][v] = 1;
            }
        }
    }
    
    for u in 0..n{
        for v in 0..n{
            for w in 0..n{
                ans[v][w] = cmp::min(ans[v][w], ans[v][u] + ans[u][w]);
            }
        }
    }

    // for u in 0..n{
    //     for v in 0..n{
    //         println!("{}", ans[u][v]);
    //     }
    // }


    let q: usize = sc.read();
    for _ in 0..q{
        let s:usize = sc.read();
        let t:usize = sc.read();
        if ans[s-1][t-1] == n{
            println!("-1");
        }else{
            println!("{}", ans[s-1][t-1]-1);
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


