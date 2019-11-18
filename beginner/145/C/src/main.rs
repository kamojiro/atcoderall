#![allow(non_snake_case)]

fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    let xy = (0..N)
        .map(|_| (sc.read::<f64>(), sc.read::<f64>()))
        .collect::<Vec<_>>();
    
    let mut sum = 0.0;
    let mut p = (0..N).collect::<Vec<_>>();
    sum += calc(&xy, &p);
    while p.next_permutation(){
        sum += calc(&xy, &p);
    }
    for i in 1..(N+1){
        sum /= i as f64;
    }
    println!("{}", sum);
                                         
}

fn calc(xy: &Vec<(f64, f64)>, p:&Vec<usize>) -> f64{
    let mut sum = 0.0;
    for i in 1..p.len(){
        sum += ((xy[p[i]].0 - xy[p[i-1]].0).powf(2.0) + (xy[p[i]].1 - xy[p[i-1]].1).powf(2.0)).sqrt();
    }
    sum
}

pub trait LexicalPermutation {
    /// Return `true` if the slice was permuted, `false` if it is already
    /// at the last ordered permutation.
    fn next_permutation(&mut self) -> bool;
    /// Return `true` if the slice was permuted, `false` if it is already
    /// at the first ordered permutation.
    fn prev_permutation(&mut self) -> bool;
}
 
impl<T> LexicalPermutation for [T]
where
    T: Ord,
{
    /// Original author in Rust: Thomas Backman <serenity@exscape.org>
    fn next_permutation(&mut self) -> bool {
        // These cases only have 1 permutation each, so we can't do anything.
        if self.len() < 2 {
            return false;
        }
 
        // Step 1: Identify the longest, rightmost weakly decreasing part of the vector
        let mut i = self.len() - 1;
        while i > 0 && self[i - 1] >= self[i] {
            i -= 1;
        }
 
        // If that is the entire vector, this is the last-ordered permutation.
        if i == 0 {
            return false;
        }
 
        // Step 2: Find the rightmost element larger than the pivot (i-1)
        let mut j = self.len() - 1;
        while j >= i && self[j] <= self[i - 1] {
            j -= 1;
        }
 
        // Step 3: Swap that element with the pivot
        self.swap(j, i - 1);
 
        // Step 4: Reverse the (previously) weakly decreasing part
        self[i..].reverse();
 
        true
    }
 
    fn prev_permutation(&mut self) -> bool {
        // These cases only have 1 permutation each, so we can't do anything.
        if self.len() < 2 {
            return false;
        }
 
        // Step 1: Identify the longest, rightmost weakly increasing part of the vector
        let mut i = self.len() - 1;
        while i > 0 && self[i - 1] <= self[i] {
            i -= 1;
        }
 
        // If that is the entire vector, this is the first-ordered permutation.
        if i == 0 {
            return false;
        }
 
        // Step 2: Reverse the weakly increasing part
        self[i..].reverse();
 
        // Step 3: Find the rightmost element equal to or bigger than the pivot (i-1)
        let mut j = self.len() - 1;
        while j >= i && self[j - 1] < self[i - 1] {
            j -= 1;
        }
 
        // Step 4: Swap that element with the pivot
        self.swap(i - 1, j);
 
        true
    }
}

pub struct Scanner<R> {
    stdin: R,
}

impl<R: std::io::Read> Scanner<R> {
    pub fn read<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        let buf = self
            .stdin
            .by_ref()
            .bytes()
            .map(|b| b.unwrap())
            .skip_while(|&b| b == b' ' || b == b'\n')
            .take_while(|&b| b != b' ' && b != b'\n')
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


