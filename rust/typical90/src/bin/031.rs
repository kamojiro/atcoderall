// -*- coding:utf-8-unix -*-
#![allow(non_snake_case)]

#[cfg(debug_assertions)]
#[allow(unused)]
macro_rules! debug_eprintln {
    ($p:tt, $($x:expr),*) => {
        eprintln!($p, $($x,)*);
    };
}
 
#[cfg(not(debug_assertions))]
#[allow(unused)]
macro_rules! debug_eprintln {
    ($p:tt, $($x:expr),*) => {};
}

use proconio::{fastout, input};

#[fastout]
fn main() {
    input!{
        N: usize,
        W: [usize; N],
        B: [usize; N],
    }
    let M = 50;
    let L = M + M*(M+1)/2;
    let mut grundy: Vec<Vec<usize>> = vec![vec![0; L+1]; M+1];
    for j in 2..=L{
        let b2 = j/2;
        // 遷移しうる状態が高々L/2 + 1くらいなので、mexはそれ以下
        let mut check_list = vec![true; L+1];
        for k in 1..=b2{
            check_list[grundy[0][j-k]] = false;
        }
        for (num, &exist) in check_list.iter().enumerate(){
            if exist{
                grundy[0][j] = num;
                break;
            }
        }
    }
    for i in 1..=M{
        grundy[i][0] = grundy[i-1][i].min(1)^1;
        grundy[i][1] = grundy[i-1][i+1].min(1)^1;
        for j in 2..=L{
            let b2 = j/2;
            let mut check_list = vec![true; L+1];
            if j+i <= L{
                check_list[grundy[i-1][j+i]] = false;
            }
            for k in 1..=b2{
                check_list[grundy[i][j-k]] = false;
            }
            for (num, &exist) in check_list.iter().enumerate(){
                if exist{
                    grundy[i][j] = num;
                    break;
                }
            }
        }
    }
    let mut ans = 0;
    for (&w,&b) in W.iter().zip(B.iter()){
        ans ^= grundy[w][b];
    }
    if ans == 0{
        println!("Second")
    }else{
        println!("First")
    }
}

// https://github.com/rust-lang-ja/ac-library-rs/tree/master/src

#[allow(unused)]
mod static_prime_modint {
    pub use crate::modint::*;
    pub trait NttFriendlyModulus<T>: StaticModulus<T>
    where
        T: NumAssignOps + PrimInt + Unsigned,
    {
        const ZETA: T;
        const MAX_NN_INDEX: usize;
    }
 
    #[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
    pub struct Mod10();
    impl StaticModulus<usize> for Mod10 {
        fn singleton() -> Self {
            Mod10()
        }
    }
    impl Modulus<usize> for Mod10 {
        fn modulus(&self) -> usize {
            1_000_000_007
        }
    }
 
    #[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
    pub struct Mod9();
    impl NttFriendlyModulus<usize> for Mod9 {
        const ZETA: usize = 15311432;
        const MAX_NN_INDEX: usize = 23;
    }
    impl StaticModulus<usize> for Mod9 {
        fn singleton() -> Self {
            Mod9()
        }
    }
    impl Modulus<usize> for Mod9 {
        fn modulus(&self) -> usize {
            998_244_353
        }
    }
 
    #[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
    pub struct Mod9_2();
    impl NttFriendlyModulus<usize> for Mod9_2 {
        const ZETA: usize = 79986183;
        const MAX_NN_INDEX: usize = 22;
    }
    impl StaticModulus<usize> for Mod9_2 {
        fn singleton() -> Self {
            Mod9_2()
        }
    }
    impl Modulus<usize> for Mod9_2 {
        fn modulus(&self) -> usize {
            998_244_353
        }
    }
 
