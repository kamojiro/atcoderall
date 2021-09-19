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
// use proconio::marker::Bytes;
// use proconio::marker::Usize1;
const EPS: f64 = 1e-9;

#[fastout]
fn main() {
    input!{
        N: usize,
        K: usize,
        XYC: [(f64,f64,f64);N],
    }
    let mut l = 0.0;
    let mut r = 1000_000.0;
    while r - l > EPS{
        let m = (l+r)/2.0;
        let mut candidate = Vec::new();
        for i in 0..N{
            let (x0,y0,c0) = XYC[i];
            candidate.push((x0, y0));
            for j in 0..N{
                let (x1,y1,c1) = XYC[j];
                for (x,y) in intersection(x0, y0, m/c0, x1, y1, m/c1){
                    candidate.push((x,y));
                }
            }
        }
        let mut can = false;
        for &(x,y) in &candidate{
            let mut count = 0;
            for &(tx,ty,c) in &XYC{
                if c*(((tx-x)*(tx-x) + (ty-y)*(ty-y)).sqrt()) <= m+EPS{
                    count += 1;
                }
            }
            if count >= K{
                can = true;
                break
            }
        }
        if can{
            r = m;
        }else{
            l = m;
        }
        
    }
    println!("{}", l);
}


fn intersection(x0: f64, y0: f64, r0:f64, x1: f64, y1: f64, r1: f64) -> Vec<(f64,f64)>{
    let mut ret = Vec::new();
    let d = ((x0-x1)*(x0-x1) + (y0-y1)*(y0-y1)).sqrt();
    let cos = (d*d + r0*r0 - r1*r1)/(2.0 * d * r0);
    if cos*cos <= 1.0{
        let sin = (1.0 - cos*cos).sqrt();
        let dx = x1 - x0;
        let dy = y1 - y0;
        let x = x0 + r0/d*(cos*dx-sin*dy);
        let y = y0 + r0/d*(sin*dx+cos*dy);
        ret.push((x,y));
        let x = x0 + r0/d*(cos*dx+sin*dy);
        let y = y0 + r0/d*(-sin*dx+cos*dy);
        ret.push((x,y))
    }
    ret
}
