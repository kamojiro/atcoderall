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

pub mod mcf {
	
	use crate::*;
	
	#[derive(Copy, Clone, Debug)]
	pub struct E {
		pub to: usize,
		pub cap: i64,
		pub init: i64,
		pub cost: i64,
		pub rev: usize
	}
	
	#[derive(Clone, Debug)]
	pub struct Graph {
		pub es: Vec<Vec<E>>,
		pub ex: Vec<i64>,
		pub p: Vec<i64>,
		iter: Vec<usize>
	}
	
	impl Graph {
		pub fn new(n: usize) -> Graph {
			Graph { es: vec![vec![]; n], ex: vec![0; n], p: vec![0; n], iter: vec![0; n] }
		}
		pub fn add(&mut self, v: usize, to: usize, cap: i64, cost: i64) {
			let (fwd, rev) = (self.es[v].len(), self.es[to].len());
			self.es[v].push(E { to: to, cap: cap, init: cap, cost: cost, rev: rev });
			self.es[to].push(E { to: v, cap: 0, init: 0, cost: -cost, rev: fwd });
		}
		fn is_admissible(&self, v: usize, e: &E) -> bool {
			e.cap > 0 && e.cost + self.p[v] - self.p[e.to] < 0
		}
		/// Compute minimum cost circulation.
		/// Return whether there is a flow satisfying the demand constraints.
		/// flow(e) = init(e) - cap(e).
		/// For solving min cost s-t flow of value F, set ex(s)=F and ex(t)=-F.
		/// For every vertex, the total capacity of its incident edges must be fit in i64.
		/// Dual: minimize \sum_v ex(v)p(v) + \sum_{uv} cap(e) max(0, -cost(uv) - p(u) + p(v)).
		/// O(V^2 E log VC), where C=max(cost(e)). When cap=1, O(V E log VC).
		pub fn solve(&mut self) -> bool {
			let n = self.es.len();
			let mut eps = 0;
			for v in &mut self.es {
				for e in v {
					e.cost *= n as i64;
					eps.setmax(e.cost);
				}
			}
			let mut stack = vec![];
			let mut visit = vec![false; n];
			let mut ok = self.ex.iter().all(|&ex| ex == 0);
			'refine: loop {
				eps = (eps / 8).max(1);
				if ok && self.fitting() {
					break;
				}
				for v in 0..n {
					for i in 0..self.es[v].len() {
						let e = self.es[v][i];
						if self.is_admissible(v, &e) {
							self.ex[e.to] += e.cap;
							self.ex[v] -= e.cap;
							self.es[e.to][e.rev].cap += e.cap;
							self.es[v][i].cap = 0;
						}
					}
				}
				loop {
					for v in 0..n {
						self.iter[v] = 0;
						if self.ex[v] > 0 {
							visit[v] = true;
							stack.push(v);
						} else {
							visit[v] = false;
						}
					}
					if stack.len() == 0 { break }
					while let Some(v) = stack.pop() {
						for e in &self.es[v] {
							if !visit[e.to] && self.is_admissible(v, e) {
								visit[e.to] = true;
								stack.push(e.to);
							}
						}
					}
					if (0..n).filter(|&v| visit[v]).flat_map(|v| self.es[v].iter()).all(|e| e.cap <= 0 || visit[e.to]) {
						assert!(!ok);
						break 'refine;
					}
					for v in (0..n).filter(|&v| visit[v]) { self.p[v] -= eps }
					for v in 0..n {
						while self.ex[v] > 0 {
							let f = self.dfs(v, self.ex[v]);
							if f == 0 { break }
							else { self.ex[v] -= f }
						}
					}
				}
				ok = true;
			}
			for v in &mut self.es {
				for e in v {
					e.cost /= n as i64;
				}
			}
			ok
		}
		fn dfs(&mut self, v: usize, f: i64) -> i64 {
			if self.ex[v] < 0 {
				let d = ::std::cmp::min(f, -self.ex[v]);
				self.ex[v] += d;
				return d;
			}
			while self.iter[v] < self.es[v].len() {
				let e = self.es[v][self.iter[v]];
				if self.is_admissible(v, &e) {
					let d = self.dfs(e.to, ::std::cmp::min(f, e.cap));
					if d > 0 {
						self.es[v][self.iter[v]].cap -= d;
						self.es[e.to][e.rev].cap += d;
						return d;
					}
				}
				self.iter[v] += 1;
			}
			0
		}
		fn fitting(&mut self) -> bool {
			let n = self.es.len();
			let mut d: Vec<i64> = self.p.iter().map(|&a| a / (n as i64)).collect(); // p must be non-positive.
			let mut d2: Vec<i64> = (0..n).map(|v| d[v] * (n as i64) - self.p[v] + 1).collect();
			let mut fixed = vec![false; n];
			let mut que = ::std::collections::BinaryHeap::new();
			for v in 0..n {
				que.push((-d2[v], v))
			}
			while let Some((_, v)) = que.pop() {
				if fixed[v] { continue }
				fixed[v] = true;
				for e in &self.es[v] {
					if e.cap > 0 && { let tmp = d2[v] + e.cost + self.p[v] - self.p[e.to] + 1; d2[e.to].setmin(tmp) } {
						if fixed[e.to] {
							return false;
						}
						d[e.to] = d[v] + e.cost / (n as i64);
						que.push((-d2[e.to], e.to));
					}
				}
			}
			self.p = d;
			true
		}
		pub fn val(&self) -> i64 {
			let mut tot = 0;
			for v in &self.es {
				for e in v {
					if e.cap < e.init {
						tot += (e.init - e.cap) * e.cost;
					}
				}
			}
			tot
		}
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

fn compute_score(input: &Input, out: &Vec<usize>) -> i64 {
	assert_eq!(out.len(), input.D);
	let mut score = 1000000;
	let mut last = vec![0; 26];
	for d in 0..input.D {
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
	ds: Vec<Vec<usize>>,
}

impl State {
	fn new(input: &Input, out: Vec<usize>) -> State {
		let mut ds = vec![vec![]; 26];
		for d in 0..input.D {
			ds[out[d]].push(d + 1);
		}
		let score = compute_score(&input, &out);
		State { out, score, ds }
	}
	fn change(&mut self, input: &Input, d: usize, new_i: usize) {
		let old_i = self.out[d];
		let p = self.ds[old_i].iter().position(|a| *a == d + 1).unwrap();
		let prev = self.ds[old_i].get(p - 1).cloned().unwrap_or(0);
		let next = self.ds[old_i].get(p + 1).cloned().unwrap_or(input.D + 1);
		self.ds[old_i].remove(p);
		self.score += (cost(prev, d + 1) + cost(d + 1, next) - cost(prev, next)) * input.c[old_i];
		let p = self.ds[new_i].iter().position(|a| *a > d + 1).unwrap_or(self.ds[new_i].len());
		let prev = self.ds[new_i].get(p - 1).cloned().unwrap_or(0);
		let next = self.ds[new_i].get(p).cloned().unwrap_or(input.D + 1);
		self.ds[new_i].insert(p, d + 1);
		self.score -= (cost(prev, d + 1) + cost(d + 1, next) - cost(prev, next)) * input.c[new_i];
		self.score += input.s[d][new_i] - input.s[d][old_i];
		self.out[d] = new_i;
	}
}

fn solve(input: &Input) -> Vec<usize> {
	const TS: f64 = 2e3;
	const TE: f64 = 6e2;
	const TL: f64 = 1.5;
	let mut rng = rand_pcg::Pcg64Mcg::new(890482);
	let mut state = State::new(input, (0..input.D).map(|_| rng.gen_range(0, 26)).collect());
	let stime = get_time();
	let mut cnt = 0;
	let mut T = TS;
	let mut best = state.score;
	let mut best_out = state.out.clone();
	while get_time() - stime < TL {
		cnt += 1;
		if cnt % 100 == 0 {
			let t = (get_time() - stime) / TL;
			T = TS.powf(1.0 - t) * TE.powf(t);
		}
		let old_score = state.score;
		if rng.gen_bool(0.5) {
			let d = rng.gen_range(0, input.D);
			let old = state.out[d];
			state.change(input, d, rng.gen_range(0, 26));
			if old_score > state.score && !rng.gen_bool(f64::exp((state.score - old_score) as f64 / T)) {
				state.change(input, d, old);
			}
		} else {
			let d1 = rng.gen_range(0, input.D - 1);
			let d2 = rng.gen_range(d1 + 1, (d1 + 16).min(input.D));
			let (a, b) = (state.out[d1], state.out[d2]);
			state.change(input, d1, b);
			state.change(input, d2, a);
			if old_score > state.score && !rng.gen_bool(f64::exp((state.score - old_score) as f64 / T)) {
				state.change(input, d1, a);
				state.change(input, d2, b);
			}
		}
		if best.setmax(state.score) {
			eprintln!("time: {:.3}, T: {:.0}, score: {}", get_time(), T, best);
			best_out = state.out.clone();
		}
	}
	eprintln!("Iter = {}", cnt);
	best_out
}

fn improve_flow(input: &Input, out: &mut Vec<usize>) {
	let mut rng = rand_pcg::Pcg64Mcg::new(890482);
	let stime = get_time();
	let mut cnt = 0;
	while get_time() - stime < 0.4 {
		cnt += 1;
		let mut ps = vec![vec![]; 26];
		let mut idx = vec![!0usize; input.D];
		for d in 0..input.D {
			idx[d] = ps[out[d]].len();
			ps[out[d]].push(d);
		}
		let mut del = vec![false; input.D];
		let mut tmp = (0..input.D).collect::<Vec<_>>();
		tmp.shuffle(&mut rng);
		for c in tmp {
			for a in 0..20 {
				for &d in &[c - a, c + a] {
					if d >= input.D || del[d] || idx[d] > 0 && del[ps[out[d]][idx[d] - 1]] || idx[d] + 1 < ps[out[d]].len() && del[ps[out[d]][idx[d] + 1]] {
						continue;
					}
					del[d] = true;
				}
			}
		}
		let mut vs = vec![];
		let mut vid = vec![!0; input.D];
		for d in 0..input.D {
			if del[d] {
				vid[d] = vs.len();
				vs.push(d);
			}
		}
		let mut g = mcf::Graph::new(vs.len() * 2 + 27);
		for v in 0..vs.len() {
			let i = out[vs[v]];
			g.ex[v] = 1;
			g.ex[vs.len() + v] = -1;
			let d = vs[v];
			let prev = *ps[out[d]].get(idx[d] - 1).unwrap_or(&!0);
			let next = *ps[out[d]].get(idx[d] + 1).unwrap_or(&input.D);
			for d in prev+1..next {
				if vid[d] != !0 {
					g.add(v, vs.len() + vid[d], 1, (cost(prev, d) + cost(d, next)) * input.c[i] - input.s[d][i]);
				}
			}
			g.add(v, vs.len() * 2 + 26, 1, cost(prev, next) * input.c[i]);
			for j in 0..26 {
				let p = ps[j].iter().position(|a| *a >= d).unwrap_or(ps[j].len());
				if p < ps[j].len() && del[ps[j][p]] {
					continue;
				}
				if p - 1 < ps[j].len() && del[ps[j][p - 1]] {
					continue;
				}
				let prev = *ps[j].get(p - 1).unwrap_or(&!0);
				let next = *ps[j].get(p).unwrap_or(&input.D);
				g.add(vs.len() * 2 + j, vs.len() + v, 1, (cost(prev, d) + cost(d, next) - cost(prev, next)) * input.c[j] - input.s[d][j]);
			}
		}
		for i in 0..26 {
			g.ex[vs.len() * 2 + i] = 1;
			g.add(vs.len() * 2 + i, vs.len() * 2 + 26, 1, 0);
		}
		g.ex[vs.len() * 2 + 26] = -26;
		g.solve();
		let out_old = out.clone();
		for v in 0..vs.len() {
			for e in &g.es[v] {
				if e.cap < e.init && e.to < vs.len() * 2 {
					out[vs[e.to - vs.len()]] = out_old[vs[v]];
				}
			}
		}
		for i in 0..26 {
			for e in &g.es[vs.len() * 2 + i] {
				if e.cap < e.init && e.to < vs.len() * 2 {
					out[vs[e.to - vs.len()]] = i;
				}
			}
		}
		assert!(compute_score(input, &out_old) <= compute_score(input, &out));
	}
	dbg!(cnt);
}

fn improve_ls(input: &Input, out: &mut Vec<usize>) {
	let mut state = State::new(input, out.clone());
	let mut score = state.score;
	while get_time() < 1.95 {
		let mut ok = false;
		for d in 0..input.D {
			for i in 0..26 {
				let old = state.out[d];
				state.change(input, d, i);
				if score.setmax(state.score) {
					ok = true;
				} else {
					state.change(input, d, old);
				}
			}
			for d2 in d+1..input.D {
				if out[d] == out[d2] {
					break;
				}
				let (a, b) = (state.out[d], state.out[d2]);
				state.change(input, d, b);
				state.change(input, d2, a);
				if score.setmax(state.score) {
					ok = true;
				} else {
					state.change(input, d, a);
					state.change(input, d2, b);
				}
			}
		}
		if !ok {
			break;
		}
	}
	*out = state.out;
}

fn run() {
	get_time();
	let input = read_input();
	let mut out = solve(&input);
	improve_flow(&input, &mut out);
	dbg!(compute_score(&input, &out));
	improve_ls(&input, &mut out);
	eprintln!("Time = {:.3}", get_time());
	eprintln!("Score = {}", compute_score(&input, &out));
	for i in 0..input.D {
		println!("{}", out[i] + 1);
	}
}


#![allow(non_snake_case)]
fn main() {
    let (r, w) = (std::io::stdin(), std::io::stdout());
    let mut sc = IO::new(r.lock(), w.lock());
    //let n: usize = sc.read();
    //let a: Vec<u64> = sc.vec(n);
    //let s = sc.chars();
    //let mut A: Vec<Vec<u64>> = (0..n).map(|_| sc.vec(n)).collect();
    
}

truct IO<R, W: std::io::Write>(R, std::io::BufWriter<W>);

impl<R: std::io::Read, W: std::io::Write> IO<R, W> {
    pub fn new(r: R, w: W) -> Self {
        Self(r, std::io::BufWriter::new(w))
    }
    pub fn write<S: ToString>(&mut self, s: S) {
        use std::io::Write;
        self.1.write(s.to_string().as_bytes()).unwrap();
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
    pub fn vec<T: std::str::FromStr>(&mut self, n: usize) -> Vec<T> {
        (0..n).map(|_| self.read()).collect()
    }
    pub fn chars(&mut self) -> Vec<char> {
        self.read::<String>().chars().collect()
    }
}