    #[derive(Clone, Debug)]
    pub struct CombinatoricsTable<M>
    where
        M: StaticModulus<usize>,
    {
        factorial_table: Vec<ModInt<usize, M>>,
        factorial_inv_table: Vec<ModInt<usize, M>>,
        stirling_second_table: Vec<Vec<ModInt<usize, M>>>,
    }
    use std::convert::TryFrom;
    impl<M> CombinatoricsTable<M>
    where
        M: StaticModulus<usize>,
    {
        pub fn new(src_max: usize, dist_max: usize) -> Self {
            let mut factorial_table = vec![ModInt::new(1)];
            let mut factorial_inv_table = vec![ModInt::new(1)];
            for i in 1..=dist_max {
                factorial_table.push(ModInt::new(i) * factorial_table[i - 1]);
                factorial_inv_table.push(factorial_table[i].inverse());
            }
            let mut stirling_second_table: Vec<Vec<_>> = Vec::with_capacity(src_max + 1);
            for n in 0..=src_max {
                let mut st_temp = vec![ModInt::new(0); dist_max + 1];
                for k in 0..=dist_max {
                    if n == 0 && k == 0 {
                        st_temp[k] = ModInt::new(1);
                    } else if n == 0 || k == 0 {
                        st_temp[k] = ModInt::new(0);
                    } else {
                        st_temp[k] = ModInt::new(k) * stirling_second_table[n - 1][k]
                            + stirling_second_table[n - 1][k - 1];
                    }
                }
                stirling_second_table.push(st_temp);
            }
            CombinatoricsTable {
                factorial_table,
                factorial_inv_table,
                stirling_second_table,
            }
        }
        pub fn factorial(&self, n: usize) -> ModInt<usize, M> {
            if self.factorial_table.len() > n {
                return self.factorial_table[n];
            } else {
                panic!("factorial_table is not long enough");
            }
        }
        pub fn stirling_second(&self, n: usize, k: usize) -> ModInt<usize, M> {
            if self.stirling_second_table.len() > n && self.stirling_second_table[n].len() > k {
                return self.stirling_second_table[n][k];
            } else {
                panic!("stirling_second_table is not large enough");
            }
        }
        pub fn tw_any(&self, src: usize, dist: usize) -> ModInt<usize, M> {
            ModInt::new(dist).pow(src)
        }
        pub fn tw_inj(&self, src: usize, dist: usize) -> ModInt<usize, M> {
            if src > dist {
                ModInt::new(0)
            } else {
                self.factorial(dist) * self.factorial_inv_table[dist - src]
            }
        }
        pub fn tw_surj(&self, src: usize, dist: usize) -> ModInt<usize, M> {
            if src < dist {
                ModInt::new(0)
            } else {
                self.factorial(dist) * self.stirling_second(src, dist)
            }
        }
        pub fn tw_inj_srcsym(&self, src: usize, dist: usize) -> ModInt<usize, M> {
            if src > dist {
                ModInt::new(0)
            } else {
                self.factorial(dist)
                    * self.factorial_inv_table[src]
                    * self.factorial_inv_table[dist - src]
            }
        }
    }
 
    // Number-theoretic transformation
    // The length of f must be a power of 2
    // and zeta must be a primitive f.len()-th root of unity
    // The inverse can be calculated by doing the same
    // with the original zeta's inverse as zeta
    // and dividing by f.len()
    pub fn number_theoretic_transformation<T, M>(
        f: &[ModInt<T, M>],
        zeta: ModInt<T, M>,
    ) -> Vec<ModInt<T, M>>
    where
        M: StaticModulus<T>,
        T: NumAssignOps + PrimInt + Unsigned,
    {
        // bit-reversal
        let bit_colength = f.len().leading_zeros() + 1;
        let mut f_rev: Vec<ModInt<T, M>> = vec![ModInt::new(T::zero()); f.len()];
        for i in 0..f.len() {
            f_rev[i.reverse_bits() >> bit_colength] = f[i];
        }
        sub(&mut f_rev, zeta);
        return f_rev;
        fn sub<T, M>(f: &mut [ModInt<T, M>], zeta: ModInt<T, M>)
        where
            M: StaticModulus<T>,
            T: NumAssignOps + PrimInt + Unsigned,
        {
            let n = f.len();
            if n == 1 {
                return;
            }
            sub(&mut f[..n / 2], zeta * zeta);
            sub(&mut f[n / 2..], zeta * zeta);
            let mut pow_zeta = ModInt::new(T::one());
            for i in 0..n / 2 {
                let g0 = f[i];
                let g1 = f[i + n / 2];
                f[i] = g0 + pow_zeta * g1;
                f[i + n / 2] = g0 - pow_zeta * g1;
                pow_zeta = pow_zeta * zeta;
            }
        }
    }
 
