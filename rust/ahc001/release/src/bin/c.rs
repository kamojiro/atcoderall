#![allow(non_snake_case)]
// use std::cmp::{max, min};

use proconio::input;
use rand::seq::SliceRandom;
use rand::{thread_rng, Rng};

pub const W: i64 = 10000;

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

    pub fn new() -> Rect{
        Rect{
            x1:0,
            y1:0,
            x2:0,
            y2:0,                
        }
    }
}

pub fn intersect(r1: &Rect, r2: &Rect) -> bool {
	r1.x2.min(r2.x2) > r1.x1.max(r2.x1) && r1.y2.min(r2.y2) > r1.y1.max(r2.y1)
}

// read_input
fn read_input() -> Input {
    input! {
        n: usize,
        xyr: [(i64, i64, i64); n],
    }
    let ps = xyr.iter().map(|&(x, y, _)| (x, y)).collect::<Vec<_>>();
	let size = xyr.iter().map(|&(_, _, s)| s).collect::<Vec<_>>();
	Input { ps, size }
}

#[derive(Clone, Debug)]
pub struct SortedInput {
    pub n: usize,
    pub XYRI: Vec<(i64, i64, i64, usize)>,
}

fn ascending_order_of_area(input: &Input) -> SortedInput {
    let n = input.ps.len();
    let mut XYRI: Vec<(i64, i64, i64, usize)> = Vec::new();
    for i in 0..n{
        XYRI.push((input.ps[i].0, input.ps[i].1, input.size[i], i))
    }
    XYRI.sort_by(|a, b| a.2.cmp(&b.2));
    SortedInput { n, XYRI }
}

fn descending_order_of_area(input: &Input) -> SortedInput {
    let n = input.ps.len();
    let mut XYRI: Vec<(i64, i64, i64, usize)> = Vec::new();
    for i in 0..n{
        XYRI.push((input.ps[i].0, input.ps[i].1, input.size[i], i))
    }
    XYRI.sort_by(|a, b| b.2.cmp(&a.2));
    SortedInput { n, XYRI }
}


// O(n) 200くらい
fn check_all_duplicates(input: &SortedInput, square: &Rect, square_index: usize, all_squares: &Vec<Rect>) -> bool{
    for i in 0..input.n{
        if i == square_index{
            continue
        }
        if intersect(square, &all_squares[i]){
            return true
        }
    }
    false
}

fn canonical_point(input: &SortedInput) -> Vec<Rect> {
    let mut ret: Vec<Rect> = Vec::new();
    for (x, y, _, _) in &input.XYRI {
        // let a = x;
        // let b = y;
        // ret.push((a,b,a+1,b+1));
        ret.push(Rect{x1:*x, y1:*y, x2:*x + 1, y2:*y + 1})
    }
    ret
}

