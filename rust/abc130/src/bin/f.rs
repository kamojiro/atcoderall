// -*- coding:utf-8-unix -*-
#![allow(non_snake_case)]

use proconio::{fastout, input};
// use proconio::marker::Bytes;

#[fastout]
fn main() {
    input!{
        N: usize,
        XYD: [(i64, i64, char); N],
    }
    let mut time = vec![0.0];
    let dymax = XYD.iter().filter(|a| a.2 == 'D').map(|&a| a.1).max().unwrap_or(0);
    let uymax = XYD.iter().filter(|a| a.2 == 'U').map(|&a| a.1).max().unwrap_or(0);
    let lrymax = XYD.iter().filter(|a| a.2 == 'L' || a.2 == 'R').map(|&a| a.1).max().unwrap_or(0);
    set_time(&mut time, dymax, lrymax, uymax);
    let uymin = XYD.iter().filter(|a| a.2 == 'U').map(|&a| a.1).min().unwrap_or(0);
    let dymin = XYD.iter().filter(|a| a.2 == 'D').map(|&a| a.1).min().unwrap_or(0);
    let lrymin = XYD.iter().filter(|a| a.2 == 'L' || a.2 == 'R').map(|&a| a.1).min().unwrap_or(0);
    set_time(&mut time, uymin, lrymin, dymin);
    let rxmax = XYD.iter().filter(|a| a.2 == 'R').map(|&a| a.0).max().unwrap_or(0);
    let lxmax = XYD.iter().filter(|a| a.2 == 'L').map(|&a| a.0).max().unwrap_or(0);
    let duxmax = XYD.iter().filter(|a| a.2 == 'D' || a.2 == 'U').map(|&a| a.0).max().unwrap_or(0);
    set_time(&mut time, rxmax, duxmax, lxmax);
    let rxmin = XYD.iter().filter(|a| a.2 == 'R').map(|&a| a.0).min().unwrap_or(0);
    let lxmin = XYD.iter().filter(|a| a.2 == 'L').map(|&a| a.0).min().unwrap_or(0);
    let duxmin = XYD.iter().filter(|a| a.2 == 'D' || a.2 == 'U').map(|&a| a.0).min().unwrap_or(0);
    set_time(&mut time, rxmin, duxmin, lxmin);   
    let max = 1000_000_000;
    let min = -1000_000_000;
    
    let mut ans: f64 = 1000_000_000_000_000_00.0;
    for &t in &time{
        let mut xmin = max as f64;
        let mut xmax = min as f64;
        let mut ymin = max as f64;
        let mut ymax = min as f64;
        for &(x,y,d) in &XYD{
            if d == 'U'{
                xmin = xmin.min(x as f64);
                xmax = xmax.max(x as f64);
                ymin = ymin.min((y as f64)+t);
                ymax = ymax.max((y as f64)+t);
            }else if d == 'D'{
                xmin = xmin.min(x as f64);
                xmax = xmax.max(x as f64);
                ymin = ymin.min((y as f64)-t);
                ymax = ymax.max((y as f64)-t);
            }else if d == 'R'{
                xmin = xmin.min((x as f64)+t);
                xmax = xmax.max((x as f64)+t);
                ymin = ymin.min(y as f64);
                ymax = ymax.max(y as f64);
            }else{
                xmin = xmin.min((x as f64)-t);
                xmax = xmax.max((x as f64)-t);
                ymin = ymin.min(y as f64);
                ymax = ymax.max(y as f64);                
            }
        }
        ans = ans.min((ymax - ymin).abs()*(xmax-xmin).abs())
    }
    println!("{}", ans);
}

fn set_time(time: &mut Vec<f64>, p: i64, q: i64, r: i64){
    time.push(((p as f64) - (r as f64)).abs()/2.0);
    time.push(((p as f64) - (q as f64)).abs());
    time.push(((q as f64) - (r as f64)).abs());
}
