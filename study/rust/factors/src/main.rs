fn factors(n: usize) -> Vec<usize>{
    //random sort
    if n == 1{
        return vec![1]
    }
    let possible = ((n as f64).sqrt() as usize) + 1;
    let mut ret:Vec<usize> = vec![];

    for i in 1..possible{
        if n%i == 0{
            if i == n/i{
                ret.push(i)
            }else{
                ret.push(i);
                ret.push(n/i);
            }
        }
    }
    ret
}

mod tests {
    use super::factors;

    #[test]
    fn factors1(){
        let mut factors = factors(1);
        factors.sort();
        assert_eq!(factors, vec![1]);
    }

    #[test]
    fn factors2(){
        let mut factors = factors(2);
        factors.sort();
        assert_eq!(factors, vec![1, 2]);
    }

    #[test]
    fn factors1_000_000_007(){
        let mut factors = factors(1_000_000_007);
        factors.sort();
        assert_eq!(factors, vec![1, 1_000_000_007]);
    }

    #[test]
    fn factors1024(){
        let mut factors = factors(1024);
        factors.sort();
        assert_eq!(factors, vec![1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]);
    }

    #[test]
    fn factors360(){
        let mut factors = factors(360);
        factors.sort();
        assert_eq!(factors, vec![1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360]);
    }

    #[test]
    fn factors57(){
        let mut factors = factors(57);
        factors.sort();
        assert_eq!(factors, vec![1, 3, 19, 57]);
    }

}
