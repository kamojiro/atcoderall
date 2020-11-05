#![allow(non_snake_case)]
// use petgraph::unionfind::UnionFind;
use proconio::{fastout, input};
use std::collections::VecDeque;
// use std::collections::BTreeSet;

pub fn main() {
    let _ = ::std::thread::Builder::new()
        .name("run".to_string())
        .stack_size(32 * 1024 * 1024)
        .spawn(run)
        .unwrap()
        .join();
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
    pub M: usize,
    pub B: usize,
    pub Goal: (usize, usize),
    pub Robot: Vec<(usize, usize)>,
    pub Direction: Vec<usize>,
    pub Board: Vec<Vec<bool>>,
}

// read_input
fn read_input() -> Input {
    input! {
        N: usize,
        M: usize,
        B: usize,
        Goal: (usize,usize),
        RC: [(usize,usize,String);M],
        Block: [(usize,usize);B],
    }
    let mut Robot: Vec<(usize, usize)> = Vec::new();
    let mut Direction: Vec<usize> = Vec::new();
    for (ry, rx, c) in RC {
        Robot.push((ry, rx));
        if c == "U".to_string(){
            Direction.push(0);
        }else if c == "D".to_string() {
            Direction.push(1);
        }else if c == "L".to_string(){
            Direction.push(2);
        }else{
            Direction.push(3);
        }
    }
    let mut Board: Vec<Vec<bool>> = vec![vec![true;N];N];
    for (by,bx) in Block{
        Board[by][bx] = false;
    }
    Input {
        N,
        M,
        B,
        Goal,
        Robot,
        Direction,
        Board,
    }
}

fn one_move(input: &Input,board: &mut Vec<Vec<usize>>, ry:usize, rx:usize, c:usize) -> bool{
    let directions:Vec<(usize,usize)> = vec![(input.N-1,0),(1,0),(0,input.N-1),(0,1)];
    let mut d: VecDeque<(usize,usize,usize)> = VecDeque::new();
    let N = input.N;
    let mut before: Vec<Vec<(usize,usize)>> = vec![vec![(N,N);N];N];
    let mut visited: Vec<Vec<bool>> = vec![vec![false;N];N];
    d.push_back((ry,rx,c));
    visited[ry][rx] = true;
    while let Some((y,x,t)) = d.pop_back(){
        // if visited[y][x]{
        //     continue
        // }
        // visited[y][x] = true;
        if y == input.Goal.0 && x == input.Goal.1{
            break
        }
        for i in 0..4{
            let (dy,dx) = directions[i];
            let ay = (y+dy)%N;
            let ax = (x+dx)%N;
            if !input.Board[ay][ax]{
                continue
            }
            if visited[ay][ax]{
                continue
            }
            visited[ay][ax] = true;
            before[ay][ax] = (y,x);
            if t == i{
                d.push_front((ay,ax,i));
            }else{
                d.push_back((ay,ax,i));
            }
            
        }
    }
    if !visited[input.Goal.0][input.Goal.1]{
        return false;
    }
    // restore the pathway
    let mut route: VecDeque<(usize,usize)> = VecDeque::new();
    let mut y = input.Goal.0;
    let mut x = input.Goal.1;
    while before[y][x].0 != N {
        route.push_front((y,x));
        let (py,px) = before[y][x];
        y = py;
        x = px;
    }
    let mut y = ry;
    let mut x = rx;
    let mut t = c;

    'routing: for (py,px) in route{
        // eprintln!("{} {}",py, px );

        for i in 0..4{
            let (dy,dx) = directions[i];
            if (y+dy)%N == py && (x+dx)%N == px{
                if t != i{
                    if board[y][x] < 4{
                        break 'routing;
                    }
                    board[y][x] = i;
                    t = i;
                    break;
                }
            }
        }
        y = py;
        x = px;
    }
    true
}


fn get_output_from_board(input: &Input, board: &Vec<Vec<usize>>) -> Vec<(usize,usize,usize)>{
    let mut ret: Vec<(usize,usize,usize)> = Vec::new();
    for i in 0..input.N{
        for j in 0..input.N{
            if board[i][j] < 4{
                ret.push((i,j,board[i][j]));
            }
        }
    }
    
    ret
}

fn solve(input: &Input) -> Vec<(usize,usize,usize)> {
    let mut board: Vec<Vec<usize>> = vec![vec![4;input.N];input.N];
    for i in 0..input.M{
    // for i in 0..1{
        let (ry,rx) = input.Robot[i];
        let c = input.Direction[i];
        one_move(&input,&mut board, ry, rx, c);
        // board[ry][rx] = 0;
    }
    get_output_from_board(&input, &board)
}

#[fastout]
fn run() {
    // 計測開始
    get_time();
    let input = read_input();
    let out = solve(&input);
    println!("{}", out.len());
    let Direction = ["U","D","L","R"];
    for (y,x,r) in out {
        println!("{} {} {}", y, x, Direction[r]);
    }
}
