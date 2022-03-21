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

use std::{cmp::Reverse, mem::swap};

use itertools::Itertools;
use proconio::{fastout, input};
use rand::{thread_rng, Rng};
use rand::seq::SliceRandom;

pub fn main() {
    let _ = ::std::thread::Builder::new()
        .name("run".to_string())
        .stack_size(32 * 1024 * 1024)
        .spawn(run)
        .unwrap()
        .join();
}

#[allow(dead_code)]
fn solve_sat4(input: &Input) -> (Vec<usize>, Vec<(i64, i64)>){
    let mut order_list = Vec::new();
    let order = nearest_sum_order(input);
    for i in 0..input.K{
        order_list.push(order[i].1);
    }
    let mut route = Vec::new();
    route.push((input.atcoder.0, input.atcoder.1, input.N));
    for i in 0..input.K{
        let x = input.ABCD[order[i].1];
        route.push((x.0, x.1, i));
    }
    for i in 0..input.K{
        let x = input.ABCD[order[i].1];
        route.push((x.2, x.3, i));
    }
    route.push((input.atcoder.0, input.atcoder.1, input.N));
    all_sat(input, &order_list,100000, &mut route);
    (order_list,route)
    
}

fn all_sat(input: &Input,order_list: &Vec<usize>,  times: usize, route: &mut Vec<(i64,i64, usize)>){
    let mut score = compute_score(route);
    for _ in 0..times{
        let mut rng = thread_rng();
        let i = rng.gen_range(0, input.K);
        let mut s = rng.gen_range(1, 101);
        let mut t = rng.gen_range(1, 101);
        if s == t{continue;}
        if s > t {swap(&mut s, &mut t)}
        let x = input.ABCD[order_list[i]];
        let satted_route = satting2(route,s,t, (x.0,x.1), (x.2, x.3));
        let satted_route_score = compute_score(&satted_route);
        if  satted_route_score < score{
            score = satted_route_score;
            *route = satted_route;
        }
    }
}

fn satting2(route: &Vec<(i64,i64,usize)>, s:usize, t:usize, x: (i64,i64), y: (i64,i64)) -> Vec<(i64,i64)>{
    let mut xt = true;
    let mut yt = true;
    let mut ves = Vec::new();
    let n = route.len();
    ves.push(route[0]);
    for i in 1..(n-1){
        if xt && route[i] == x{
            xt = false;
            continue;
        }
        if yt && route[i] == y{
            yt = false;
            continue;
        }
        ves.push(route[i]);
    }
    ves.push(route[n-1]);
    ves.insert(s, x);
    ves.insert(t, y);
    ves
}



#[allow(dead_code)]
fn solve_sat3(input: &Input) -> (Vec<usize>, Vec<(i64, i64)>){
    let mut order = (0..input.N).collect_vec();
    let mut rng = thread_rng();
    let times: usize = 1000;
    let mut order_list = Vec::new();
    let mut route = Vec::new();
    let mut score = 1000000;
    for _ in 0..100{
        order.shuffle(&mut rng);
        let mut sorder_list = Vec::new();
        for i in 0..input.K{
            sorder_list.push(order[i]);
        }
        let mut sroute = Vec::new();
        sroute.push(input.atcoder);
        for i in 0..input.K{
            let x = input.ABCD[order[i]];
            sroute.push((x.0, x.1));
        }
        for i in 0..input.K{
            let x = input.ABCD[order[i]];
            sroute.push((x.2, x.3));
        }
        sroute.push(input.atcoder);
        separation_sat(times, 1, 51, 101, &mut sroute);
        if compute_score(&sroute) < score{
            score = compute_score(&sroute);
            order_list = sorder_list;
            route = sroute;
        }
    }
    (order_list,route)
    
}


#[allow(dead_code)]
fn solve_sat2(input: &Input) -> (Vec<usize>, Vec<(i64, i64)>){
    let mut order_list = Vec::new();
    let order = mesh_order(input);
    for i in 0..input.K{
        order_list.push(order[i]);
    }
    let mut route = Vec::new();
    route.push(input.atcoder);
    for i in 0..input.K{
        let x = input.ABCD[order[i]];
        route.push((x.0, x.1));
    }
    for i in 0..input.K{
        let x = input.ABCD[order[i]];
        route.push((x.2, x.3));
    }
    route.push(input.atcoder);
    let times = 100000;
    separation_sat(times, 1, 51, 101, &mut route);
    (order_list,route)
    
}

fn mesh_order(input: &Input) -> Vec<usize>{
    let mesh_size = 100;
    let mesh_count = (input.H + mesh_size)/mesh_size;
    // eprintln!("{}", mesh_count);
    let mut mesh = vec![vec![vec![vec![vec![];mesh_count]; mesh_count]; mesh_count]; mesh_count];
    for (i,&(a,b,c,d)) in input.ABCD.iter().enumerate(){
        mesh[(a as usize)/mesh_size][(b as usize)/mesh_size][(c as usize)/mesh_size][(d as usize)/mesh_size].push(i);
    }
    let mut meshes = Vec::new();
    for a in 0..mesh_count{
        for b in 0..mesh_count{
            for c in 0..mesh_count{
                for d in 0..mesh_count{
                    meshes.push((mesh[a][b][c][d].len(), a,b,c,d))
                }
            }
        }
    }
    meshes.sort_by_key(|x| Reverse(x.0));
    let mut ret = Vec::new();
    for &(_,a,b,c,d) in &meshes{
        for &i in &mesh[a][b][c][d]{
            ret.push(i);
        }
        if ret.len() >= input.K{
            break
        }
    }
    ret
    
}