// 1つずつ大きくしていく
// 左上右下の順番で処理する
// どの操作においても、面積を大きくすることができなければストップする
fn solve_extension(
    input: &SortedInput,
    base_points: &Vec<Rect>,
) -> Vec<Rect> {
    let mut ret = base_points.clone();
    let directions = vec![(-1,0,0,0),(0,-1,0,0),(0,0,1,0),(0,0,0,1)];
    for i in 0..input.n {
        // let (mut x1,mut y1,mut x2,mut y2) = (ret[i].x1, ret[i].y1, ret[i].x2, ret[i].y2);
        // let (mut tx1,mut ty1,mut tx2,mut ty2):(i64, i64, i64, i64) = (0,0,0,0);
        let mut next_rect = Rect{x1:0, y1:0, x2:0, y2:0};
        let r = input.XYRI[i].2;
        let mut unblocked = 0;
        loop{
            for (j, direction) in directions.iter().enumerate(){
                // println!("{} {}", j, unblocked);
                if (unblocked & (1<<j)) > 0{
                    continue
                }
                if (j == 0 && ret[i].x1 == 0)||(j==1 && ret[i].y1==0)||(j == 2 && ret[i].x2 == W) || (j==3 && ret[i].y2 == W){
                    unblocked |= 1<<j;
                    continue
                }
                // println!("{:?}", direction);
                // a, d が小さい方なので
                next_rect.x1 = ret[i].x1+direction.0;
                next_rect.y1 = ret[i].y1+direction.1;
                next_rect.x2 = ret[i].x2+direction.2;
                next_rect.y2 = ret[i].y2+direction.3;
                // println!("{} {} {} {}", ta, tb, tc, td);
                // println!("{} {}", get_area(ta,tb,tc,td), r);
                if next_rect.size() > r{
                    unblocked |= 1<<j;
                    continue
                }
                // println!("{} {} {} {}",i, a,ta,unblocked);
                // println!("{}", j);
                // println!("{} {} {} {}", a, b, c, d);
                // if i == 0 && td < 10{
                //     println!("{} {:?} {:?} {}",j,(a, b, c, d),(ta,tb,tc,td) , check_all_duplicates(&input, (ta,tb,tc,td),i, &ret));
                // }
                if check_all_duplicates(&input, &next_rect,i, &ret){
                    unblocked |= 1<<j;
                }else{
                    ret[i].x1 = next_rect.x1;
                    ret[i].y1 = next_rect.y1;
                    ret[i].x2 = next_rect.x2;
                    ret[i].y2 = next_rect.y2;
                }
            }
            // println!("{}", unblocked);            
            if unblocked == 15{
                break
            }
        }
    }
    ret
}

fn sort_by_index(indices: &Vec<usize>, input: &Input) -> SortedInput{
    let n = input.ps.len();
    let mut XYRI: Vec<(i64,i64,i64,usize)> = vec![(0,0,0,0);n];
    for (i, &index) in indices.iter().enumerate(){
        XYRI[index].0 = input.ps[i].0;
        XYRI[index].1 = input.ps[i].1;
        XYRI[index].2 = input.size[i];
        XYRI[index].3 = i;
    }
    SortedInput{
        n, XYRI,
    }
    
}

fn solve_extension_random(input:&Input, indices: &mut Vec<usize>) -> (SortedInput,Vec<Rect>){
    let mut rng = rand::thread_rng();
    indices.shuffle(&mut rng);
    let sorted_input = sort_by_index(&indices, &input);
    let base_points = canonical_point(&sorted_input);
    let ans =  solve_extension(&sorted_input, &base_points);
    (sorted_input, ans)
}

fn shaping(
    input: &SortedInput,
    ans: &Vec<Rect>,
) -> Vec<Rect> {
    let mut ret: Vec<Rect> = vec![Rect{x1:0,y1:0,x2:0,y2:0}; input.n];
    for i in 0..input.n {
        ret[input.XYRI[i].3] = ans[i];
    }
    ret
}

fn extension(
    i: usize,
    input: &SortedInput,
    iron: &mut Vec<Rect>){
    // let mut ret = base_points.clone();
    let directions = vec![(-1,0,0,0),(0,-1,0,0),(0,0,1,0),(0,0,0,1)];
    let mut next_rect = Rect{x1:0, y1:0, x2:0, y2:0};
    let r = input.XYRI[i].2;
    let mut unblocked = 0;
    loop{
        for (j, direction) in directions.iter().enumerate(){
            // println!("{} {}", j, unblocked);
            if (unblocked & (1<<j)) > 0{
                continue
            }
            if (j == 0 && iron[i].x1 == 0)||(j==1 && iron[i].y1==0)||(j == 2 && iron[i].x2 == W) || (j==3 && iron[i].y2 == W){
                unblocked |= 1<<j;
                continue
            }
            // println!("{:?}", direction);
            // a, d が小さい方なので
            next_rect.x1 = iron[i].x1+direction.0;
            next_rect.y1 = iron[i].y1+direction.1;
            next_rect.x2 = iron[i].x2+direction.2;
            next_rect.y2 = iron[i].y2+direction.3;
            // println!("{} {} {} {}", ta, tb, tc, td);
            // println!("{} {}", get_area(ta,tb,tc,td), r);
            if next_rect.size() > r{
                unblocked |= 1<<j;
                continue
            }
            // println!("{} {} {} {}",i, a,ta,unblocked);
            // println!("{}", j);
            // println!("{} {} {} {}", a, b, c, d);
            // if i == 0 && td < 10{
            //     println!("{} {:?} {:?} {}",j,(a, b, c, d),(ta,tb,tc,td) , check_all_duplicates(&input, (ta,tb,tc,td),i, &ret));
            // }
            if check_all_duplicates(&input, &next_rect,i, &ret){
                unblocked |= 1<<j;
            }else{
                iron[i].x1 = next_rect.x1;
                iron[i].y1 = next_rect.y1;
                iron[i].x2 = next_rect.x2;
                iron[i].y2 = next_rect.y2;
            }
        }
        // println!("{}", unblocked);            
        if unblocked == 15{
            break
        }
    }
}


