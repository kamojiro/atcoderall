#![allow(non_snake_case)]
use proconio::{input, fastout};


fn mod_pow(x: i64, y: i64, z: i64) -> i64 {
    if y == 0 {
        1
    } else {
        let h = mod_pow(x, y / 2, z);
        let res = (h * h) % z;
        if y % 2 == 0 {
            res
        } else {
            (res * x) % z
        }
    }
}
#[fastout]
fn main() {
    input!{
        //N: i64,
        //array: [(usize,usize);N],
        H: usize,
        W: usize,
        T: [String;H],
    }
    let mut S:Vec<Vec<String>> = vec![];
    for i in 0..H{
        let v: Vec<char>= T[i].chars().collect();
        let mut w: Vec<String> = vec![];
        for j in 0..W{
            w.push(v[j].to_string());
        }
        S.push(w);
    }
    // println!("{:?}",S);
    let mut Lites:Vec<Vec<i64>> = vec![vec![0;W];H];
    let mut K: i64 = 0;
    let Q:i64 = 1000000007;
    for i in 0..H {
        let mut nums:i64 = 0;
        for j in 0..W{
            if S[i][j] == "#".to_string() {
                nums = 0;
                continue
            }
            K += 1;
            nums += 1;
            Lites[i][j] = nums;
        }
        // Println!("{:?}", Lites[i]);
        let mut now:i64 = -1;
        for j in (0..W).rev(){
            if Lites[i][j] == 0{
                now = -1;
                continue
            }
            // println!("{} {} {}",i,j, Lites[i][j] );
            if now == -1{
                now = Lites[i][j];
            }else{
                Lites[i][j] = now;
            }
        }
        // println!("{:?}",Lites );
    }
    // println!("{}", K);
    let mut TateLites:Vec<Vec<i64>> = vec![vec![0;W];H];
    for j in 0..W {
        let mut nums:i64 = 0;
        for i in 0..H{
            if S[i][j] == "#".to_string() {
                nums = 0;
                continue
            }
            nums += 1;
            TateLites[i][j] = nums;
        }
        let mut now:i64 = -1;
        for i in (0..H).rev(){
            if TateLites[i][j] == 0{
                now = -1;
                continue
            }
            if now == -1{
                now = TateLites[i][j];
            }else{
                TateLites[i][j] = now;
            }
        }
    }
    let mut ans:i64 = 0;
    for i in 0..H{
        for j in 0..W{
            if S[i][j] == ".".to_string(){
                let p:i64 = Lites[i][j] + TateLites[i][j]-1;
                ans += (mod_pow(2,p,Q)-1)*mod_pow(2,K-p,Q)%Q;
                // println!("{}",p);
                ans %= Q;
            }
        }
    }
    println!("{}", ans);

}
