// -*- coding:utf-8-unix -*-
#![allow(non_snake_case)]

// use proconio::input;
// use rand::seq::SliceRandom;
// use rand::{thread_rng, Rng};
use std::cmp::{min, max};

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


fn mean_solve(){
    let N: usize = 1000;
    let (r, w) = (std::io::stdin(), std::io::stdout());
    let mut sc = IO::new(r.lock(), w.lock());
    let mean = 3500;
    // let mean = 0;
    let H: usize = 30;
    let W: usize = 30;
    let initial_check = 10;
    let K = 300;
    let k = 1;
    let straight_apply = 100;
    let straight_threshold = 0.2;
    let disruptive_threshold = 0.35;
    let disruptive_cost = 20.0;
    let mut unfixR: Vec<Vec<bool>> = vec![vec![true;W-1]; H];
    let mut unfixC: Vec<Vec<bool>> = vec![vec![true;W]; H-1];
    let mut R: Vec<Vec<usize>> = vec![vec![mean;W-1]; H];
    let mut C: Vec<Vec<usize>> = vec![vec![mean;W]; H-1];
    for i in 0..N{
        let si: usize = sc.read();
        let sj: usize = sc.read();
        let ti: usize = sc.read();
        let tj: usize = sc.read();
        let (prediction, path) = {
            if ((si == ti) || (sj == tj)) && (i < straight_apply){
                straight_path(si, sj, ti, tj, &R, &C)
            }else{
                dijkstra(si, sj, ti, tj, H, W, &R, &C)
            }
        };
        // eprintln!("{} {} {} {} {:?}", si, sj, ti, tj, &path);
        print_ans(&path);
        let real_distance: usize = sc.read();
        let new_cost = real_distance/(path.len()-1);
        let relative_error = ((max(prediction, real_distance) - min(prediction, real_distance)) as f64)/(real_distance as f64);
        if i < initial_check{
            static_update_path_cost(N, k, &path, new_cost, &mut R, &mut C);
            if i == initial_check - 1{
                smoothing_path_cost(i,&mut R, &mut C, &mut unfixR, &mut unfixC);
            }
            continue;
        }
        if ((si == ti) || (sj == tj)) && (i < straight_apply) && (relative_error > straight_threshold){
            weighted_update_path_cost(1, 0, &path, new_cost, &mut R, &mut C);
        }else{

            if relative_error > disruptive_threshold{
                let cost_more = (disruptive_cost*relative_error).floor() as usize;
                // if prediction < real_distance{
                //     cost_more = 0;
                // }
                disruptive_update_path_cost(N,i,&path, new_cost+cost_more, &mut R, &mut C);
                smoothing_path_cost(i,&mut R, &mut C, &mut unfixR, &mut unfixC);
            }else{
                dynamical_update_path_cost(N,i,&path, new_cost, &mut R, &mut C);
                if i < K{
                    if i%k == 0{
                        smoothing_path_cost(i,&mut R, &mut C, &mut unfixR, &mut unfixC);
                    }
                }
            }
        }
        // for i in 0..H{
        //     for j in 0..(W-1){
        //         eprint!("{} ", R[i][j])
        //     }
        //     eprintln!();
        // }
        // dynamical_update_path_cost(N,i,&path, new_cost, &mut R, &mut C);
    }
}

fn straight_path(si: usize, sj: usize, ti: usize, tj:usize, R: &Vec<Vec<usize>>, C: &Vec<Vec<usize>>) -> (usize,Vec<(usize, usize)>){
    let path: Vec<(usize, usize)> = {
        if si == ti{
            if sj < tj{
                (sj..=tj).map(|x| (si, x)).collect()
            }else{
                (tj..=sj).rev().map(|x| (si, x)).collect()
            }
        }else{
            if si < ti{
                (si..=ti).map(|x| (x, ti)).collect()
            }else{
                (ti..=si).rev().map(|x| (x, ti)).collect()
            }
        }
    };
    let (mut vi, mut vj) = path[0];
    let mut path_cost = 0;
    for i in 1..path.len(){
        let (wi, wj) = path[i];
        if vi == wi{
            path_cost += R[vi][min(vj,wj)];
        }else{
            path_cost += C[min(vi, wi)][vj];
        }
        vi = wi;
        vj = wj;
    }
    (path_cost, path)
}

