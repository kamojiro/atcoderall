#![allow(non_snake_case)]

use std::cmp::Ordering;
use std::collections::BinaryHeap;


fn main() {
    let (r, w) = (std::io::stdin(), std::io::stdout());
    let mut sc = IO::new(r.lock(), w.lock());
    let n: usize = 30;
    let mut A: Vec<Vec<u64>> = (0..n).map(|_| sc.vec(n)).collect();
    let mut ANS: Vec<(usize,usize)> = Vec::new();

    // let mut ans = 0;
    // for i in 0..30 {
    //     for j in 0..30 {
    //         ans += A[i][j];
    //     }
    // }
    // println!("{}", ans);
    // change(&mut A);
    // println!("{}", A[0][0]);
    // let (x,y) = get_first(&A);
    // println!("{} {}", x, y );
    
    let mut heap = BinaryHeap::new();
    for i in 0..n{
        for j in 0..n{
            // println!("{} ({}, {})",A[i][j], i, j);
            heap.push(Information {height: A[i][j], position: (i,j)});
        }
    }
    // println!("{}", heap.len());
    // for _ in 0..30 {
    //     let info = heap.pop();
    //     match info{
    //     Some(Information{height, position}) => {
    //         let (z,w) = position;
    //         ANS.push((z,w));
    //         println!("{} ({},{})", height, z,w);
    //     },
    //     _ => (),
    //     }
    // }
    // println!("{}", heap.len());

    while let Some( Information{height, position}) = heap.pop(){
        let (x,y) = position;
        if height > A[x][y]{
            continue
        }
        if height < 1{
            break
        }
        change(n,x,y,&mut A, &mut ANS, &mut heap);
    }
    // let t = ANS.len();
    for (x,y) in ANS{
        println!("{} {}", x, y);
    }
    // println!("{}", t);    
}

fn change(n:usize, a:usize, b:usize, board: &mut Vec<Vec<u64>>, ANS: &mut Vec<(usize, usize)>, heap: &mut BinaryHeap<Information>) {
    let mut x = a;
    let mut y = b;
    let mut judge:bool = false;
    let mut height = board[x][y];
    loop {
        if height == 0{
            break
        }
        ANS.push((x+1,y+1));
        height = height-1;
        board[x][y] = height;
        heap.push(Information{height:height, position:(x,y)});
        for i in 0..4 {
            let (c, s, t) = descend(i,n,x,y,&board,height);
            if c {
                x = s;
                y = t;
                judge = c;
                break
            }
        }
        if judge{
            judge = false;
            continue
        }
        break
        
    }
}

fn descend(pattern:usize, n:usize, x:usize, y:usize, board: &Vec<Vec<u64>>, height:u64) -> (bool, usize, usize){
    if pattern == 0 {
        if 0 < x{
            if board[x-1][y] == height{
                return (true,x-1,y);
            }
        }
    }else if pattern == 1 {
        if x < n-1{
            if board[x+1][y] == height{
                return (true,x+1,y);
            }
        }
    }else if pattern == 2{
        if y > 0{
            if board[x][y-1] == height{
                return (true,x,y-1);
            }
        }
    }else if pattern == 3{
        if y < n-1{
            if board[x][y+1] == height{
                return (true,x,y+1);
            }
        }
    }
    (false,x,y)
    
}


#[derive(Copy, Clone, Eq, PartialEq)]
struct Information {
    height: u64,
    position: (usize, usize),
}

impl Ord for Information{
    fn cmp(&self, other: &Information) -> Ordering {
        self.height.cmp(&other.height)
    }
}

impl PartialOrd for Information {
    fn partial_cmp(&self, other: &Information) -> Option<Ordering>{
        Some(self.cmp(other))
    }
}


pub struct IO<R, W: std::io::Write>(R, std::io::BufWriter<W>);
 
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
