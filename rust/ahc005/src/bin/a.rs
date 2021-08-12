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
use std::collections::{BinaryHeap, HashSet};

use proconio::marker::Bytes;
use proconio::{fastout, input};
use rand::{thread_rng, Rng};

pub fn main() {
    let _ = ::std::thread::Builder::new()
        .name("run".to_string())
        .stack_size(32 * 1024 * 1024)
        .spawn(run)
        .unwrap()
        .join();
}


#[fastout]
fn run() {
    // 計測開始
    const TL: f64 = 2.9;
    get_time();

    let input = read_input();
    let points = necessary_points(&input);
    let mut minimum_points = minimize_light(&input, &points);
    let mut ans = make_ans(&input, &minimum_points);
    if minimum_points.len() <= 4{
        print_ans(&input, &mut ans);
        return;
    }
    let mut cost = get_cost(&input, &ans);
    loop {
        let t = get_time()/TL;
        // eprintln!("{}", get_time());
        let new = two_sat(&minimum_points);
        let new_ans = make_ans(&input, &new);
        let new_cost= get_cost(&input, &new_ans);
        if new_cost < cost{
            minimum_points = new;
            ans = new_ans;
            cost = new_cost;
        }
        if t >= 1.0{
            break
        }
    }

    // let mut ans = make_ans(&input, minimum_points);
    print_ans(&input, &mut ans);
}


fn two_sat(ans: &Vec<(usize,usize)>) -> Vec<(usize,usize)>{
    let n = ans.len();
    let mut rng = thread_rng();
    let s = rng.gen_range(1, n-2);
    let t = rng.gen_range(s+1, n);
    let mut ret = Vec::new();
    for i in 0..s{
        ret.push(ans[i]);
    }
    for i in (s..t).rev(){
        ret.push(ans[i])
    }
    for i in t..n{
        ret.push(ans[i])
    }
    ret
    
}

fn get_cost(input: &Input, ans: &Vec<(usize,usize)>) -> usize{
    if ans.len() == 0{
        return 0
    }
    let mut ret = 0;
    for i in 0..(ans.len()-1){
        let z = ans[i];
        ret += input.C[z.0][z.1]
    }
    ret
}


fn make_ans(input: &Input, route: &Vec<(usize,usize)>) -> Vec<(usize,usize)>{
    if route.len() == 0{
        return vec![(input.s.0, input.s.1)]
    }
    let mut x = route[0].0;
    let mut y = route[0].1;
    let mut ans = vec![(input.s.0, input.s.1)];
    for i in 1..route.len(){
        let mut path = shortest_path(input, x, y, route[i].0, route[i].1);
        // eprintln!("start ({},{}), goal ({},{})", x,y,route[i].0, route[i].1);
        // eprintln!("{:?}", path);
        ans.append(&mut path);
        x = route[i].0;
        y = route[i].1;
    }
    ans
}

fn shortest_path(input: &Input, sx: usize, sy: usize, gx: usize, gy: usize) -> Vec<(usize,usize)>{
    if sx == gx && sy == gy{
        return vec![]
    }
    let mut visited = vec![vec![std::usize::MAX; input.N]; input.N];
    let mut previous = vec![vec![(0,0); input.N]; input.N];
    let mut queue = BinaryHeap::new();
    queue.push((Reverse(0), sx,sy,sx,sy));
    while let Some((Reverse(dist),x,y,px,py)) = queue.pop(){
        if visited[x][y] < std::usize::MAX{
            continue;
        }
        visited[x][y] = dist;
        previous[x][y] = (px,py);
        if x == gx && y == gy{
            break
        }
        if x > 0{
            if visited[x-1][y] == std::usize::MAX && input.C[x-1][y] != 0{
                queue.push((Reverse(dist+input.C[x-1][y]), x-1,y,x,y));
            }
        }
        if x < input.N-1{
            if visited[x+1][y] == std::usize::MAX && input.C[x+1][y] != 0{
                queue.push((Reverse(dist+input.C[x+1][y]), x+1,y,x,y));
            }        
        }
        if y > 0{
            if visited[x][y-1] == std::usize::MAX&& input.C[x][y-1] != 0{
                queue.push((Reverse(dist+input.C[x+1][y]), x,y-1,x,y));
            }
        }
        if y < input.N-1{
            if visited[x][y+1] == std::usize::MAX&& input.C[x][y+1] != 0{
                queue.push((Reverse(dist+input.C[x+1][y]), x,y+1,x,y));
            }
        }
    }
    let mut z = (gx,gy);
    let mut ret = Vec::new();
    while z.0 != sx || z.1 != sy{
        ret.push(z);
        z = previous[z.0][z.1];
    }
    ret.reverse();
    ret
}