    // convolution function
    pub fn convolution<M>(aa: &[ModInt<usize, M>], bb: &[ModInt<usize, M>]) -> Vec<ModInt<usize, M>>
    where
        M: NttFriendlyModulus<usize>,
    {
        let mut a: Vec<_> = aa.iter().cloned().collect();
        let mut b: Vec<_> = bb.iter().cloned().collect();
        let mut nn = 1;
        let mut nn_index = 0;
        while nn < aa.len() + bb.len() - 1 {
            nn *= 2;
            nn_index += 1;
        }
        while a.len() < nn {
            a.push(ModInt::new(0));
        }
        while b.len() < nn {
            b.push(ModInt::new(0));
        }
        debug_assert!(nn_index <= M::MAX_NN_INDEX);
        let mut zeta = ModInt::new(M::ZETA); // a primitive 2^MAX_NN_INDEX-th root of unity
        while nn_index < M::MAX_NN_INDEX {
            zeta = zeta * zeta;
            nn_index += 1;
        }
        // Now zeta is a primitive nn-th root of unity
        let ahat = number_theoretic_transformation(&a, zeta);
        let bhat = number_theoretic_transformation(&b, zeta);
        let mut chat = Vec::new();
        for i in 0..nn {
            chat.push(ahat[i] * bhat[i]);
        }
        let mut c = number_theoretic_transformation(&chat, ModInt::new(1) * zeta.inverse());
        for ci in &mut c {
            *ci = *ci * ModInt::new(nn).inverse();
        }
        // Now c is the convolution
        for i in aa.len() + bb.len() - 1..c.len() {
            debug_assert!(c[i] == ModInt::new(0));
        }
        c.resize(aa.len() + bb.len() - 1, ModInt::new(0));
        return c;
    }
}
 
#[allow(unused)]
mod dynamic_modint {
    use crate::gcd;
    pub use crate::modint::*;
    // For a = aa mod m,
    // it computes (g mod m, b mod m),
    // that satisfies g = gcd(aa,m) and aa*b = g mod m
    pub fn inv_gcd<T>(am: ModInt<T, ModDyn<T>>) -> (ModInt<T, ModDyn<T>>, ModInt<T, ModDyn<T>>)
    where
        T: PrimInt + Unsigned + NumAssignOps,
    {
        let a = am.value();
        let m = am.modulus();
        if m % a == T::zero() {
            return (am, ModInt::new_with(T::one(), m));
        }
        let q = m / a;
        let r = m % a;
        let (ga, xa) = inv_gcd(ModInt::new_with(r, a));
        let g = ga.value();
        let gm = ModInt::new_with(g, m);
        let x = xa.value();
        if r * x > g {
            let y = (r * x - g) / a;
            let z = (q * x + y) % m;
            let zm = ModInt::new_with(T::zero(), m) - ModInt::new_with(z, m);
            debug_assert!(am * zm == gm);
            return (gm, zm);
        } else {
            let y = (g - r * x) / a;
            let zm = ModInt::new_with(y, m) - ModInt::new_with((q * x) % m, m);
            debug_assert!(am * zm == gm);
            return (gm, zm);
        }
    }
 
    // Two-term Chinese remainder theorem function
    pub fn crt<T>(
        am: ModInt<T, ModDyn<T>>,
        bmm: ModInt<T, ModDyn<T>>,
    ) -> Option<ModInt<T, ModDyn<T>>>
    where
        T: PrimInt + Unsigned + NumAssignOps,
    {
        let a = am.value();
        let m = am.modulus();
        let b = bmm.value();
        let mm = bmm.modulus();
        if m == mm {
            if a == b {
                return Some(am);
            } else {
                return None;
            }
        } else if m > mm {
            return crt(bmm, am);
        } else {
            // m < mm
            let (dmm, xmm) = inv_gcd(ModInt::new_with(m, mm));
            let d = dmm.value();
            debug_assert!(d == gcd(m, mm));
            let x = xmm.value();
            return crt_internal(a, b, m, mm, d, x);
        }
    }
 
