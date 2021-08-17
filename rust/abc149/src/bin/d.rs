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

use std::cmp::max;

#[fastout]
fn main() {
    input!{
        N: usize,
        K: usize,
        R: usize,
        S: usize,
        P: usize,
        T: Bytes,
    }
    let mut dp = vec![vec![0;3];N];
    for i in 0..K{
        if T[i] == b'r'{
            dp[i][2] = P;
        }else if T[i] == b's'{
            dp[i][0] = R;
        }else{
            dp[i][1] = S;
        }
    }
    for i in K..N{
        dp[i][0] = dp[i][0].max(max(dp[i-K][1], dp[i-K][2]));
        dp[i][1] = dp[i][1].max(max(dp[i-K][0], dp[i-K][2]));
        dp[i][2] = dp[i][2].max(max(dp[i-K][0], dp[i-K][1]));
        if T[i] == b'r'{
            dp[i][2] = dp[i][2].max(max(dp[i-K][0], dp[i-K][1])+P);
        }else if T[i] == b's'{
            dp[i][0] = dp[i][0].max(max(dp[i-K][1], dp[i-K][2])+R);
        }else{
            dp[i][1] = dp[i][1].max(max(dp[i-K][0], dp[i-K][2])+S);
        }        
    }
    let mut ans = 0;
    for i in (N-K)..N{
        ans += dp[i].iter().max().unwrap();
    }
    println!("{}", ans);
}