fn minimize_light(input: &Input, lights: &Vec<(usize,usize)>) -> Vec<(usize,usize)>{
    let mut needs = vec![true; lights.len()];
    let mut board = vec![vec![0i64; input.N]; input.N];
    for z in lights.iter(){
        update_board(input, &mut board, z.0,z.1, 1);
    }

    for (i, (x,y)) in lights.iter().enumerate(){
        if *x == input.s.0 && *y == input.s.1{continue;}
        if check_needs(input, &board, *x, *y){continue;}
        // eprintln!("{} {}", x,y);
        update_board(input, &mut board, *x, *y, -1);
        // eprintln!("{:?}", board);
        needs[i] = false;
    }

    (0..lights.len()).filter(|&x| needs[x]).map(|x| lights[x]).collect()
}

fn check_needs(input: &Input, board: &Vec<Vec<i64>>, x: usize, y: usize) -> bool{
    if board[x][y] == 1{
        return true
    }
    for i in (0..x).rev(){
        if input.C[i][y] == 0{
            break
        }
        if board[i][y] == 1{
            return true
        }
    }
    for i in (x+1)..input.N{
        if input.C[i][y] == 0{
            break
        }
        if board[i][y] == 1{
            return true
        }
    }
    for j in (0..y).rev(){
        if input.C[x][j] == 0{
            break
        }
        if board[x][j] == 1{
            return true
        }
    }
    for j in (y+1)..input.N{
        if input.C[x][j] == 0{
            break
        }
        if board[x][j] == 1{
            return true
        }
    }
    false
}

fn update_board(input: &Input, board: &mut Vec<Vec<i64>>, x: usize, y: usize, cost: i64){
    board[x][y] += cost;
    for i in (0..x).rev(){
        if input.C[i][y] == 0{
            break
        }
        board[i][y] += cost;
    }
    for i in (x+1)..input.N{
        if input.C[i][y] == 0{
            break
        }
        board[i][y] += cost;
    }
    for j in (0..y).rev(){
        if input.C[x][j] == 0{
            break
        }
        board[x][j] += cost;
    }
    for j in (y+1)..input.N{
        if input.C[x][j] == 0{
            break
        }
        board[x][j] += cost;
    }
}


fn necessary_points(input: &Input) -> Vec<(usize, usize)>{
    let mut set = HashSet::new();
    for i in 0..input.N{
        let mut now = 0;
        for j in 0..input.N{
            if input.C[i][j] == 0{
                if now+1 >= j{
                    now = j;
                    continue;
                }
                let mut point = now+1;
                'jsearch: for p in (now+1)..j{
                    if i > 0{
                        if input.C[i-1][p] > 0{
                            point = p;
                            break 'jsearch
                        }
                    }
                    if i < input.N-1{
                        if input.C[i+1][p] > 0{
                            point = p;
                            break 'jsearch
                        }
                    }
                }
                set.insert((i, point));
                now = j;
            }
        }
    }
    for j in 0..input.N{
        let mut now = 0;
        for i in 0..input.N{
            if input.C[i][j] == 0{
                if now+1 >= i{
                    now = i;
                    continue;
                }
                let mut point = now+1;
                'isearch: for p in (now+1)..i{
                    if j > 0{
                        if input.C[p][j-1] > 0{
                            point = p;
                            break 'isearch
                        }
                    }
                    if j < input.N-1{
                        if input.C[p][j+1] > 0{
                            point = p;
                            break 'isearch
                        }
                    }
                }
                set.insert((point, j));
                now = i;
            }
        }
    }
    let mut ret = vec![(input.s.0, input.s.1)];
    let mut hoge = set.into_iter().collect();
    ret.append(&mut hoge);
    if ret.len() > 1{
        ret.push((input.s.0, input.s.1));
    }
    ret
}

