#![allow(non_snake_case)]
use std::cmp::{max, min};

use proconio::input;

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
    pub n: usize,
    pub l: usize,
    pub XYR: Vec<(i64, i64, i64)>,
}

// read_input
fn read_input() -> Input {
    input! {
        n: usize,
        XYR: [(i64, i64, i64); n],
    }
    let l: usize = 10000;
    Input { n,l, XYR }
}

#[derive(Clone, Debug)]
pub struct SortedInput {
    pub n: usize,
    pub l: usize,
    pub XYRI: Vec<(i64, i64, i64, usize)>,
}

fn ascending_order_of_area(input: &Input) -> SortedInput {
    let n = input.n;
    let l = input.l;
    let mut XYRI: Vec<(i64, i64, i64, usize)> = Vec::new();
    let mut index: usize = 0;
    for (x, y, r) in &input.XYR {
        XYRI.push((*x, *y, *r, index));
        index += 1;
    }
    XYRI.sort_by(|a, b| a.2.cmp(&b.2));
    SortedInput { n,l, XYRI }
}

fn get_area(a: i64, b: i64, c: i64, d: i64) -> i64 {
    // println!("{} {} {} {}", a,b,c,d);
    // println!("get area: {}",(c - a) * (d - b));
    (c - a) * (d - b)
}

// fn canonical_point(input: &Input) -> Vec<(usize, usize, usize, usize)> {
//     let mut ret: Vec<(usize, usize, usize, usize)> = Vec::new();
//     for (x,y,_) in &input.XYR{
//         // let a = x;
//         // let b = y;
//         // ret.push((a,b,a+1,b+1));
//         ret.push((*x,*y,*x+1,*y+1))
//     }
//     ret
// }

fn check_duplicate(
    square_s: (i64, i64, i64, i64),
    square_t: (i64, i64, i64, i64),
) -> bool {
    if max(square_s.0, square_t.0) < min(square_s.2, square_t.2)
        && max(square_s.1, square_t.1) < min(square_s.3, square_t.3)
    {
        true
    } else {
        false
    }
}

// O(n) 200くらい
fn check_all_duplicates(input: &SortedInput, square: (usize, usize, usize, usize), square_index: usize, all_squares: &Vec<(usize, usize, usize, usize)>) -> bool{
    for i in 0..input.n{
        if i == square_index{
            continue
        }
        if check_duplicate(square, all_squares[i]){
            return true
        }
    }
    false
}

fn canonical_point(input: &SortedInput) -> Vec<(i64, i64, i64, i64)> {
    let mut ret: Vec<(i64, i64, i64, i64)> = Vec::new();
    for (x, y, _, _) in &input.XYRI {
        // let a = x;
        // let b = y;
        // ret.push((a,b,a+1,b+1));
        ret.push((*x, *y, *x + 1, *y + 1))
    }
    ret
}

// 1つずつ大きくしていく
// 左上右下の順番で処理する
// どの操作においても、面積を大きくすることができなければストップする
fn solve01(
    input: &SortedInput,
    base_points: &Vec<(i64, i64, i64, i64)>,
) -> Vec<(i64, i64, i64, i64)> {
    let mut ret = base_points.clone();
    let directions = vec![(-1,0,0,0),(0,-1,0,0),(0,0,1,0),(0,0,0,1)];
    for i in 0..input.n {
        let (mut a,mut b,mut c,mut d) = ret[i];
        // println!("{:?}", ret[i]);
        let (mut ta,mut tb,mut tc,mut td):(i64, i64, i64, i64) = (0,0,0,0);
        let r = input.XYRI[i].2;
        let mut unblocked = 0;
        loop{
            for (j, direction) in directions.iter().enumerate(){
                // println!("{} {}", j, unblocked);
                if (unblocked & (1<<j)) > 0{
                    continue
                }
                if (j == 0 && a == 0)||(j==1 && b==0)||(j == 2 && c == input.l) || (j==3 && d == input.l){
                    unblocked |= 1<<j;
                    continue
                }
                // println!("{:?}", direction);
                // a, d が小さい方なので
                ta = a+direction.0;
                tb = b+direction.1;
                tc = c+direction.2;
                td = d+direction.3;
                // println!("{} {} {} {}", ta, tb, tc, td);
                // println!("{} {}", get_area(ta,tb,tc,td), r);
                if get_area(ta,tb,tc,td) > r{
                    unblocked |= 1<<j;
                    continue
                }
                // println!("{} {} {} {}",i, a,ta,unblocked);
                // println!("{}", j);
                // println!("{} {} {} {}", a, b, c, d);
                // if i == 0 && td < 10{
                //     println!("{} {:?} {:?} {}",j,(a, b, c, d),(ta,tb,tc,td) , check_all_duplicates(&input, (ta,tb,tc,td),i, &ret));
                // }
                if check_all_duplicates(&input, (ta,tb,tc,td),i, &ret){
                    unblocked |= 1<<j;
                }else{
                    a = ta;
                    b = tb;
                    c = tc;
                    d = td;
                }
            }
            // println!("{}", unblocked);            
            if unblocked == 15{
                break
            }
        }
        // println!("{} finished", i);
        ret[i] = (a,b,c,d);
        // println!("{:?}", ret);
    }
    ret
}

