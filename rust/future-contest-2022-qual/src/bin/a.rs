// -*- coding:utf-8-unix -*-
#![allow(non_snake_case)]

// use std::collections::VecDeque;

use std::cmp::max;
use std::cmp::Reverse;
use rand::prelude::SliceRandom;

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
    pub K: usize,
    pub R: usize,
    pub D: Vec<Vec<i64>>,
    pub edges: Vec<Vec<usize>>,
}

fn read_input() -> Input {
    let (r, w) = (std::io::stdin(), std::io::stdout());
    let mut sc = IO::new(r.lock(), w.lock());

    let N: usize = sc.read();
    let M: usize = sc.read();
    let K: usize = sc.read();
    let R: usize = sc.read();
    let D: Vec<Vec<i64>> = (0..N).map(|_| sc.vec(K)).collect();
    let mut edges = vec![vec![]; N];
    for _ in 0..R{
        let u = sc.usize0();
        let v = sc.usize0();
        edges[u].push(v);
    }
	Input {N, M, K, R, D, edges}
}

fn solve(input: &Input){
    let T = 1000;
    let mut rng = rand::thread_rng();
    let d_sum = sum_d(input);
    let mut S = vec![vec![40; input.K]; input.M];
    let mut member_assigned_task = vec![std::usize::MAX; input.M];
    let mut member_task_started = vec![0; input.M];
    let mut tasks_prepared = vec![0; input.N];
    for u in 0..input.N{
        for &v in &input.edges[u]{
            tasks_prepared[v] += 1;
        }
    }
    let mut tasks = Vec::new();
    for u in 0..input.N{
        if tasks_prepared[u] == 0{
            tasks.push(u);
        }
    }
    // tasks.shuffle(&mut rng);
    for day in 0..2010{
        let mut assign_today = Vec::new();
        let mut estimated_best_time = std::i64::MAX;
        tasks.sort_by_key(|&x| Reverse(d_sum[x]));
        let superiority_order = sort_by_superiority(input, &S);
        for _ in 0..T{            
            let mut assign_today_candidate = Vec::new();
            let mut j = 0;
            for &i in &superiority_order{
                if member_assigned_task[i] < std::usize::MAX{continue;}
                if j == tasks.len(){break;}
                assign_today_candidate.push((i, tasks[j]));
                j += 1;
            }
            let expected_working_days_sum =  calculate_working_days_sum(&input, &S, &assign_today_candidate);
            if expected_working_days_sum < estimated_best_time{
                assign_today = assign_today_candidate;
                estimated_best_time = expected_working_days_sum;
            }
            tasks.shuffle(&mut rng);
        }

        if !assign_today.is_empty(){
            let mut enabled_task = vec![false; input.N];
            for &task in &tasks{
                enabled_task[task] = true;
            }
            for &(_, task) in &assign_today{
                enabled_task[task] = false;
            }
            tasks = (0..input.N).filter(|&i| enabled_task[i]).collect();
        }
        
        print!("{} ", assign_today.len());
        for &(worker, task) in &assign_today{
            member_assigned_task[worker] = task;
            member_task_started[worker] = day;
            print!("{} {} ", worker+1, task+1);
        }
        println!();
        assign_today.clear();
        let (r, w) = (std::io::stdin(), std::io::stdout());
        let mut sc = IO::new(r.lock(), w.lock());
        let n: i64 = sc.read();
        if n == -1{
            return;
        }
        let unassigned_member: Vec<usize> = sc.vec(n as usize);
        for &worker in &unassigned_member{
            let u = member_assigned_task[worker-1];
            let s = estimate_s(&input, u , day - member_task_started[worker-1]+1);
            for k in 0..input.K{
                S[worker-1][k] = s;
            }
            for &v in &input.edges[u]{
                tasks_prepared[v] -= 1;
                if tasks_prepared[v] == 0{
                    tasks.push(v);
                }
            }
            member_assigned_task[worker-1] = std::usize::MAX;
        }
        // tasks.shuffle(&mut rng);
    }
    
}

fn calculate_working_days_sum(input: &Input, S: &Vec<Vec<i64>>, assign: &Vec<(usize, usize)>) -> i64{
    let mut ret = 0;
    for &(worker, task) in assign{
        for k in 0..input.K{
            // sum なので、max(1) はしない
            ret += max(0, input.D[task][k] - S[worker][k]);
        }
    }
    ret
}

// #[allow(dead_code)]
// fn calculate_working_days_max(input: &Input, S: &Vec<Vec<i64>>, assign: &Vec<(usize, usize)>) -> i64{
//     unimplemented!();
// }

