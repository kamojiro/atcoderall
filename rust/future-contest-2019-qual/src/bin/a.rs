#![allow(non_snake_case)]
// use petgraph::unionfind::UnionFind;
use proconio::{input,fastout};
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
	pub id: usize,
	pub N: usize,
	pub K: usize,
	// The colors are represented by 1..=K
	pub S_ij: Vec<Vec<usize>>,
}

// read_input
fn read_input() -> Input {
	input! {
		id: usize,
		N: usize,
		K: usize,
		S_lines: [String; N],
	}
	let mut S_ij = Vec::new();
	for i in 0..N {
		let S_oneline = S_lines[i].as_bytes();
		let mut S_line = Vec::with_capacity(N);
		for j in 0..N {
			S_line.push((S_oneline[j] - b'0') as usize);
		}
		S_ij.push(S_line);
	}
	Input { id, N, K, S_ij }
}

fn solve(input:&Input) -> Vec<usize>{
    let ans = vec![0; 3];
    ans
}

#[fastout]
fn run() {
	// 計測開始
	get_time();
	let input = read_input();
    let out = solve(&input);
    for v in 0..out.len(){
        println!("{}", v);
    }
}
