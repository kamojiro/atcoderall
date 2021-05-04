#![allow(non_snake_case)]
use proconio::{input, fastout};

#[fastout]
fn main() {
    input!{
        X: i64,
    }
    println!("{}", 100-X%100);
}