fn sum_d(input: &Input) -> Vec<i64>{
    let mut ret = Vec::new();
    for i in 0..input.N{
        let s = input.D[i].iter().fold(0, |s,x| s+x);
        ret.push(s);
    }
    ret
}

fn sort_by_superiority(input: &Input, S: &Vec<Vec<i64>>) -> Vec<usize>{
    let mut s_sum = Vec::new();
    for i in 0..input.M{
        let p = S[i].iter().fold(0, |s,x| s+x);
        s_sum.push(p);
    }
    let mut ret: Vec<usize> = (0..input.M).collect();
    ret.sort_by_key(|&x| Reverse(s_sum[x]));
    ret
}

fn estimate_s(input: &Input, task_num: usize, measured_time: i64) -> i64{
    let mut ret = 40;
    let mut diff = std::i64::MAX;
    for s in 20..=60{
        let mut s_diff = 0;
        for k in 0..input.K{
            s_diff += max(0, input.D[task_num][k] - s);
        }
        s_diff = s_diff.max(1);
        if (s_diff - measured_time).abs() < diff{
            diff = s_diff;
            ret = s;
        }
    }
    ret
}


// #[fastout]
fn run() {
    // 計測開始
    get_time();
    let input = read_input();
    // const TL: f64 = 2.8;    

    solve(&input);
}

#[allow(dead_code)]
fn fundamental_solve(input: &Input){
    let mut rng = rand::thread_rng();
    let mut member_assigned_task = vec![std::usize::MAX; input.M];
    let mut tasks_prepared = vec![0; input.N];
    for u in 0..input.N{
        for &v in &input.edges[u]{
            tasks_prepared[v] += 1;
        }
    }
    eprintln!("{:?}", tasks_prepared);
    let mut tasks = Vec::new();
    for u in 0..input.N{
        if tasks_prepared[u] == 0{
            tasks.push(u);
        }
    }
    tasks.shuffle(&mut rng);
    loop {
        let mut assign_today = Vec::new();
        for i in 0..input.M{
            if member_assigned_task[i] < std::usize::MAX{continue;}
            if let Some(u) = tasks.pop(){
                assign_today.push((i, u));
            }else{
                break
            }
        }
        print!("{} ", assign_today.len());
        for &(worker, task) in &assign_today{
            member_assigned_task[worker] = task;
            print!("{} {} ", worker+1, task+1);
        }
        println!();
        assign_today.clear();
        let (r, w) = (std::io::stdin(), std::io::stdout());
        let mut sc = IO::new(r.lock(), w.lock());
        let n: i64 = sc.read();
        if n == -1{
            return;
        }
        let unassigned_member: Vec<usize> = sc.vec(n as usize);
        for &worker in &unassigned_member{
            let u = member_assigned_task[worker-1];
            member_assigned_task[worker-1] = std::usize::MAX;
            for &v in &input.edges[u]{
                tasks_prepared[v] -= 1;
                if tasks_prepared[v] == 0{
                    tasks.push(v);
                }
            }
        }
        tasks.shuffle(&mut rng);
    }
    
}


pub struct IO<R, W: std::io::Write>(R, std::io::BufWriter<W>);
 
impl<R: std::io::Read, W: std::io::Write> IO<R, W> {
    pub fn new(r: R, w: W) -> IO<R, W> {
        IO(r, std::io::BufWriter::new(w))
    }
    pub fn write<S: ToString>(&mut self, s: S) {
        use std::io::Write;
        self.1.write_all(s.to_string().as_bytes()).unwrap();
    }
    pub fn read<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        let buf = self
            .0
            .by_ref()
            .bytes()
            .map(|b| b.unwrap())
            .skip_while(|&b| b == b' ' || b == b'\n' || b == b'\r' || b == b'\t')
            .take_while(|&b| b != b' ' && b != b'\n' && b != b'\r' && b != b'\t')
            .collect::<Vec<_>>();
        unsafe { std::str::from_utf8_unchecked(&buf) }
            .parse()
            .ok()
            .expect("Parse error.")
    }
    pub fn usize0(&mut self) -> usize {
        self.read::<usize>() - 1
    }
    pub fn vec<T: std::str::FromStr>(&mut self, n: usize) -> Vec<T> {
        (0..n).map(|_| self.read()).collect()
    }
    pub fn chars(&mut self) -> Vec<char> {
        self.read::<String>().chars().collect()
    }
}
