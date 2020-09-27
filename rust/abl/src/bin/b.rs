use proconio::input;

fn main() {
    input!{
        a: i64,
        b: i64,
        c: i64,
        d: i64,
    }
    if (b<c) || (d<a) {
        println!("No");
    }else{
        println!("Yes");
    }
}
