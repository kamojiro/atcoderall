use proconio::input;
// use rand::seq::SliceRandom;
// use rand::{thread_rng, Rng};

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

// #[derive(Clone, Debug)]
// pub struct Input {
// 	pub ps: Vec<(i64, i64)>,
// 	pub size: Vec<i64>,
// }

// #[derive(Clone, Copy, Debug, PartialEq, Eq)]
// pub struct Rect {
// 	pub x1: i64,
// 	pub x2: i64,
// 	pub y1: i64,
// 	pub y2: i64,
// }

// impl Rect {
// 	pub fn size(&self) -> i64 {
// 		(self.x2 - self.x1) * (self.y2 - self.y1)
// 	}

//     pub fn new() -> Rect{
//         Rect{
//             x1:0,
//             y1:0,
//             x2:0,
//             y2:0,                
//         }
//     }
// }


// // read_input
// fn read_input() -> Input {
//     input! {
//         n: usize,
//         xyr: [(i64, i64, i64); n],
//     }
//     let ps = xyr.iter().map(|&(x, y, _)| (x, y)).collect::<Vec<_>>();
// 	let size = xyr.iter().map(|&(_, _, s)| s).collect::<Vec<_>>();
// 	Input { ps, size }
// }

// #[derive(Clone, Debug)]
// pub struct SortedInput {
//     pub n: usize,
//     pub XYRI: Vec<(i64, i64, i64, usize)>,
// }

fn elemental_solve(){
    let N: usize = 1000;
    for _ in 0..N{
        let mut u = 0;
        let mut d = 0;
        let mut l = 0;
        let mut r = 0;
        input! {
            si: usize,
            sj: usize,
            ti: usize,
            tj: usize,
        }
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
        print_answer(u, d, l, r);
        input! {
            _length: usize,
        }
    }
    
}

fn print_answer(u: usize, d: usize, l: usize, r: usize){
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
    eprintln!("{}", get_time());
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
    elemental_solve();
}





// pub fn score(input: &Input, out: &Vec<Rect>) -> i64 {
//     unimplemented!()
// }