#[allow(dead_code)]
fn is_straight(path: &Vec<(usize, usize)>) -> bool{
    let row = {
        if path[0].0 == path[1].0{
            true
        }else{
            false
        }
    };
    for i in 1..(path.len()-1){
        if path[i].0 == path[i+1].0{
            if !row{
                return false
            }
        }else{
            if row{
                return false
            }
        }
    }
    true
}

#[allow(dead_code)]
fn initialize_cost(H: usize, W: usize, m: usize, M: usize) -> Vec<Vec<usize>>{
    let mut ret: Vec<Vec<usize>> = vec![vec![0;W]; H];
    let h = H-1;
    let w = W-1;
    let f = h/2;
    for i in 0..H{
        for j in 0..W{
            let p = min(min(i-0, h-i), min(j-0,w-j));
            ret[i][j] = m + (M-m)*p/f;
        }
    }
    ret
}

fn smoothing_path_cost(k: usize,R: &mut Vec<Vec<usize>>, C: &mut Vec<Vec<usize>>, unfixR: &mut Vec<Vec<bool>>, unfixC: &mut Vec<Vec<bool>>){
    let mut m = 1;
    let mut n = 1;

    // if k >= 100{
    //     m = 1;
    //     n = 1;
    // }
    // weighted_smoothing_path_cost(m, n, R, C);
    weighted_smoothing_path_cost(m, n, R, C, unfixR, unfixC);

}

#[allow(dead_code)]
fn weighted_smoothing_path_cost(m: usize, n: usize, R: &mut Vec<Vec<usize>>, C: &mut Vec<Vec<usize>>, unfixR: &mut Vec<Vec<bool>>, unfixC: &mut Vec<Vec<bool>>){
    let mn = m+n;
        for i in 0..R.len(){
        let mut row_sum = 0;
        for j in 0..R[i].len(){
            row_sum += R[i][j];
        }
        let row_mean = row_sum / R[i].len();
            for j in 0..R[i].len(){
                if unfixR[i][j]{
                    R[i][j] = (m*row_mean + n*R[i][j])/mn;
                }
        }
    }
    for j in 0..C[0].len(){
        let mut column_sum = 0;
        for i in 0..C.len(){
            column_sum += C[i][j];
        }
        let column_mean = column_sum / C.len();
        for i in 0..C.len(){
            if unfixC[i][j]{
                C[i][j] = (m*column_mean + n*C[i][j])/mn;
            }
        }
    }
}

#[allow(dead_code)]
fn weighted_smoothing_path_cost_with_median(m: usize, n: usize, R: &mut Vec<Vec<usize>>, C: &mut Vec<Vec<usize>>){
    let mn = m+n;
    for i in 0..R.len(){
        let mut row: Vec<usize> = R[i].clone();
        row.sort();
        let row_median = row[(row.len()-1)/2];
        for j in 0..R[i].len(){
            R[i][j] = (m*row_median + n*R[i][j])/mn;
        }
    }
    for j in 0..C[0].len(){
        let mut column: Vec<usize> = Vec::new();
        for i in 0..C.len(){
            column.push(C[i][j]);
        }
        column.sort();
        let column_median = column[(column.len()-1)/2];
        for i in 0..C.len(){
            C[i][j] = (m*column_median + n*C[i][j])/mn;
        }
    }
}


