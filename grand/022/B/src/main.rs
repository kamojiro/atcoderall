#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let N:usize = sc.read();
    if N == 3{
        println!("2 5 63");
        return
    }
    if N == 4{
        println!("2 5 20 63");
        return
    }
    let template: Vec< Vec<usize>> = vec![vec![],
                                          vec![3],
                                          vec![0,2],
                                          vec![0,2,3],
                                          vec![0,2,4,6],
                                          vec![0,1,2,3,5],
                                          vec![1,2,3,4,5,7],
                                          vec![0,1,2,3,4,5,6]
    ];
    let mut nums:Vec<usize> = vec![];
    for i in 0..5000{
        nums.push(i*6+2);
        nums.push(i*6+3);
        nums.push(i*6+4);
        nums.push(i*6+6);
    }
    nums.sort();
    let quotient = N/8;
    let remainder = N%8;
    let mut ans:String = "".to_string();
    for i in 0..quotient{
        for j in 0..8{
            ans.push(' ');
            ans.push_str(&nums[i*8+j].to_string());
        }
    }
    for i in 0..remainder{
        ans.push(' ');
        ans.push_str(&nums[quotient*8+template[remainder][i]].to_string());
    }
    println!("{}", ans.trim());
    //trimが合ってもなくても通る。時間も変わらない。


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


