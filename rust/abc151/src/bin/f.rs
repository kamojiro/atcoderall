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

#[fastout]
fn main() {
    input!{
        N: usize,
        XY: [(f64, f64); N],
    }
    let g = 0.000000001;
    let mut l = 0.0;
    let mut r = 1_000_000.0;
    for _ in 0..50{
        let m = (l+r)/2.0;
        let mut ok = false;
        'points: for i in 0..(N-1){
            for j in (i+1)..N{
                if d(XY[i], XY[j]) > m*2.0{continue;}
                let (x,y) = intersection(XY[i], XY[j], m);
                let mut xok = true;
                for k in 0..N{
                    if d(x, XY[k]) > m+g{
                        xok = false;
                        break;
                    }
                }
                if xok{
                    ok = true;
                    break 'points;
                }
                let mut yok = true;
                for k in 0..N{
                    if d(y, XY[k]) > m+g{
                        yok = false;
                        break;
                    }
                }
                if yok{
                    ok = true;
                    break 'points;
                }
            }
        }
        if ok{
            r = m;
        }else{
            l = m
        }
    }
    println!("{}", r);
}

fn intersection(x: (f64, f64), y: (f64,f64), r: f64) -> ((f64,f64),(f64,f64)){
    let z = ((x.0 + y.0)/2.0, (x.1 + y.1)/2.0);
    let xy = d(x,y);
    let a = ((y.0 - x.0)/xy, (y.1 - x.1)/xy);
    let h = pythangorean_theorem(r, xy/2.0);
    let hp = (-a.1*h, a.0*h);
    let hm = (a.1*h, -a.0*h);
    ((z.0+hp.0, z.1+hp.1), (z.0+hm.0,z.1+hm.1))
    
}

fn d(x: (f64, f64), y: (f64,f64)) -> f64{
    ((x.0 - y.0)*(x.0 - y.0) + (x.1 - y.1)*(x.1 - y.1)).sqrt()
}

fn pythangorean_theorem(r: f64, x: f64) -> f64{
    (r*r - x*x).sqrt()
}
