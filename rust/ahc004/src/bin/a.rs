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

use proconio::marker::Bytes;
use proconio::{fastout, input};
use rand::Rng;
// use proconio::marker::Bytes;

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
    pub S: Vec<Vec<u8>>,
}

// read_input
fn read_input() -> Input {
    input!{
        N: usize,
        M: usize,
        S: [Bytes; M],
    }

	Input {N, M, S}
}

#[allow(dead_code)]
fn all_dots(input: &Input) -> Vec<Vec<u8>>{
    vec![vec![b'.';input.N]; input.N]
}

#[allow(dead_code)]
fn random_dna(input: &Input) -> Vec<Vec<u8>>{
    let mut ret = vec![vec![b'.';input.N]; input.N];
    let mut rng = rand::thread_rng();
    for i in 0..input.N{
        for j in 0..input.N{
            ret[i][j] = b'A' + rng.gen_range(0, 8);
        }
    }
    ret
}

fn turn_dna(input: &Input) -> Vec<Vec<u8>>{
    let mut ret = vec![vec![b'.';input.N]; input.N];
    let mut S = input.S.clone();
    S.sort_by(|a,b| a.len().cmp(&b.len()));
    let mut count = vec![0; input.N];
    'sub: for m in 0..input.M{
        if exist(&ret, &S[m]){continue;}
        for i in 0..input.N{
            if count[i] + S[m].len() < input.N{
                dna_change_based_on_s(&mut ret, input, (m,i,count[i],1));
                count[i] += S[m].len();
                break
            }else{
                if i == input.N-1{
                    break 'sub
                }
            }
        }
    }
    let mut rng = rand::thread_rng();
    for i in 0..input.N{
        for j in 0..input.N{
            if ret[i][j] == b'.'{
                ret[i][j] = b'A' + rng.gen_range(0, 8);
            }
        }
    }
    ret
}

fn initial_dna(input: &Input) -> Vec<Vec<u8>>{
    turn_dna(input)
}


fn annealing(input: &Input, dna: &mut Vec<Vec<u8>>){
    let mut score = get_score(input, dna);
    const TL: f64 = 2.9;
    loop{
        let t = get_time()/TL;
        // eprintln!("{}", get_time());
        if t >= 1.0{
            break
        }
        let (new_dna, mijd) = random_change(input, dna);
        let new_score = get_score(input, &new_dna);
        if score < new_score{
            dna_change_based_on_s(dna, input, mijd);
            score = new_score;
        }
    }
}

fn random_change(input: &Input, dna: &Vec<Vec<u8>>) -> (Vec<Vec<u8>>, (usize, usize, usize, usize)){
    let mut ret = dna.clone();
    let mut rng = rand::thread_rng();
    let m = rng.gen_range(0, input.M);
    let i = rng.gen_range(0, input.N);
    let j = rng.gen_range(0, input.N);
    let d = rng.gen_range(0, 2);
    let mijd = (m,i,j,d);
    dna_change_based_on_s(&mut ret, input, mijd);
    (ret, mijd)
}

fn dna_change_based_on_s(dna: &mut Vec<Vec<u8>>, input: &Input,  mijd: (usize,usize, usize,usize)){
    let (m, i, j, d) = mijd;
    // 縦
    if d == 0{
        for k in 0..input.S[m].len(){
            dna[(i+k)%input.N][j] = input.S[m][k];
        }
    }else{
        for k in 0..input.S[m].len(){
            dna[i][(j+k)%input.N] = input.S[m][k];
        }
    }
}

#[fastout]
fn run() {
    // 計測開始
    get_time();
    let input = read_input();
    let mut dna = initial_dna(&input);
    // for i in 0..input.N{
    //     eprintln!("{}", dna[i].iter().map(|&s| s as char).collect::<String>());
    // }
    // eprintln!(" initialized {}", get_time());
    // for i in 0..input.N{
    //     eprintln!("{}", dna[i].len());
    //     eprintln!("{}", dna[i].iter().map(|&s| s as char).collect::<String>().len());
    // }
    annealing(&input, &mut dna);

    // 最後に使ってないものを.に書き換える?c=Mってレアケースだしな。
    for i in 0..input.N{
        println!("{}", dna[i].iter().map(|&s| s as char).collect::<String>());
    }
}

fn get_score(input: &Input, dna: &Vec<Vec<u8>>) -> u64{
    let mut c = 0;
    for i in 0..input.M{
        if exist(dna, &input.S[i]){
            c += 1;
        }
    }
    let f: f64 = 100000000.0;
    if c < input.M {
        (f*(c as f64)/(input.M as f64)).round() as u64
    }else{
        let dot = count_dot(dna);
        (f*((2*input.N*input.N) as f64)/((2*input.N*input.N - dot) as f64)).round() as u64
    }
    
}

fn count_dot(dna: &Vec<Vec<u8>>) -> usize{
    let mut ret = 0;
    let N = dna.len();
    for i in 0..N{
        for j in 0..N{
            if dna[i][j] == b'.'{
                ret += 1;
            }
        }
    }
    ret
}

fn exist(dna: &Vec<Vec<u8>>, sub: &Vec<u8>) -> bool{
    let N = dna.len();
    let K = sub.len();
    for i in 0..N{
        for j in 0..N{
            // 縦
            let mut e = true;
            for k in 0..K{
                if sub[k] != dna[(i+k)%N][j]{
                    e = false;
                    break
                }
            }
            if e{return true}
            // 横
            let mut e = true;
            for k in 0..K{
                if sub[k] != dna[i][(j+k)%N]{
                    e = false;
                    break
                }
            }
            if e{return true}
        }
    }
    false
}
