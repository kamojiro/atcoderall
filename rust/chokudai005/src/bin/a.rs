#![allow(non_snake_case)]
use petgraph::unionfind::UnionFind;
use proconio::input;
use std::collections::BTreeSet;

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

// solve()
fn solve3(input: &Input) -> Vec<(usize, usize, usize)> {
	const TL: f64 = 2.95;
	// let mut rng = rand_pcg::Pcg64Mcg::new(890482);
	let N = input.N;
	let K = input.K;
	let mut unionfind = UnionFind::new(N * N);
	// (i,j) is mapped to i*N+j
	// Here (i,j) is 0-indexed
	// yokohoukou
	for i in 1..=N {
		for j in 1..N {
			if input.S_ij[i - 1][j - 1] == input.S_ij[i - 1][j] {
				unionfind.union((i - 1) * N + j - 1, (i - 1) * N + j);
			}
		}
	}
	// tatehoukou
	for i in 1..N {
		for j in 1..=N {
			if input.S_ij[i - 1][j - 1] == input.S_ij[i][j - 1] {
				unionfind.union((i - 1) * N + j - 1, i * N + j - 1);
			}
		}
	}

	// 連結成分に番号を与える
	let mut masumes_of_connected_comps = Vec::new();
	let mut conn_comp_ids = vec![N * N + 1; N * N];
	for i in 0..N * N {
		let ii = unionfind.find_mut(i);
		if conn_comp_ids[ii] > N * N {
			// not yet given a number
			conn_comp_ids[ii] = masumes_of_connected_comps.len();
			masumes_of_connected_comps.push(ii);
		}
		conn_comp_ids[i] = conn_comp_ids[ii];
	}
	let number_of_connected_comps = masumes_of_connected_comps.len();
	// グラフを作る
	let mut neighbors: Vec<BTreeSet<usize>> = vec![BTreeSet::new(); number_of_connected_comps];
	// 辺でつなげる
	// yokohoukou
	for i in 1..=N {
		for j in 1..N {
			let l1 = (i - 1) * N + j - 1;
			let l2 = (i - 1) * N + j;
			if unionfind.equiv(l1, l2) {
				continue;
			}
			let conn1 = conn_comp_ids[l1];
			let conn2 = conn_comp_ids[l2];
			if neighbors[conn1].contains(&conn2) {
				continue;
			}
			neighbors[conn1].insert(conn2);
			neighbors[conn2].insert(conn1);
		}
	}
	// tatehoukou
	for i in 1..N {
		for j in 1..=N {
			let l1 = (i - 1) * N + j - 1;
			let l2 = i * N + j - 1;
			if unionfind.equiv(l1, l2) {
				continue;
			}
			let conn1 = conn_comp_ids[l1];
			let conn2 = conn_comp_ids[l2];
			if neighbors[conn1].contains(&conn2) {
				continue;
			}
			neighbors[conn1].insert(conn2);
			neighbors[conn2].insert(conn1);
		}
	}

	// 連結成分を数える

	let mut colors_connected: Vec<usize> = vec![0; K + 1];
	let mut board: Vec<bool> = vec![false; N * N];
	for i in 0..(N * N) {
		let mut color = input.S_ij[i / N][i % N];
		if !board[unionfind.find_mut(i)] {
			colors_connected[color] += 1;
			board[unionfind.find_mut(i)] = true;
		}
	}

	// let mut sum_of_connected = colors_connected.iter().sum();

	let max_of_connected = *colors_connected.iter().max().unwrap();
	let mut color_max_of_connected: usize = 0;
	for i in 1..(K + 1) {
		if colors_connected[i] == max_of_connected {
			color_max_of_connected = i;
			break;
		}
	}

	// 中心となる連結成分と、隣接している連結成分を以下で管理する
	// 隣接している色ごとに、隣接している頂点を蓄える。つまり、以下のように
	// Vec<Vec<usize>> [[色1の頂点たち], [色2の頂点たち]]
	// 色kに変更するときは、[色kの頂点たち]と隣接する頂点が新しく、[色iの頂点たち]に追加される

	let mut ANS0 = Vec::new();
	ANS0
}
// 単純に真ん中から点滅させる
fn solve2(input: &Input) -> Vec<(usize, usize, usize)> {
	let N = input.N;
	let K = input.K;
	let i_center = (N / 2) * N + N / 2;
	let mut ANS0 = Vec::new();
	for _ in 0..N {
		for color in 1..=K {
			ANS0.push(((i_center / N) + 1, (i_center % N) + 1, color));
		}
	}
	return ANS0;
}