    // Two-slice Chinese remainder theorem function
    // It assumes all the moduli are equal for each slice
    pub fn crt_slice<T>(
        a: &[ModInt<T, ModDyn<T>>],
        b: &[ModInt<T, ModDyn<T>>],
    ) -> Vec<Option<ModInt<T, ModDyn<T>>>>
    where
        T: PrimInt + Unsigned + NumAssignOps,
    {
        let mut result = vec![];
        if a.len() == 0 || a.len() != b.len() {
            return result;
        }
        // Now a.len() == b.len() >= 1
        result.reserve(a.len());
        let m = a[0].modulus();
        let mm = b[0].modulus();
        if m == mm {
            for i in 0..a.len() {
                if a[i].value() == b[i].value() {
                    result.push(Some(a[i]));
                } else {
                    result.push(None);
                }
            }
        } else if m > mm {
            return crt_slice(b, a);
        } else {
            // m < mm
            let (dmm, xmm) = inv_gcd(ModInt::new_with(m, mm));
            let d = dmm.value();
            debug_assert!(d == gcd(m, mm));
            let x = xmm.value();
            for i in 0..a.len() {
                result.push(crt_internal(a[i].value(), b[i].value(), m, mm, d, x));
                // if let Some(cmmm) = crt_internal(a[i].value(), b[i].value(), m, mm, d, x) {
                //     result.push(cmmm);
                // } else {
                //     return None;
                // }
            }
        }
        return result;
    }
 
    fn crt_internal<T>(a: T, b: T, m: T, mm: T, d: T, x: T) -> Option<ModInt<T, ModDyn<T>>>
    where
        T: PrimInt + Unsigned + NumAssignOps,
    {
        if a % d != b % d {
            return None;
        }
        let mmm = m * mm / d;
        if a == b {
            return Some(ModInt::new_with(a, mmm));
        } else if a < b {
            let y = (b - a) / d;
            let ans =
                ModInt::new_with(a, mmm) + ModInt::new_with(m * x, mmm) * ModInt::new_with(y, mmm);
            debug_assert!(ans.value() % m == a);
            debug_assert!(ans.value() % mm == b);
            return Some(ans);
        } else {
            // a > b
            let y = (a - b) / d;
            let ans =
                ModInt::new_with(a, mmm) - ModInt::new_with(m * x, mmm) * ModInt::new_with(y, mmm);
            debug_assert!(ans.value() % m == a);
            debug_assert!(ans.value() % mm == b);
            return Some(ans);
        }
    }
 
    // Helper function for number-theoretic transformation
    // lists Proth primes of the form
    // p = k * 2^n + 1
    // in the form
    // n k p a zeta.
    // zeta = a^k is a primitive 2^n-th root of unity in mod p.
    pub fn list_proth_primes(min: usize, max: usize) {
        for n in 1..64 {
            let two_n = 1 << n;
            if two_n >= max {
                break;
            }
            for k0 in 1..=(two_n / 2) {
                let k = 2 * k0 - 1;
                let p = k * two_n + 1;
                if p > max {
                    break;
                }
                if p < min {
                    continue;
                }
                let alist = vec![2, 3, 5, 7, 11, 13, 17, 19];
                for a in alist {
                    if a >= p {
                        break;
                    }
                    let sym = ModInt::new_with(a as u128, p as u128).pow((p - 1) / 2);
                    if sym.value() == (p - 1) as u128 {
                        let zeta = ModInt::new_with(a as u128, p as u128).pow(k);
                        println!("{} {} {} {} {}", n, k, p, a, zeta.value());
                        break;
                    }
                }
            }
        }
    }
 
    pub fn check_powers(a: usize, p: usize, n: usize) {
        let mut aa = ModInt::new_with(a as u128, p as u128);
        for i in 0..n {
            println!("{} times: {}", i, aa.value());
            aa = aa * aa;
        }
    }
 
    // Calculate the smallest primitive root mod p
    // and the corresponding discrete logarithm table
    // The argument p must be a prime
    // The dlog of a is in table[a-1]
    // Time: O(p)
    pub fn primitive_root(p: usize) -> (usize, Vec<usize>) {
        // discrete_logarithm[a-1] = the dlog of a
        // or 0 if a hasn't been occurred
        let mut discrete_logarithm = vec![0; p - 1];
        if p == 2 {
            return (1, discrete_logarithm);
        }
        'a_loop: for a in 2..p {
            if discrete_logarithm[a - 1] != 0 {
                continue;
            }
            discrete_logarithm[a - 1] = 1;
            let mut a_power = ModInt::new_with(a, p);
            // calculate a^2 to a^(p-2)
            for i in 2..p - 1 {
                a_power = a_power * ModInt::new_with(a, p);
                if a_power.value() == 1 {
                    continue 'a_loop;
                }
                discrete_logarithm[a_power.value() - 1] = i;
            }
            return (a, discrete_logarithm);
        }
        panic!();
    }
}
 
