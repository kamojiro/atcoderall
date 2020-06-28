#![allow(non_snake_case)]

fn main() {
    // let s = std::io::stdin();
    // let mut sc = Scanner { stdin: s.lock() };
    let (r, w) = (std::io::stdin(), std::io::stdout());
    let mut sc = IO::new(r.lock(), w.lock());
    let D:usize = sc.read();
    let C:Vec<i64> = sc.vec(26);
    let S: Vec<Vec<i64>> = (0..D).map(|_| sc.vec(26)).collect();
    let mut past: Vec<i64> = (0..26).map(|_| -1).collect();
    let mut ANS:Vec<usize> = Vec::new();
    let mut point:i64 = 0;
    for i in 0..D{
        let mut m:i64 = -1000000000;
        let mut ind:usize = 0;
        for j in 0..26{
            let mut temp_point:i64 = point+S[i][j];
            for k in 0..26{
                if k == j{
                    continue
                }
                temp_point -= C[k]*((i as i64)-past[k]);
            }
            if m < temp_point{
                ind = j;
                m = temp_point;
            }
        }
        ANS.push(ind);
        point = m;
        past[ind] = i as i64;
    }
    let deadline = D;
    let times = 5;
    for _ in 0..times{
        for i in 0..deadline{
            let oldest:usize = ANS[i];
            for j in 0..26{
                if j == oldest {
                    continue
                }
                let old = ANS[i];
                ANS[i] = j;
                let temp_point = check_point(D,&S,&ANS,&C);
                if point < temp_point{
                    // println!("!!!!!! {} < {}",point, temp_point);
                    point = temp_point;
                }else{
                    ANS[i] = old;
                }
            }
        }
    }

    let mut ANS_1:Vec<usize> = Vec::new();
    for i in 0..D{
        let mut m = 0;
        let mut ind = 0;
        for j in 0..26{
            if m < S[i][j]{
                m = S[i][j];
                ind = j;
            }
        }
        ANS_1.push(ind);
    }

    let deadline = D;
    let times = 0;
    let mut point_1 = check_point(D,&S,&ANS_1,&C);
    for _ in 0..times{
        for i in 0..deadline{
            let oldest:usize = ANS_1[i];
            for j in 0..26{
                if j == oldest {
                    continue
                }
                let old = ANS_1[i];
                ANS_1[i] = j;
                let temp_point = check_point(D,&S,&ANS_1,&C);
                if point_1 < temp_point{
                    // println!("!!!!!! {} < {}",point, temp_point);
                    point_1 = temp_point;
                }else{
                    ANS_1[i] = old;
                }
            }
        }
    }

    let mut ANS_2:Vec<usize> = Vec::new();
    let mut ind = 0;
    let mut m = C[0];
    for i in 1..26{
        if C[i] < m{
            ind = i;
            m = C[i];
        }
    }
    for _ in 0..D{
        ANS_2.push(ind);
    }

    let deadline = D;
    let times = 0;
    let mut point_2 = check_point(D,&S,&ANS_2,&C);
    for _ in 0..times{
        for i in 0..deadline{
            let oldest:usize = ANS_2[i];
            for j in 0..26{
                if j == oldest {
                    continue
                }
                let old = ANS_2[i];
                ANS_2[i] = j;
                let temp_point = check_point(D,&S,&ANS_2,&C);
                if point_2 < temp_point{
                    // println!("!!!!!! {} < {}",point, temp_point);
                    point_2 = temp_point;
                }else{
                    ANS_2[i] = old;
                }
            }
        }
    }

    
    if (point > point_1) && (point > point_2){
        for i in 0..D{
            println!("{}", ANS[i]+1);
        }
    }else if point_1 > point_2{
        for i in 0..D{
            println!("{}", ANS_1[i]+1);
        }        
    }else{
        for i in 0..D{
            println!("{}", ANS_2[i]+1);
        }        
        
    }
    // for i in 0..D{
    //     ans += S[i][T[i]-1];
    //     past[T[i]-1] = i as i64;
    //     for j in 0..26{
    //         ans -= C[j]*((i as i64)-past[j]);
    //     }
    //     println!("{}", ans);
    // }
}

fn check_point(D:usize, S:&Vec<Vec<i64>>, T:&Vec<usize>,C:&Vec<i64>) -> i64{
    let mut ans:i64 = 0;
    let mut past: Vec<i64> = (0..26).map(|_| -1).collect();
    for i in 0..D{
        ans += S[i][T[i]];
        past[T[i]] = i as i64;
        for j in 0..26{
            ans -= C[j]*((i as i64)-past[j]);
        }
    }
    ans
}

struct IO<R, W: std::io::Write>(R, std::io::BufWriter<W>);


impl<R: std::io::Read, W: std::io::Write> IO<R, W> {
    pub fn new(r: R, w: W) -> Self {
        Self(r, std::io::BufWriter::new(w))
    }
    pub fn read<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        let buf = self
            .0
            .by_ref()
            .bytes()
            .map(|b| b.unwrap())
            .skip_while(|&b| b == b' ' || b == b'\n' || b == b'\r' || b == b'\t')
            .take_while(|&b| b != b' ' && b != b'\n' && b != b'\r' && b != b'\t')
            .collect::<Vec<_>>();
        unsafe { std::str::from_utf8_unchecked(&buf) }
        .parse()
            .ok()
            .expect("Parse error.")
    }
    pub fn vec<T: std::str::FromStr>(&mut self, n: usize) -> Vec<T> {
        (0..n).map(|_| self.read()).collect()
    }
}