#[allow(dead_code)]
fn solve_sat1(input: &Input) -> (Vec<usize>, Vec<(i64, i64)>){
    let mut order_list = Vec::new();
    let order = nearest_sum_order(input);
    for i in 0..input.K{
        order_list.push(order[i].1);
    }
    let mut route = Vec::new();
    route.push(input.atcoder);
    for i in 0..input.K{
        let x = input.ABCD[order[i].1];
        route.push((x.0, x.1));
    }
    for i in 0..input.K{
        let x = input.ABCD[order[i].1];
        route.push((x.2, x.3));
    }
    route.push(input.atcoder);
    separation_sat(100000,1, 51, 101, &mut route);
    (order_list,route)
    
}

fn separation_sat(times: usize, sa: usize, sb: usize, sc: usize, route: &mut Vec<(i64,i64)>){
    let mut score = compute_score(route);
    for _ in 0..times{
        let mut rng = thread_rng();
        let mut s = rng.gen_range(sa, sb);
        let mut t = rng.gen_range(sa, sb);
        if s == t{continue;}
        if s > t {swap(&mut s, &mut t)}
        let satted_route = satting(route,s,t);
        let satted_route_score = compute_score(&satted_route);
        if  satted_route_score < score{
            score = satted_route_score;
            *route = satted_route;
        }
    }
    for _ in 0..times{
        let mut rng = thread_rng();
        let mut s = rng.gen_range(sb, sc);
        let mut t = rng.gen_range(sb, sc);
        if s == t{continue;}
        if s > t {swap(&mut s, &mut t)}
        let satted_route = satting(route,s,t);
        let satted_route_score = compute_score(&satted_route);
        if  satted_route_score < score{
            score = satted_route_score;
            *route = satted_route;
        }
    }
}

fn satting(route: &Vec<(i64,i64)>, s:usize, t:usize) -> Vec<(i64,i64)>{
    let n = route.len();
    let mut ret = Vec::new();
    for i in 0..s{
        ret.push(route[i]);
    }
    for i in (s..t).rev(){
        ret.push(route[i])
    }
    for i in t..n{
        ret.push(route[i])
    }
    ret
}





#[allow(dead_code)]
fn fundamental_solve(input: &Input) -> (Vec<usize>, Vec<(i64, i64)>){
    let mut order_list = Vec::new();
    let order = nearest_sum_order(input);
    let mut ret = Vec::new();
    ret.push(input.atcoder);
    for i in 0..input.K{
        order_list.push(order[i].1);
        let x = input.ABCD[order[i].1];
        ret.push((x.0, x.1));
        ret.push((x.2, x.3));            
    }
    ret.push(input.atcoder);
    (order_list,ret)
}

fn compute_score(route: &Vec<(i64,i64)>) -> i64{
    let n = route.len();
    let mut time = 0;
    for i in 0..(n-1){
        time += distance(route[i], route[i+1])
    }
    time
}

fn nearest_sum_order(input: &Input) -> Vec<(i64,usize)>{
    let mut orders = Vec::new();
    for (i, &(a,b,c,d)) in input.ABCD.iter().enumerate(){
        orders.push((distance(input.atcoder, (a,b)) + distance((a,b), (c,d)),i))
    }
    orders.sort();
    orders
}

fn distance(x:(i64,i64), y: (i64,i64)) -> i64{
    (x.0 - y.0).abs() + (x.1 - y.1).abs()
}


#[fastout]
fn run() {
    // // 計測開始
    // const TL: f64 = 1.9;
    // get_time();

    let input = read_input();
    // let (order_list, route) = fundamental_solve(&input);
    // let (order_list, route) = solve_sat1(&input);
    let (order_list, route) = solve_sat4(&input);
    print_ans(&order_list, &route);
}

fn print_ans(order_list: &Vec<usize>, route: &Vec<(i64,i64)>){
    print!("{} ", order_list.len());
    for &x in order_list{
        print!("{} ", x+1)
    }
    println!();
    print!("{} ", route.len());
    for &(x,y) in route{
        print!("{} {} ", x, y)
    }
    println!()
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
    pub K: usize,
    pub H: usize,
    pub W: usize,
    pub ABCD: Vec<(i64,i64,i64,i64)>,
    pub atcoder: (i64, i64),
}

// read_input
fn read_input() -> Input {
    let N: usize = 1000;
    input!{
        ABCD: [(i64,i64,i64,i64); N],
    }
    let K: usize = 50;
    let H = 800;
    let W = 800;
    let atcoder = (400, 400);
	Input {N, K, H, W, ABCD, atcoder}
}