#[allow(unused)]
mod modint {
    pub use num_traits::{NumAssignOps, PrimInt, Unsigned};
    use std::ops::{Add, AddAssign, Div, Mul, MulAssign, Sub, SubAssign};
 
    pub trait Modulus<T>: Copy + Eq
    where
        T: NumAssignOps + PrimInt + Unsigned,
    {
        fn modulus(&self) -> T;
    }
 
    #[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
    pub struct ModDyn<T>(T);
    impl<T> Modulus<T> for ModDyn<T>
    where
        T: NumAssignOps + PrimInt + Unsigned,
    {
        fn modulus(&self) -> T {
            self.0
        }
    }
 
    #[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
    pub struct ModInt<T, M>(T, M)
    where
        M: Modulus<T>,
        T: NumAssignOps + PrimInt + Unsigned;
    pub trait StaticModulus<T>: Modulus<T>
    where
        T: NumAssignOps + PrimInt + Unsigned,
    {
        fn singleton() -> Self;
    }
    impl<T, M> ModInt<T, M>
    where
        M: StaticModulus<T>,
        T: NumAssignOps + PrimInt + Unsigned,
    {
        pub fn new(x: T) -> Self {
            ModInt(x % M::singleton().modulus(), M::singleton())
        }
    }
    impl<T> ModInt<T, ModDyn<T>>
    where
        T: NumAssignOps + PrimInt + Unsigned,
    {
        pub fn new_with(x: T, m: T) -> Self {
            ModInt(x % m, ModDyn(m))
        }
        pub fn modulus(&self) -> T {
            self.1.modulus()
        }
    }
    impl<T, M> ModInt<T, M>
    where
        M: Modulus<T>,
        T: NumAssignOps + PrimInt + Unsigned,
    {
        pub fn value(&self) -> T {
            self.0
        }
        pub fn pow(&self, index: usize) -> Self {
            if index == 0 {
                return ModInt(T::one(), self.1);
            } else {
                if index % 2 == 0 {
                    let half = self.pow(index / 2);
                    return half * half;
                } else {
                    let half = self.pow(index / 2);
                    return half * half * *self;
                }
            }
        }
    }
    impl<M> ModInt<usize, M>
    where
        M: StaticModulus<usize>,
    {
        pub fn inverse(&self) -> Self {
            self.pow(self.1.modulus() - 2)
        }
    }
 
    impl<T, M> AddAssign<T> for ModInt<T, M>
    where
        M: Modulus<T>,
        T: NumAssignOps + PrimInt + Unsigned,
    {
        fn add_assign(&mut self, rhs: T) {
            self.0 += rhs % self.1.modulus();
            self.0 %= self.1.modulus();
        }
    }
    impl<T, M> AddAssign for ModInt<T, M>
    where
        M: Modulus<T>,
        T: NumAssignOps + PrimInt + Unsigned,
    {
        fn add_assign(&mut self, rhs: Self) {
            self.0 += rhs.0;
            self.0 %= self.1.modulus();
        }
    }
    impl<T, M> SubAssign<T> for ModInt<T, M>
    where
        M: Modulus<T>,
        T: NumAssignOps + PrimInt + Unsigned,
    {
        fn sub_assign(&mut self, rhs: T) {
            self.0 += self.1.modulus();
            self.0 -= rhs % self.1.modulus();
            self.0 %= self.1.modulus();
        }
    }
    impl<T, M> SubAssign for ModInt<T, M>
    where
        M: Modulus<T>,
        T: NumAssignOps + PrimInt + Unsigned,
    {
        fn sub_assign(&mut self, rhs: Self) {
            self.0 += self.1.modulus();
            self.0 -= rhs.0;
            self.0 %= self.1.modulus();
        }
    }
    impl<T, M> MulAssign<T> for ModInt<T, M>
    where
        M: Modulus<T>,
        T: NumAssignOps + PrimInt + Unsigned,
    {
        fn mul_assign(&mut self, rhs: T) {
            self.0 *= (rhs % self.1.modulus());
            self.0 %= self.1.modulus();
        }
    }
    impl<T, M> MulAssign for ModInt<T, M>
    where
        M: Modulus<T>,
        T: NumAssignOps + PrimInt + Unsigned,
    {
        fn mul_assign(&mut self, rhs: Self) {
            self.0 *= rhs.0;
            self.0 %= self.1.modulus();
        }
    }
    macro_rules! impl_op_from_opassign {
        ($op:ident, $opname:ident, $opassignmane:ident, $rhstype:ident) => {
            impl<T, M> $op<$rhstype> for ModInt<T, M>
            where
                M: Modulus<T>,
                T: NumAssignOps + PrimInt + Unsigned,
            {
                type Output = Self;
                fn $opname(self, rhs: $rhstype) -> Self {
                    let mut temp = self.clone();
                    temp.$opassignmane(rhs);
                    temp
                }
            }
        };
    }
    impl_op_from_opassign!(Add, add, add_assign, T);
    impl_op_from_opassign!(Sub, sub, sub_assign, T);
    impl_op_from_opassign!(Mul, mul, mul_assign, T);
    impl_op_from_opassign!(Add, add, add_assign, Self);
    impl_op_from_opassign!(Sub, sub, sub_assign, Self);
    impl_op_from_opassign!(Mul, mul, mul_assign, Self);
}
 
