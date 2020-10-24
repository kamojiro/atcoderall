#![allow(non_snake_case)]

use proconio::input;
fn main() {
    input!{
        N: usize,
        M: usize,
        _V: usize,
        P: usize,
        mut A: [usize; N],
    }
    A.sort();
    let pth_num = A[N-P];
    // let beforepth_num = pth_num;
    // let mut same_count = 0;
    let mut ans = 0;
    // let mut index = 0;
    for i in 0..N{
        let a = A[i];
        if a >= pth_num{
            ans += 1;
        }else{
            if pth_num - a <= M{
                ans += 1;
            }
        }
        // if a == pth_num{
        //     same_count += 1;
        // }
        // if a < pth_num{
        //     index = i;
        //     break
        // }
    }
    
    println!("{}", ans);
    
    
}