fn make_wata_input(input: &Input) -> WataInput{
    let ps = input.XYR.iter().map(|&(x, y, _)| (x, y)).collect::<Vec<_>>();
	let size = input.XYR.iter().map(|&(_, _, s)| s).collect::<Vec<_>>();
    WataInput{ps,size}
}

fn shaping(
    input: &SortedInput,
    ans: &Vec<(usize, usize, usize, usize)>,
) -> Vec<(usize, usize, usize, usize)> {
    let mut ret: Vec<(usize, usize, usize, usize)> = vec![(0, 0, 0, 0); input.n];
    for i in 0..input.n {
        ret[input.XYRI[i].3] = ans[i];
    }
    ret
}

fn run() {
    // 計測開始
    get_time();
    let input = read_input();
    let wata_input = make_wata_input(&input);
    // println!("finished input");
    let sorted_input = ascending_order_of_area(&input);
    let base_points = canonical_point(&sorted_input);
    // println!("{:?}", base_points);
    let ans01 = solve01(&sorted_input, &base_points);
    let sorted_ans = shaping(&sorted_input, &ans01);
    for (a, b, c, d) in sorted_ans {
        println!("{} {} {} {}", a, b, c, d);
    }
}

pub const W: i64 = 10000;

#[derive(Clone, Debug)]
pub struct WataInput {
	pub ps: Vec<(i64, i64)>,
	pub size: Vec<i64>,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct Rect {
	pub x1: i64,
	pub x2: i64,
	pub y1: i64,
	pub y2: i64,
}

impl Rect {
	pub fn size(&self) -> i64 {
		(self.x2 - self.x1) * (self.y2 - self.y1)
	}
}

pub fn intersect(r1: &Rect, r2: &Rect) -> bool {
	r1.x2.min(r2.x2) > r1.x1.max(r2.x1) && r1.y2.min(r2.y2) > r1.y1.max(r2.y1)
}

pub fn score(input: &WataInput, out: &Vec<Rect>) -> i64 {
	let n = input.ps.len();
	let mut score = 0.0;
	for i in 0..n {
		if out[i].x1 < 0 || out[i].x2 > W || out[i].y1 < 0 || out[i].y2 > W {
			eprintln!("rectangle {} is out of range", i);
			return 0;
		}
		if out[i].x1 >= out[i].x2 || out[i].y1 >= out[i].y2 {
			eprintln!("rectangle {} does not have positive area", i);
			return 0;
		}
		if !(out[i].x1 <= input.ps[i].0 && input.ps[i].0 < out[i].x2 && out[i].y1 <= input.ps[i].1 && input.ps[i].1 < out[i].y2) {
			eprintln!("rectangle {} does not contain point {}", i, i);
			continue;
		}
		for j in 0..i {
			if intersect(&out[i], &out[j]) {
				eprintln!("rectangles {} and {} overlap", j, i);
				return 0;
			}
		}
		let s = out[i].size().min(input.size[i]) as f64 / out[i].size().max(input.size[i]) as f64;
		score += 1.0 - (1.0 - s) * (1.0 - s);
	}
	(1e9 * score / n as f64).round() as i64
}
