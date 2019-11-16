fn prime(n:usize) -> bool{
    if n == 1{
        return false
    }
    let possible = ((n as f64).sqrt() as usize) + 1;
    for i in 2..possible{
        if n%i == 0{
            return false
        }
    }

    true
}

#[cfg(test)]
mod tests {
    use super::prime;

    #[test]
    fn prime1(){
        assert_eq!(prime(1), false);
    }
    
    #[test]
    fn prime2(){
        assert_eq!(prime(2), true);
    }

    #[test]
    fn prime3(){
        assert_eq!(prime(3), true);
    }

    #[test]
    fn prime4(){
        assert_eq!(prime(4), false);
    }

    #[test]
    fn prime1_000_000_007(){
        assert_eq!(prime(1_000_000_007), true);
    }

    #[test]
    fn prime1_000_000(){
        assert_eq!(prime(1_000_000), false);
    }

    
    
}