fn disruptive_update_path_cost(N: usize, k: usize, path: &Vec<(usize, usize)>,new_cost: usize, R: &mut Vec<Vec<usize>>, C: &mut Vec<Vec<usize>>){
    let m = 10;
    let n = 1;
    weighted_update_path_cost(m, n, path, new_cost, R, C)
}


#[allow(dead_code)]
fn static_update_path_cost(N: usize, k: usize, path: &Vec<(usize, usize)>,new_cost: usize, R: &mut Vec<Vec<usize>>, C: &mut Vec<Vec<usize>>){
    let m = 3;
    let n = 2;
    weighted_update_path_cost(m, n, path, new_cost, R, C)
}


// 平均取ってみる?
fn dynamical_update_path_cost(N: usize, k: usize, path: &Vec<(usize, usize)>,new_cost: usize, R: &mut Vec<Vec<usize>>, C: &mut Vec<Vec<usize>>){
    // let m = N+k;
    // let n = N*2+N-k;
    // // let m = 1;
    // // let n = 3;
    // let mn = m + n;
    let mut m = 1;
    let mut n = 1;
    if k >= N/10{
        m = 1;
        n = 2;
    }
    weighted_update_path_cost(m, n, path, new_cost, R, C);
    // let mn = m+n;
    // for i in 1..path.len(){
    //     let (wi, wj) = path[i];
    //     if vi == wi{
    //         R[vi][min(vj,wj)] = (new_cost*m + R[vi][min(vj,wj)]*n)/mn;
    //     }else{
    //         C[min(vi,wi)][vj] = (new_cost*m + C[min(vi,wi)][vj]*n)/mn;
    //     }
    //     vi = wi;
    //     vj = wj;
    // }
    
}

fn weighted_update_path_cost(m: usize, n: usize, path: &Vec<(usize, usize)>,new_cost: usize, R: &mut Vec<Vec<usize>>, C: &mut Vec<Vec<usize>>){
    let (mut vi, mut vj) = path[0];
    let mn = m+n;
    for i in 1..path.len(){
        let (wi, wj) = path[i];
        if vi == wi{
            R[vi][min(vj,wj)] = (new_cost*m + R[vi][min(vj,wj)]*n)/mn;
        }else{
            C[min(vi,wi)][vj] = (new_cost*m + C[min(vi,wi)][vj]*n)/mn;
        }
        vi = wi;
        vj = wj;
    }
    
}

fn print_ans(path: &Vec<(usize, usize)>){
    let mut ans = Vec::new();
    let (mut vi, mut vj) = path[0];
    for i in 1..path.len(){
        let (wi, wj) = path[i];
        if vi == wi{
            if vj < wj{
                ans.push(b'R')
            }else{
                ans.push(b'L')
            }
        }else{
            if vi < wi{
                ans.push(b'D')
            }else{
                ans.push(b'U')
            }
        }
        vi = wi;
        vj = wj;
    }
    // eprintln!("{:?}", path);
    // eprintln!("{:?}", ans);
    println!("{}", ans.iter().map(|&s| s as char).collect::<String>())
}

