#![allow(non_snake_case, unused)]
use rand::prelude::*;

pub trait SetMinMax {
	fn setmin(&mut self, v: Self) -> bool;
	fn setmax(&mut self, v: Self) -> bool;
}
impl<T> SetMinMax for T where T: PartialOrd {
	fn setmin(&mut self, v: T) -> bool {
		*self > v && { *self = v; true }
	}
	fn setmax(&mut self, v: T) -> bool {
		*self < v && { *self = v; true }
	}
}

#[macro_export]
#[allow(unused)]
macro_rules! mat {
	($($e:expr),*) => { Vec::from(vec![$($e),*]) };
	($($e:expr,)*) => { Vec::from(vec![$($e),*]) };
	($e:expr; $d:expr) => { Vec::from(vec![$e; $d]) };
	($e:expr; $d:expr $(; $ds:expr)+) => { Vec::from(vec![mat![$e $(; $ds)*]; $d]) };
}

pub fn readln() -> String {
	let mut line = String::new();
	::std::io::stdin().read_line(&mut line).unwrap_or_else(|e| panic!("{}", e));
	line
}

macro_rules! read {
	($($t:tt),*; $n:expr) => {{
		let stdin = ::std::io::stdin();
		let ret = ::std::io::BufRead::lines(stdin.lock()).take($n).map(|line| {
			let line = line.unwrap();
			let mut it = line.split_whitespace();
			_read!(it; $($t),*)
		}).collect::<Vec<_>>();
		ret
	}};
	($($t:tt),*) => {{
		let line = readln();
		let mut it = line.split_whitespace();
		_read!(it; $($t),*)
	}};
}

macro_rules! _read {
	($it:ident; [char]) => {
		_read!($it; String).chars().collect::<Vec<_>>()
	};
	($it:ident; [u8]) => {
		Vec::from(_read!($it; String).into_bytes())
	};
	($it:ident; usize1) => {
		$it.next().unwrap_or_else(|| panic!("input mismatch")).parse::<usize>().unwrap_or_else(|e| panic!("{}", e)) - 1
	};
	($it:ident; [usize1]) => {
		$it.map(|s| s.parse::<usize>().unwrap_or_else(|e| panic!("{}", e)) - 1).collect::<Vec<_>>()
	};
	($it:ident; [$t:ty]) => {
		$it.map(|s| s.parse::<$t>().unwrap_or_else(|e| panic!("{}", e))).collect::<Vec<_>>()
	};
	($it:ident; $t:ty) => {
		$it.next().unwrap_or_else(|| panic!("input mismatch")).parse::<$t>().unwrap_or_else(|e| panic!("{}", e))
	};
	($it:ident; $($t:tt),+) => {
		($(_read!($it; $t)),*)
	};
}

pub fn main() {
	let _ = ::std::thread::Builder::new().name("run".to_string()).stack_size(32 * 1024 * 1024).spawn(run).unwrap().join();
}

pub fn get_time() -> f64 {
	static mut STIME: f64 = -1.0;
	let t = std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).unwrap();
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
	pub D: usize,
	pub s: Vec<Vec<i64>>,
	pub c: Vec<i64>
}

fn read_input() -> Input {
	let D = read!(usize);
	let c = read!([i64]);
	let s = read!([i64]; D);
	Input { D, s, c }
}

// スコアの計算
pub fn compute_score(input: &Input, out: &Vec<usize>) -> i64 {
	let mut score = 0;
	let mut last = vec![0; 26];
	for d in 0..out.len() {
		last[out[d]] = d + 1;
		for i in 0..26 {
			score -= (d + 1 - last[i]) as i64 * input.c[i];
		}
		score += input.s[d][out[d]];
	}
	score
}

fn cost(a: usize, b: usize) -> i64 {
	let d = b - a;
	(d * (d - 1) / 2) as i64
}

struct State {
	out: Vec<usize>,
	score: i64,
	prev: Vec<Vec<usize>>,
	next: Vec<Vec<usize>>,
}

