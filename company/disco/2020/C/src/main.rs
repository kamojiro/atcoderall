#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let H:usize = sc.read();
    let W:usize = sc.read();
    let K:usize = sc.read();
    let mut P:Vec<(usize, usize)> = vec![];
    let A:Vec< Vec< char>> = (0..H).map(|_| sc.chars()).collect();
    // for i in 0..H{
    //     for j in 0..W{
    //         println!("{}", A[i][j]);
    //     }
    //     println!("huga");
    // }
    let mut ans:Vec< Vec< usize>> = vec![ vec![0; W]; H];
    let mut now:usize = 1;

    for i in 0..H{
        for j in 0..W{
            if A[i][j] == '#'{
                P.push((i, j));
                ans[i][j] = now;
                now += 1;
            }
        }
    }
    for k in 0..K{
        ans[P[k].0][P[k].1] = k+1;
        let X = P[k].0;
        let Y = P[k].1;
        let mut LY:usize = Y;
        if Y > 0{
            for y in (0..Y).rev(){
                if ans[X][y] > 0{
                    break
                }
                LY = y;
                ans[X][y] = k+1;
            }
        }
        let mut U:Vec<usize> = vec![];
        U.push(X);
        if X > 0{
            for x in (0..X).rev(){
                if ans[x][LY] > 0{
                    break
                }
                ans[x][LY] = k+1;
                U.push(x);
            }
        }
        let lenU = U.len();
        let mut D:Vec<usize> = vec![];
//        D.push(LY);
        for y in LY..W{
            let mut check = true;
            for i in 0..lenU{
                if (ans[U[i]][y] > 0) && (ans[U[i]][y] != k+1){
                    check = false;
                }
            }
            if !check{
                break
            }
            D.push(y);
            for i in 0..lenU{
                ans[U[i]][y] = k+1;
            }
        }
        let lenD = D.len();

        for x in X..H{
            let mut check = true;
            for i in 0..lenD{
                if (ans[x][D[i]] > 0) && (ans[x][D[i]] != k+1){
                    check = false;
                }
            }
            if !check{
                break
            }
            for i in 0..lenD{
                ans[x][D[i]] = k+1;
            }

        }        
    }
    for i in 0..H{
        for j in 0..W{
            print!("{} ", ans[i][j]);
        }
        println!("");
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


