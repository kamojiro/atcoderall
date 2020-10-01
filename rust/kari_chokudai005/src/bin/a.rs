#![allow(non_snake_case)]
use proconio::input;

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
	pub N: usize,
}

// read_input
fn read_input() -> Input {
    input!{
        N: usize,
    }
	Input {N,}
}

// solve()
fn solve(input: &Input) -> Vec<usize> {
	const TL: f64 = 2.95;
    // let mut rng = rand_pcg::Pcg64Mcg::new(890482);
    println!("solve");
	loop {
		let t = get_time() / TL;
		if t >= 0.9 {
			break;
        }
    }
    let mut x = Vec::new();
    x.push(2);
    x
}


fn run() {
    // 計測開始
    get_time();
    let input = read_input();
	let out = solve(&input);
	eprintln!("Time = {:.3}", get_time());
	// eprintln!("Score = {}", compute_score(&input, &out));
	for a in out{
        println!("{}",a);
	}
	
}