// solve()
fn solve1(input: &Input) -> Vec<(usize, usize, usize)> {
	const TL: f64 = 2.95;
	// let mut rng = rand_pcg::Pcg64Mcg::new(890482);
	let N = input.N;
	let K = input.K;
	let mut unionfind = UnionFind::new(N * N);
	// (i,j) is mapped to i*N+j
	// Here (i,j) is 0-indexed
	// yokohoukou
	for i in 1..=N {
		for j in 1..N {
			if input.S_ij[i - 1][j - 1] == input.S_ij[i - 1][j] {
				unionfind.union((i - 1) * N + j - 1, (i - 1) * N + j);
			}
		}
	}
	// tatehoukou
	for i in 1..N {
		for j in 1..=N {
			if input.S_ij[i - 1][j - 1] == input.S_ij[i][j - 1] {
				unionfind.union((i - 1) * N + j - 1, i * N + j - 1);
			}
		}
	}

	// 連結成分を数える

	let mut colors_connected: Vec<usize> = vec![0; K + 1];
	let mut board: Vec<bool> = vec![false; N * N];
	for i in 0..(N * N) {
		let mut color = input.S_ij[i / N][i % N];
		if !board[unionfind.find_mut(i)] {
			colors_connected[color] += 1;
			board[unionfind.find_mut(i)] = true;
		}
	}

	// let mut sum_of_connected = colors_connected.iter().sum();

	let max_of_connected = *colors_connected.iter().max().unwrap();
	let mut color_max_of_connected: usize = 0;
	for i in 1..(K + 1) {
		if colors_connected[i] == max_of_connected {
			color_max_of_connected = i;
			break;
		}
	}
	// 解答の操作
	let mut ANS0: Vec<(usize, usize, usize)> = Vec::new();

	// 具体的な操作
	// color_max_of_connected: 揃えたい色
	let mut board2: Vec<bool> = vec![false; N * N];
	for i in 0..(N * N) {
		let color = input.S_ij[i / N][i % N];
		if board2[unionfind.find_mut(i)] {
			// Already touched
			continue;
		}
		if color == color_max_of_connected {
			// Net needed to touch
			continue;
		}
		ANS0.push((i / N + 1, (i % N) + 1, color));
	}

	ANS0
}

fn one_point_score_checker(
	input: &Input,
	query: &Vec<(usize, usize, usize)>,
	start: usize,
) -> usize {
	let N = input.N;
	let K = input.K;
	let mut S_ij = input.S_ij.clone();
	let mut visited: Vec<bool> = vec![false; N * N];
	let mut another_visited: Vec<bool> = vec![false; N * N];
	let mut color = S_ij[start / N][start % N];
	let mut stack: Vec<usize> = Vec::new();
	let mut color_neighborhood: Vec<Vec<usize>> = vec![Vec::new(); K + 1];
	let vy: Vec<isize> = vec![1, -1, 0, 0];
	let vx: Vec<isize> = vec![0, 0, 1, -1];
	stack.push(start);
	// visited[start] = true;

	while let Some(point) = stack.pop() {
		if visited[point] {
			continue;
		}
		// shori
		visited[point] = true;
		for i in 0..4 {
			let y = (point / N) as isize + vy[i];
			let x = (point % N) as isize + vx[i];
			if (y < 0) || (N as isize - 1 < y) || (x < 0) || (N as isize - 1 < x) {
				continue;
			}
			let y = y as usize;
			let x = x as usize;
			if S_ij[y][x] == color {
				if visited[y * N + x] {
					stack.push(y * N + x);
				}
			} else {
				if !another_visited[y * N + x] {
					color_neighborhood[S_ij[y][x]].push(y * N + x);
					another_visited[y * N + x] = true;
				}
			}
		}
	}
    let mut count:usize = 0;
	'outer: for &(y, x, c) in query {
		// let y = y - 1;
		// let x = x - 1;
		let color = c;
		let mut stack: Vec<usize> = Vec::new();
		for &h in &color_neighborhood[color] {
			stack.push(h);
        }
		color_neighborhood[c] = Vec::new();
		while let Some(point) = stack.pop() {
			if visited[point] {
				continue;
			}
			// shori
			visited[point] = true;
			for i in 0..4 {
				let y = (point / N) as isize + vy[i];
				let x = (point % N) as isize + vx[i];
				if (y < 0) || (N as isize - 1 < y) || (x < 0) || (N as isize - 1 < x) {
					continue;
				}
				let y = y as usize;
				let x = x as usize;
				if S_ij[y][x] == color {
					if visited[y * N + x] {
						stack.push(y * N + x);
					}
				} else {
					if !another_visited[y * N + x] {
						color_neighborhood[S_ij[y][x]].push(y * N + x);
						another_visited[y * N + x] = true;
					}
				}
			}
        }
        count += 1;
        for i in 1..K{
            if !color_neighborhood[i].is_empty(){
                continue 'outer;
            }
        }
        break;
	}
	return count;
}

fn run() {
	// 計測開始
	get_time();
	let input = read_input();
    let out = solve2(&input);
    let count = one_point_score_checker(&input, &out,out[0].0*input.N+out[0].1);
	// eprintln!("Time = {:.3}", get_time());
	// eprintln!("Score = {}", compute_score(&input, &out));
	let Q = count;
    println!("{}", Q);
    for i in 0..count{
        println!("{} {} {}", out[i].0, out[i].1, out[i].2);
    }
    
}