// Binary search for closures
// returns the value i where f(i) == true but f(i+1) == false
// if forall i f(i) == true, returns max_value
#[allow(dead_code)]
fn closure_binary_search<T>(f: T, min_value: usize, max_value: usize) -> usize
where
    T: Fn(usize) -> bool,
{
    if !f(min_value) {
        panic!("Check the condition for closure_binary_search()");
    }
    if f(max_value) {
        return max_value;
    }
    let mut min_value = min_value;
    let mut max_value = max_value;
    while min_value + 1 < max_value {
        let check_value = min_value + (max_value - min_value) / 2;
        if f(check_value) {
            min_value = check_value;
        } else {
            max_value = check_value;
        }
    }
    return min_value;
}
 
// Iterator of proper subsets
// Caution: it does NOT starts with the universal set itself!
struct SubsetIterator {
    universal_set: usize,
    last_set: usize,
}
#[allow(dead_code)]
impl SubsetIterator {
    fn new(universal_set: usize) -> Self {
        SubsetIterator {
            universal_set,
            last_set: universal_set,
        }
    }
}
impl Iterator for SubsetIterator {
    type Item = usize;
    fn next(&mut self) -> Option<Self::Item> {
        if self.last_set == 0 {
            return None;
        } else {
            self.last_set -= 1;
            self.last_set &= self.universal_set;
            return Some(self.last_set);
        }
    }
}
 
#[derive(Debug, Clone)]
struct EquivalenceRelation {
    parent: Vec<std::cell::Cell<usize>>,
    size: Vec<usize>,
}
 
#[allow(dead_code)]
impl EquivalenceRelation {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(std::cell::Cell::new(i));
        }
        let size = vec![1; n];
        return Self { parent, size };
    }
 
    fn make_equivalent(&mut self, a: usize, b: usize) {
        let volume = self.parent.len();
        if a >= volume || b >= volume {
            panic!(
                "Tried to make {} and {} equivalent but there are only {} elements",
                a, b, volume
            );
        }
        let aa = self.find(a);
        let bb = self.find(b);
        if aa == bb {
            return;
        }
        let aasize = self.size[aa];
        let bbsize = self.size[bb];
        if aasize > bbsize {
            self.parent[bb].set(aa);
            self.size[aa] = aasize + bbsize;
        } else {
            self.parent[aa].set(bb);
            self.size[bb] = aasize + bbsize;
        }
    }
 
    fn find(&self, a: usize) -> usize {
        let volume = self.parent.len();
        if a >= volume {
            panic!("Tried to find {} but there are only {} elements", a, volume);
        }
        let b = self.parent[a].get();
        if b == a {
            return a;
        } else {
            let c = self.find(b);
            self.parent[a].set(c);
            return c;
        }
    }
 
    fn are_equivalent(&self, a: usize, b: usize) -> bool {
        return self.find(a) == self.find(b);
    }
 
    fn size(&self, a: usize) -> usize {
        self.size[self.find(a)]
    }
}
 
// Segment tree for range minimum query and alike problems
// The closures must fulfill the defining laws of monoids
// Indexing is 0-based
// The code is based on that in C++ in the 'ant book'
#[derive(Clone, PartialEq, Debug)]
struct SegmentTree<A, CUnit, CMult> {
    data: Vec<A>,
    monoid_unit_closure: CUnit,
    monoid_op_closure: CMult,
}
 
