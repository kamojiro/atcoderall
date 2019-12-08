#![allow(non_snake_case)]

fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let H:usize = sc.read();
    let W:usize = sc.read();
    let A:Vec< Vec< i64>> = (0..H).map(|_| sc.vec(W)).collect();
    let B:Vec< Vec< i64>> = (0..H).map(|_| sc.vec(W)).collect();
    let mut C:Vec< Vec<i64>> = vec![vec![0; W]; H];
    for i in 0..H{
        for j in 0..W{
            C[i][j] = A[i][j] - B[i][j];
        }
    }
    let R:usize = 2*(80+80)*80+1;
    let M:i64 = (80+80)*80;

    let mut ANS:Vec<Vec< Vec< bool>>> = vec![vec![vec![false; R]; W]; H];
    ANS[0][0][(C[0][0]+M) as usize] = true;
    for i in 0..H{
//        println!("b {}", i);
        for j in 0..W{
            for k in 0..R{
                if !ANS[i][j][k] {
//                    println!("{}", j);
                    continue
                }
//                println!("{} {}", i, j);
                if i + 1 < H{
//                    println!("hoge");
                    ANS[i+1][j][((k as i64) + C[i+1][j]) as usize] = true;
                    ANS[i+1][j][((k as i64) - C[i+1][j]) as usize] = true;
                }
                if j + 1 < W{
//                    println!("a{} {}",i, j );
                    ANS[i][j+1][((k as i64) + C[i][j+1]) as usize] = true;
                    ANS[i][j+1][((k as i64) - C[i][j+1]) as usize] = true;
//                    println!("hee");
                }
            }
        }
    }
//    println!("hoge");
//         for k in 0..R{
// //            println!("hoge");
//             if !ANS[i][k]{
//                 continue
//             }
//             println!("{} {}",i, k as i64 - M as i64);
//             for j in 0..W{
//                 ANS[i+1][((k as i64) + C[i][j]) as usize] = true;
//             }
//         }
//     }
//     let M:i64 = M as i64;

    let mut ans:i64 = R as i64;
    for i in 0..R{
        if ANS[H-1][W-1][i]{
//            println!("{}", i as i64 - M);
            if ((i as i64) - M).abs() < ans{
                ans = ((i as i64) - M).abs();
            }
        }
    }

    println!("{}", ans);


}

pub struct Scanner<R> {
    stdin: R,
}

impl<R: std::io::Read> Scanner<R> {
    pub fn read<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        let buf = self
            .stdin
            .by_ref()
            .bytes()
            .map(|b| b.unwrap())
            .skip_while(|&b| b == b' ' || b == b'\n')
            .take_while(|&b| b != b' ' && b != b'\n')
            .collect::<Vec<_>>();
        unsafe { std::str::from_utf8_unchecked(&buf) }
        .parse()
            .ok()
            .expect("Parse error.")
    }
    pub fn vec<T: std::str::FromStr>(&mut self, n: usize) -> Vec<T> {
        (0..n).map(|_| self.read()).collect()
    }
    pub fn chars(&mut self) -> Vec<char> {
        self.read::<String>().chars().collect()
    }
}