use std::{cmp::Reverse, collections::BinaryHeap};
fn dijkstra(si: usize, sj: usize, ti: usize, tj: usize,H: usize, W: usize, R: &Vec<Vec<usize>>, C: &Vec<Vec<usize>>) -> (usize, Vec<(usize,usize)>){
    let mut queue = BinaryHeap::new();
    let mut vertex = vec![vec![std::usize::MAX; W]; H];
    vertex[si][sj] = 0;
    let mut visited = vec![vec![false; W]; H];
    let mut prev = vec![vec![(0, 0); W]; H];
    queue.push((Reverse(0), (si,sj)));
    // eprintln!("dijkstra");
    while let Some((Reverse(_), (vi, vj))) = queue.pop(){
        if visited[vi][vj]{
            continue;
        }
        if (vi == ti) && (vj == tj){break}
        visited[vi][vj] = true;
        if 0 < vi{
            if (!visited[vi-1][vj]) && (vertex[vi-1][vj] > vertex[vi][vj] + C[vi-1][vj]){
                vertex[vi-1][vj] = vertex[vi][vj] + C[vi-1][vj];
                prev[vi-1][vj] = (vi, vj);
                queue.push((Reverse(vertex[vi-1][vj]), (vi-1, vj)))
            }
        }
        if vi < H-1{
            if (!visited[vi+1][vj]) && (vertex[vi+1][vj] > vertex[vi][vj] + C[vi][vj]){
                vertex[vi+1][vj] = vertex[vi][vj] + C[vi][vj];
                prev[vi+1][vj] = (vi, vj);
                queue.push((Reverse(vertex[vi+1][vj]), (vi+1, vj)))
            }
        }
        if 0 < vj{
            if (!visited[vi][vj-1]) && (vertex[vi][vj-1] > vertex[vi][vj] + R[vi][vj-1]){
                vertex[vi][vj-1] = vertex[vi][vj] + R[vi][vj-1];
                prev[vi][vj-1] = (vi, vj);
                queue.push((Reverse(vertex[vi][vj-1]), (vi, vj-1)))
            }
        }
        if vj < W-1{
            if (!visited[vi][vj+1]) && (vertex[vi][vj+1] > vertex[vi][vj] + R[vi][vj]){
                vertex[vi][vj+1] = vertex[vi][vj] + R[vi][vj];
                prev[vi][vj+1] = (vi, vj);
                queue.push((Reverse(vertex[vi][vj+1]), (vi, vj+1)))
            }
        }
    }
    let mut ret = Vec::new();
    let mut vi = ti;
    let mut vj = tj;
    ret.push((vi,vj));
    loop{
        let (_wi, _wj) = prev[vi][vj];
        vi = _wi;
        vj = _wj;
        ret.push((vi, vj));
        if (vi == si) && (vj == sj){
            break
        }
    }
    ret.reverse();
    (vertex[ti][tj], ret)
}

fn run() {
    // // 計測開始
    // const TL: f64 = 4.9;
    get_time();
    // let T0: f64 = 50.0;
    // let T1: f64 = 35.0;

    // loop {
    //     let t = get_time()/TL;
    //     // eprintln!("{}", get_time());
    //     if t >= 1.0{
    //         break
    //     }
    // }
    // println!("answer");
    mean_solve();
}

#[allow(dead_code)]
fn elemental_solve(){
    let N: usize = 1000;
    let (r, w) = (std::io::stdin(), std::io::stdout());
    let mut sc = IO::new(r.lock(), w.lock());
    for _ in 0..N{
        let mut u = 0;
        let mut d = 0;
        let mut l = 0;
        let mut r = 0;
        let si: usize = sc.read();
        let sj: usize = sc.read();
        let ti: usize = sc.read();
        let tj: usize = sc.read();

        if si < ti{
            d = ti - si;
        }else{
            u = si - ti;
        }
        if sj < tj{
            r = tj - sj;
        }else{
            l = sj - tj;
        }
        // eprintln!("{} {} {} {}", u, d, l, r);
        print_elemental_answer(u, d, l, r);
        let _length: usize = sc.read();
    }
    
}

#[allow(dead_code)]
fn print_elemental_answer(u: usize, d: usize, l: usize, r: usize){
    let mut ans: Vec<u8> = Vec::new();
    for _ in 0..u{
        ans.push(b'U');
    }
    for _ in 0..d{
        ans.push(b'D');
    }
    for _ in 0..l{
        ans.push(b'L');
    }
    for _ in 0..r{
        ans.push(b'R');
    }
    println!("{}", ans.iter().map(|&s| s as char).collect::<String>());
    // eprintln!("{}", get_time());
}




// pub fn score(input: &Input, out: &Vec<Rect>) -> i64 {
//     unimplemented!()
// }

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
