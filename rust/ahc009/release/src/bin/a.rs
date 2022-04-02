#![allow(non_snake_case)]

use proconio::input;
use proconio::marker::Bytes;

#[macro_export]
macro_rules! mat {
	($($e:expr),*) => { Vec::from(vec![$($e),*]) };
	($($e:expr,)*) => { Vec::from(vec![$($e),*]) };
	($e:expr; $d:expr) => { Vec::from(vec![$e; $d]) };
	($e:expr; $d:expr $(; $ds:expr)+) => { Vec::from(vec![mat![$e $(; $ds)*]; $d]) };
}

#[derive(Clone, Debug)]
pub struct Input {
    pub H: usize,
    pub W: usize,
    pub s: (usize, usize),
    pub t: (usize, usize),
    pub p: f64,
    pub h: Vec<Vec<bool>>,
    pub v: Vec<Vec<bool>>,
}

pub fn solve3(_input: &Input) -> String{
    let mut ans = Vec::new();
    for i in 0..150{
        if i%40 == 0 || i%40 ==1{
            ans.push(b'U');
            continue;
        } 
        if i%40 == 20 || i%40 ==21{
            ans.push(b'L');
            continue;
        }
        if i%5 == 0 || i%5 == 1{
            ans.push(b'D');
        }else if i%5 == 2 || i%5 == 3{
            ans.push(b'R');
        }else{
            if i%10 == 4{
                ans.push(b'U')
            }else{
                ans.push(b'L');
            }
        }
    }
    
    for i in 150..200{
        if i%10 == 2{
            ans.push(b'D');
        }else if i%10 == 3{
        ans.push(b'R');
        }else if i%4 == 0{
            ans.push(b'D');
        }else if i%4 == 1{
            ans.push(b'R');
        }else if i%4 == 2 {
            ans.push(b'U');
        }else{
            ans.push(b'L')
        }
    }
    ans.iter().map(|&s| s as char).collect::<String>()
}



fn main() {
	get_time();
    let input = read_input();
    println!("{}", solve3(&input))
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

pub fn solve1(_input: &Input) -> String{
    let mut ans = Vec::new();
    for i in 0..200{
        if i%2 == 0{
            ans.push(b'D');
        }else{
            ans.push(b'R');
        }
    }
    ans.iter().map(|&s| s as char).collect::<String>()
}

pub fn solve2(_input: &Input) -> String{
    let mut ans = Vec::new();
    for i in 0..150{
        if i%5 == 0 || i%5 == 1{
            ans.push(b'D');
        }else if i%5 == 2 || i%5 == 3{
            ans.push(b'R');
        }else{
            if i%10 == 4{
                ans.push(b'U')
            }else{
                ans.push(b'L');
            }
        }
    }
    
    for i in 150..200{
        if i%4 == 0{
            ans.push(b'D');
        }else if i%4 == 1{
            ans.push(b'R');
        }else if i%4 == 2 {
            ans.push(b'U');
        }else{
            ans.push(b'L')
        }
    }
    ans.iter().map(|&s| s as char).collect::<String>()
}

// read_input
fn read_input() -> Input {
    let H: usize = 20;
    let W: usize = 20;
    input!{
        (si, sj, ti, tj, p):(usize, usize, usize, usize, f64),
        hor: [Bytes; H],
        ver: [Bytes; H-1],
    };
    let s = (si, sj);
    let t = (ti, tj);
    let mut h = vec![vec![false; W-1]; H];
    let mut v = vec![vec![false; W]; H-1];
    for i in 0..H{
        for j in 0..(W-1){
            if hor[i][j] == 1{
                h[i][j] = true;
            }
        }
    }
    for i in 0..(H-1){
        for j in 0..W{
            if ver[i][j] == 1{
                v[i][j] = true;
            }
        }
    }
    Input{H, W, s, t, p, h, v}
}