#[allow(dead_code)]
fn solve_dfs(input: &Input) -> Vec<(usize, usize)>{
    let mut visited = vec![vec![false; input.N]; input.N];
    let mut ret = Vec::new();
    visited[input.s.0][input.s.1] = true;
    dfs(input, input.s.0, input.s.1, &mut ret, &mut visited);
    ret
}

#[allow(dead_code)]
fn dfs(input: &Input, x: usize, y: usize, route: &mut Vec<(usize,usize)>, visited: &mut Vec<Vec<bool>>){
    route.push((x,y));
    if x > 0{
        if !visited[x-1][y] && input.C[x-1][y] != 0{
            visited[x-1][y] = true;
            dfs(input, x-1, y, route, visited);
            route.push((x,y));
        }
    }
    if x < input.N-1{
        if !visited[x+1][y] && input.C[x+1][y] != 0{
            visited[x+1][y] = true;
            dfs(input, x+1, y, route, visited);
            route.push((x,y));
        }        
    }
    if y > 0{
        if !visited[x][y-1] && input.C[x][y-1] != 0{
            visited[x][y-1] = true;
            dfs(input, x, y-1, route, visited);
            route.push((x,y));
        }
    }
    if y < input.N-1{
        if !visited[x][y+1] && input.C[x][y+1] != 0{
            visited[x][y+1] = true;
            dfs(input, x, y+1, route, visited);
            route.push((x,y));
        }        
    }
}


fn print_ans(input: &Input, ans: &mut Vec<(usize, usize)>){
    let N = ans.len();
    if N == 0{
        println!();
        return;
    }
    if N == 1{
        if ans[0].0 == input.s.0 && ans[0].1 == input.s.1{
            println!();
            return;
        }else{
            ans.push(input.s);
        }
            
    }
    for i in 0..(N-1){
        if ans[i].0 == ans[i+1].0 && ans[i].1 == ans[i+1].1{
            continue;
        }
        if ans[i].0 == ans[i+1].0{
            if ans[i].1 < ans[i+1].1{
                print!("R")
            }else{
                print!("L")
            }
        }else{
            if ans[i].0 < ans[i+1].0{
                print!("D")
            }else{
                print!("U")
            }            
        }
    }
    println!();
}


pub fn get_time() -> f64 {
    static mut STIME: f64 = -1.0;
    let t = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap();
    let ms = t.as_secs() as f64 + t.subsec_nanos() as f64 * 1e-9;
    unsafe {
        if STIME < 0.0 {
            STIME = ms;
        }
        ms - STIME
    }
}

#[derive(Clone, Debug)]
pub struct Input {
    pub N: usize,
    pub s: (usize,usize),
    pub C: Vec<Vec<usize>>,
}

// read_input
fn read_input() -> Input {
    input!{
        mut N: usize,
        si: usize,
        sj: usize,
        B: [Bytes; N],
    }
    let s = (si+1,sj+1);
    let mut C = Vec::new();
    C.push(vec![0; N+2]);
    for i in 0..N{
        let mut F: Vec<usize> = B[i].iter().map(|&x| if x == b'#'{0} else{x - b'0'}).map(|x| x as usize).collect();
        F.insert(0, 0);
        F.push(0);
        C.push(F);
    }
    C.push(vec![0; N+2]);
    N += 2;
	Input {N, s, C}
}
