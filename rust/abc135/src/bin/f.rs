// -*- coding:utf-8-unix -*-
#![allow(non_snake_case)]

#[cfg(debug_assertions)]
#[allow(unused)]
macro_rules! eprintln {
    ($p:tt, $($x:expr),*) => {
        std::eprintln!($p, $($x,)*);
    };
}

#[cfg(not(debug_assertions))]
#[allow(unused)]
macro_rules! eprintln {
    ($p:tt, $($x:expr),*) => {};
}

use proconio::{fastout, input};
use proconio::marker::Bytes;
// use proconio::marker::Usize1;

#[fastout]
fn main() {
    input!{
        s: Bytes,
        t: Bytes,
    }
    let mut ss = Vec::new();
    while ss.len() < t.len(){
        ss.extend_from_slice(&s);
    }
    let n = ss.len();
    let tn = t.len();
    while ss.len() < n+tn{
        ss.extend_from_slice(&s);
    }
    let mut ts = t;
    ts.push(b'$');
    ts.extend_from_slice(&ss);
    let z_array = get_z_array(&ts);
    let mut not_start = vec![false; n];
    let mut edges: Vec<usize> = vec![n; n];
    for i in (tn+1)..z_array.len(){
        if z_array[i] == tn{
            edges[(i-tn-1)%n] = (i-1)%n;
            not_start[(i-1)%n] = true;
        }
    }
    let mut ans = 0;
    let mut visited = vec![false; n];
    for i in 0..n{
        if not_start[i]{continue;}
        let mut now = i;
        let mut ians = 0;
        visited[now] = true;
        loop {
            now = edges[now];
            if now == n{
                if ans < ians{
                    ans = ians;
                }
                break
            }
            visited[now] = true;
            ians += 1;
        }
    }
    for i in 0..n{
        if visited[i]{continue;}
        let mut now = i;
        visited[now] = true;
        loop {
            now = edges[now];
            if now == n{break}
            if visited[now]{
                println!("-1");
                return;
            }
            visited[now] = true;
        }
    }
    println!("{}", ans);
    
}

// Z-algorithm
// Z[i] = (length of the the longest substring s[i:] which is also a prefix of s)
// reference
// [geeksfotgeeks](https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/)
// [kenkoooo's submit](https://atcoder.jp/contests/abc135/submissions/22268126)
fn get_z_array<T: PartialEq>(s: &[T]) -> Vec<usize>{
    let n = s.len();
    let mut ret = vec![0; n];
    // [l,r) is a window wchich matches with the prefix of s
    let mut l = 0;
    let mut r = 1;
    for i in 1..n{
        if i >= r{
            l = i;
            r = i+1;
            while r <= n && s[r-l-1] == s[r-1]{
                r += 1;
            }
            r -= 1;
            ret[i] = r-l;
        }else if ret[i-l] < r-i{
            ret[i] = ret[i-l]
        }else {
            l = i;
            while r <= n && s[r-l-1] == s[r-1]{
                r += 1;
            }
            r -= 1;
            ret[i] = r-l;
        }
    }
    ret[0] = n;
    ret
}
