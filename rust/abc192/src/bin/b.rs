#![allow(non_snake_case)]
use proconio::{input, fastout};
use proconio::marker::{Chars};

#[fastout]
fn main() {
    input!{
        chars: Chars,
        //N: i64,
        //array: [(usize,usize);N],
    }
    for i in 0..chars.len(){
        if i%2 == 0{
            if chars[i].is_uppercase(){
                println!("No");
                return
            }
        }else{
            if chars[i].is_lowercase(){
                println!("No");
                return
            }
        }
    }
    println!("Yes");
}