impl State {
	fn new(input: &Input, out: Vec<usize>) -> State {
		let mut prev = mat![!0; 26; input.D + 1];
		let mut next = mat![input.D; 26; input.D + 1];
		for d in 0..input.D {
			for i in 0..26 {
				prev[i][d + 1] = prev[i][d];
			}
			prev[out[d]][d + 1] = d;
		}
		for d in (0..input.D).rev() {
			for i in 0..26 {
				next[i][d] = next[i][d + 1];
			}
			next[out[d]][d] = d;
		}
		let score = compute_score(&input, &out);
		State { out, score, prev, next }
	}
	fn try_shift(&self, input: &Input, d: usize, d2: usize) -> i64 {
		let i = self.out[d];
		let prev = self.prev[i][d];
		let next = self.next[i][d + 1];
		let before = input.s[d][i] - input.c[i] * (cost(prev, d) + cost(d, next));
		let after = if d2 == !0 {
			-input.c[i] * cost(prev, next)
		} else {
			input.s[d2][i] - input.c[i] * (cost(prev, d2) + cost(d2, next))
		};
		after - before
	}
	fn try_insert(&self, input: &Input, d: usize, i: usize) -> i64 {
		let prev = self.prev[i][d];
		let next = self.next[i][d + 1];
		let before = -input.c[i] * cost(prev, next);
		let after = input.s[d][i] - input.c[i] * (cost(prev, d) + cost(d, next));
		after - before
	}
	fn update(&mut self, i: usize, prev: usize, d2: usize, next: usize) {
		for d in prev+1..=d2 {
			self.prev[i][d] = prev;
			self.next[i][d] = d2;
		}
		for d in d2+1..=next {
			self.prev[i][d] = d2;
			self.next[i][d] = next;
		}
	}
	fn change(&mut self, d: usize, i: usize) {
		let j = self.out[d];
		let (prev1, next1) = (self.prev[i][d], self.next[i][d + 1]);
		let (prev2, next2) = (self.prev[j][d], self.next[j][d + 1]);
		self.out[d] = i;
		self.update(i, prev1, d, next1);
		for d in prev2+1..=next2 {
			self.prev[j][d] = prev2;
			self.next[j][d] = next2;
		}
	}
}

fn dfs(input: &Input, state: &mut State, d: usize, diff: i64, diff0: i64, used: &mut Vec<bool>, s: usize, depth: usize) -> bool {
	if d != s {
		if s == !0 {
			let diff = diff + diff0 + state.try_shift(input, d, !0);
			if diff > 0 {
				state.score += diff;
				return true;
			}
		} else {
			let i = state.out[d];
			if state.prev[i][d] + 1 <= s && s < state.next[i][d + 1] {
				let diff = diff + state.try_shift(input, d, s);
				if diff > 0 {
					state.score += diff;
					state.change(s, i);
					return true;
				}
			}
		}
	}
	let i = state.out[d];
	let prev = state.prev[i][d];
	let next = state.next[i][d + 1];
	if depth < 2 {
		for d2 in prev+1..next {
			if used[state.out[d2]] {
				continue;
			}
			let diff = diff + state.try_shift(input, d, d2);
			if diff > 0 {
				let j = state.out[d2];
				used[j] = true;
				let ok = dfs(input, state, d2, diff, diff0, used, s, depth + 1);
				used[j] = false;
				if ok {
					state.change(d2, i);
					return true;
				}
			}
		}
	} else if s != !0 {
		let mut max_diff = 0;
		let mut max_d2 = !0;
		for d2 in prev+1..next {
			if used[state.out[d2]] {
				continue;
			}
			if max_diff.setmax(diff + state.try_shift(input, d, d2)) {
				max_d2 = d2;
			}
		}
		if max_diff > 0 {
			used[state.out[max_d2]] = true;
			let ok = dfs(input, state, max_d2, max_diff, diff0, used, s, depth + 1);
			used[state.out[max_d2]] = false;
			if ok {
				state.change(max_d2, i);
				return true;
			}
		}
	}
	false
}

fn solve(input: &Input) -> Vec<usize> {
	const T0: f64 = 2e3;
	const T1: f64 = 2e2;
	const TL: f64 = 1.95;
	let mut rng = rand_pcg::Pcg64Mcg::new(890482);
	let mut state = State::new(input, (0..input.D).map(|_| rng.gen_range(0, 26)).collect());
	let mut used = vec![false; 26];
	let mut cnt = 0;
	let mut best_score = state.score;
	let mut best = state.out.clone();
	loop {
		let t = get_time() / TL;
		if t >= 0.9 {
			break;
		}
		let T = T0.powf(1.0 - t) * T1.powf(t);
		let add = (-T * rng.gen::<f64>().ln()) as i64;
		cnt += 1;
		if rng.gen_bool(0.5) {
			let d = rng.gen_range(0, input.D);
			let i = rng.gen_range(0, 26);
			if state.out[d] == i {
				continue;
			}
			let j = state.out[d];
			let diff = state.try_insert(input, d, i);
			used[i] = true;
			used[j] = true;
			if dfs(input, &mut state, d, add + diff / 4, diff - diff / 4, &mut used, !0, 0) {
				state.change(d, i);
				state.score -= add;
			}
			used[i] = false;
			used[j] = false;
		} else {
			let s = rng.gen_range(0, input.D);
			let i = state.out[s];
			used[i] = true;
			if dfs(input, &mut state, s, add, 0, &mut used, s, 0) {
				state.score -= add;
			}
			used[i] = false;
		}
		if best_score.setmax(state.score) {
			best = state.out.clone();
			eprintln!("Time: {:.3}, Score: {}", get_time(), best_score);
		}
	}
	eprintln!("Iter = {}", cnt);
	best
}

fn run() {
	get_time();
	let input = read_input();
	let out = solve(&input);
	eprintln!("Time = {:.3}", get_time());
	eprintln!("Score = {}", compute_score(&input, &out));
	for i in 0..input.D {
		println!("{}", out[i] + 1);
	}
}