#[allow(dead_code)]
impl<A, CUnit, CMult> SegmentTree<A, CUnit, CMult>
where
    A: Copy,
    CUnit: Fn() -> A,
    CMult: Fn(A, A) -> A,
{
    fn new(n: usize, monoid_unit_closure: CUnit, monoid_op_closure: CMult) -> Self {
        let mut nn = 1;
        while nn < n {
            nn *= 2;
        }
        let this = Self {
            data: vec![monoid_unit_closure(); 2 * nn - 1],
            monoid_unit_closure,
            monoid_op_closure,
        };
        return this;
    }
 
    fn from_slice(sl: &[A], monoid_unit_closure: CUnit, monoid_op_closure: CMult) -> Self {
        let n = sl.len();
        let mut nn = 1;
        while nn < n {
            nn *= 2;
        }
        let mut data = vec![monoid_unit_closure(); 2 * nn - 1];
        for k in 0..n {
            data[k + nn - 1] = sl[k];
        }
        if n >= 2 {
            for j in (0..=(n + nn - 3) / 2).rev() {
                data[j] = (monoid_op_closure)(data[j * 2 + 1], data[j * 2 + 2]);
            }
        }
        Self {
            data,
            monoid_unit_closure,
            monoid_op_closure,
        }
    }
 
    fn update(&mut self, k: usize, a: A) {
        let n = (self.data.len() + 1) / 2;
        let mut k = k + n - 1;
        self.data[k] = a;
        while k > 0 {
            k = (k - 1) / 2;
            self.data[k] = (self.monoid_op_closure)(self.data[k * 2 + 1], self.data[k * 2 + 2]);
        }
    }
 
    fn query_internal(&self, a: usize, b: usize, k: usize, l: usize, r: usize) -> A {
        if r <= a || b <= l {
            return (self.monoid_unit_closure)();
        }
        if a <= l && r <= b {
            return self.data[k];
        } else {
            let vl = self.query_internal(a, b, k * 2 + 1, l, (l + r) / 2);
            let vr = self.query_internal(a, b, k * 2 + 2, (l + r) / 2, r);
            return (self.monoid_op_closure)(vl, vr);
        }
    }
}
 
trait RangeQuery<T> {
    type Output;
    fn query(&self, r: T) -> Self::Output;
}
 
use std::ops::Range;
 
#[allow(dead_code)]
impl<A, CUnit, CMult> RangeQuery<Range<usize>> for SegmentTree<A, CUnit, CMult>
where
    A: Copy,
    CUnit: Fn() -> A,
    CMult: Fn(A, A) -> A,
{
    type Output = A;
    fn query(&self, range: Range<usize>) -> A {
        let n = (self.data.len() + 1) / 2;
        return self.query_internal(range.start, range.end, 0, 0, n);
    }
}
 
#[allow(dead_code)]
fn divisors(n: u64) -> Vec<u64> {
    let mut divisors = Vec::new();
    for d in 1..=n {
        if d * d > n {
            break;
        }
        if n % d != 0 {
            continue;
        }
        divisors.push(d);
        if n / d != d {
            divisors.push(n / d);
        }
    }
    return divisors;
}
 
use num_traits::PrimInt;
#[allow(dead_code)]
fn gcd<T>(a: T, b: T) -> T
where
    T: PrimInt,
{
    if a < b {
        return gcd(b, a);
    } else if b == T::zero() {
        return a;
    } else {
        return gcd(b, a % b);
    }
}
 
use num_traits::Unsigned;
// Sum of floor((ai+b)/m) for i = 0..=n-1
// based on the (new) editorial of practice2-c
#[allow(dead_code)]
fn floor_sum<T>(n: T, m: T, a: T, b: T) -> T
where
    T: PrimInt + Unsigned,
{
    if n == T::zero() {
        return T::zero();
    }
    if a >= m || b >= m {
        return floor_sum(n, m, a % m, b % m)
            + (b / m) * n
            + (a / m) * n * (n - T::one()) / (T::one() + T::one());
    }
    // a, b < m
    if a == T::zero() {
        return T::zero();
    }
    // 0<a<m, 0<=b<m
    let y = (a * n + b) / m;
    let z = (a * n + b) % m;
    // a*n+b = y*m+z
    return floor_sum(y, a, m, z);
}
