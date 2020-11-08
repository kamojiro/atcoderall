#![allow(non_snake_case)]
use proconio::{input, fastout};
use rand::thread_rng;
use rand::seq::SliceRandom;

#[fastout]
fn main() {
    input!{
        N: usize,
    }
    let mut vec: Vec<usize> = Vec::new();
    for i in 0..N{
        vec.push(i);
    }
    let mut rng = thread_rng();
    println!("Unshuffled: {:?}", vec);
    for i in 0..N{
        vec.shuffle(&mut rng);
        println!("Shuffled {}:   {:?}",i, vec);

    }
    
}