fn annealing(input: &SortedInput, iron: Vec<Rect>) -> Vec<Rect>{
    let mut ret = iron.clone();
    let n = input.ps.len();
    let mut rng = thread_rng();
    let mut changed = vec![false; n];
    for _ in 0..10{
        let index: usize = rng.gen_range(0, n);
        changed[index] = true;
        let width_smaller: i64 = rng.gen_range(1,21);
        let hight_smaller: i64 = rng.gen_range(1,21);
        if width_smaller <= 10{
            let length = width_smaller;
            if ret[index].x2 - ret[index].x1 > length{
                ret[index].x1 += length;
            }
        }else{
            let length = width_smaller-10;
            if ret[index].x2 - ret[index].x1 > length{
                ret[index].x2 -= length;
            }
        }
        if hight_smaller <= 10{
            let length = hight_smaller;
            if ret[index].y2 - ret[index].y1 > length{
                ret[index].y1 += length;
            }
        }else{
            let length = hight_smaller-10;
            if ret[index].y2 - ret[index].y1 > length{
                ret[index].y2 -= length;
            } 
        }
    }
    for i in 0..n{
        if changed[i]{
            continue
        }
        extension(i,input,&mut ret);
    }
    for i in 0..n{
        if !changed[i]{
            continue
        }
        extension(i,input,&mut ret);        
    }

    
    ret
}

fn run() {
    // 計測開始
    const TL: f64 = 4.8;
    get_time();
    let input = read_input();
    let sorted_input = ascending_order_of_area(&input);
    let base_points = canonical_point(&sorted_input);
    // println!("{:?}", base_points);
    let ans = solve_extension(&sorted_input, &base_points);
    let mut sorted_ans = shaping(&sorted_input, &ans);
    let mut max_score = score(&input, &sorted_ans);

    // descending
    let sorted_input = descending_order_of_area(&input);
    let base_points = canonical_point(&sorted_input);
    let ans_descending = solve_extension(&sorted_input, &base_points);
    let sorted_ans_descending = shaping(&sorted_input, &ans_descending);
    let max_score_descending = score(&input, &sorted_ans_descending);

    if max_score < max_score_descending{
        max_score = max_score_descending;
        sorted_ans = sorted_ans_descending;
    }
    
    let mut indices: Vec<usize> = (0..input.ps.len()).collect();
    // eprintln!("{}", max_score);
    // eprintln!("{}", input.ps.len());
    loop{
        let t = get_time()/TL;
        // eprintln!("{}", get_time());
        if t >= 1.0{
            // eprintln!("{} {} {}", input.ps.len(), t, get_time());
            // eprintln!("{}", max_score);
            break
        }
        let (sorted_input0, ans0) = solve_extension_random(&input, &mut indices);
        let sorted_ans0 = shaping(&sorted_input0, &ans0);
        let score0 = score(&input, &sorted_ans0);
        if score0 > max_score{
            max_score = score0;
            sorted_ans = sorted_ans0;
        }
    }
    // let sorted_ans = shaping(&sorted_input, &ans);
    for rect in sorted_ans {
        println!("{} {} {} {}", rect.x1, rect.y1, rect.x2, rect.y2);
    }
}





pub fn score(input: &Input, out: &Vec<Rect>) -> i64 {
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
