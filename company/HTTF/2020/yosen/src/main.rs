#![allow(non_snake_case)]
use std::collections::VecDeque;
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N: usize = sc.read();
    let M:usize = sc.read();
    let B:usize = sc.read();
    let g:(usize, usize) = (sc.read(), sc.read());
    let mut Robot: Vec<(usize, usize, String)> = vec![];
    let mut Block: Vec<(usize, usize)> = vec![];
    for _ in 0..M {
        Robot.push((sc.read(), sc.read(), sc.read()));
    }
    for _ in 0..B{
        Block.push((sc.read(), sc.read()));
    }
//    let Direction: Vec< (i8, i8)> = vec![(-1,0), (1,0), (0,-1), (0,1)];
    let DirectTurn: Vec< Vec<usize>> = vec![ vec![2, 0, 3, 1], vec![0, 2, 1, 3], vec![3, 0, 2, 1], vec![1, 3, 0, 2]];

    let mut q: VecDeque<(usize, usize, usize)> = VecDeque::new();
    //マスの生成とブロックマスの配置
    let mut board:Vec< Vec< Option<usize>>> = vec![ vec![None; N]; N];
    board[g.0][g.1] = Some(5);
    for i in 0..B{
        board[Block[i].0][Block[i].1] = Some(5);
    }
    //    dequeの初期化
    if g.0 < N-1{
        q.push_back((g.0+1, g.1, 0));
    }else if g.0 > 0{
        q.push_back((g.0-1, g.1, 1));
    }
    if g.1 < N-1{
        q.push_back((g.0, g.1+1, 2));
    }
    if g.1 > 0{
        q.push_back((g.0, g.1-1, 3));
    }
    //ゴールから逆探索
    //    println!("search from goal");
    // q.push_front((g.0, g.1));
    while let Some((y, x, z)) = q.pop_front(){
        //        println!("{} {}",y, x );
        if board[y][x] == None{
            board[y][x] = Some(z);
        }else{
            continue;
        }
        if (y > g.0) && ( x + g.0 < y  + g.1) && ( x + y >= g.0+g.1){
            let mut t = true;
            for i in 0..4{
                if let Some((b, a)) = check(y, x, DirectTurn[0][i], N){
                    if t {
//                        board[b][a] = Some(DirectTurn[0][i]);
                        q.push_front((b,a,DirectTurn[0][i]));
                        t = false;
                    }else{
                        q.push_back((b,a,DirectTurn[0][i]));
                    }
                }
            }
        }
        if (x < g.1) && ( x + g.0 <= y + g.1) && ( x+y < g.0+g.1){
            let mut t = true;
            for i in 0..4{
                if let Some((b, a)) = check(y, x, DirectTurn[1][i], N){
                    if t {
                        // board[b][a] = Some(DirectTurn[1][i]);
                        q.push_front((b,a,DirectTurn[1][i]));
                        t = false;
                    }else{
                        q.push_back((b,a,DirectTurn[1][i]));
                    }
                }
            }
        }
        if (y < g.0) && ( x + g.0 > y  + g.1) && ( x + y <= g.0+g.1){
            let mut t = true;
            for i in 0..4{
                if let Some((b, a)) = check(y, x, DirectTurn[2][i], N){
                    if t {
                        // board[b][a] = Some(DirectTurn[2][i]);
                        q.push_front((b,a,DirectTurn[2][i]));
                        t = false;
                    }else{
                        q.push_back((b,a,DirectTurn[2][i]));
                    }
                }
            }
        }
        if (x > g.1) && ( x + g.0 <= y + g.1) && ( x+y < g.0+g.1){
            let mut t = true;
            for i in 0..4{
                if let Some((b, a)) = check(y, x, DirectTurn[3][i], N){
                    if t {
                        // board[b][a] = Some(DirectTurn[3][i]);
                        q.push_front((b,a,DirectTurn[3][i]));
                        t = false;
                    }else{
                        q.push_back((b,a,DirectTurn[3][i]));
                    }
                }
            }
        }
    }

    //通り道の確認
    //
    let mut need:Vec< Vec< usize>> = vec![ vec![0; N]; N];
    need[g.0][g.1] = 5;
    for i in 0..B{
        need[Block[i].0][Block[i].1] = 5;
    }
    for i in 0..M{
        let mut now:usize = 0;
        if Robot[i].2 == "U"{
            now = 0;
        }else if  Robot[i].2 == "D"{
            now = 1;
        }else if Robot[i].2 == "L"{
            now = 2;
        }else if Robot[i].2 == "R"{
            now = 3;
        }
        let mut by = Robot[i].0;
        let mut bx = Robot[i].1;
        let mut luck:Vec< Vec< usize>> = vec![ vec![0; N]; N];
        while by != g.0 || bx != g.1{
            if luck[by][bx] == 1{
                break;
            }
            luck[by][bx] = 1;
            if (by < 0) || (N <= by) || (bx < 0usize) || (N<=bx){
                break;
            }
            if let Some(t) = board[by][bx]{
                if t == 5usize{
                    break;
                }

                if now != t{
                    now = t;
                    need[by][bx] = 1;
                }
                if t == 0usize{
                    by += 1;
                }else if t == 1usize{
                    by -= 1;
                }else if t == 2usize{
                    bx -= 1;
                }else if t == 3usize{
                    bx += 1;
                }
            }
        }
    }
    


    
    // 答えの確認
//    println!("ANS");
    let mut k:usize = 0;
    let l:usize = 0;
    let r:usize = 4;
    for i in 0..N{
        for j in 0..N{
            if let Some(t) = board[i][j]{
                if l <= t && t < r && need[i][j] == 1{
                    k += 1;
                }
            }
        }
    }
    println!("{}", k);
    
    for i in 0..N{
        for j in 0..N{
            if let Some(t) = board[i][j]{
                if l <= t && t < r && need[i][j] == 1{
                    if t == 0usize{
                        println!("{} {} {}",i, j, 'U' );
                    }else if t == 1usize{
                        println!("{} {} {}",i, j, 'D' );
                    }else if t == 2usize{
                        println!("{} {} {}",i, j, 'L' );
                    }else if t == 3usize{
                        println!("{} {} {}",i, j, 'R' );
                    }
                }
            }
        }
    }
}

fn check(y:usize, x:usize, num:usize, n: usize) -> Option<(usize, usize)>{
    if num == 0{
        if y < n-1 {
//            println!("{}",num );
            return Some((y+1, x))
       } 
    }
    if num == 1{
        if y > 0{
//            println!("{}",num );
            return Some((y-1, x))
        }
    }
    if num == 2{
        if x < n-1 {
//            println!("{}",num );
            return Some((y, x+1)) 
        }
    }
    if num == 3{
        if x > 0{
//            println!("{}",num );
            return Some((y, x-1))
        }
    }
    None
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


