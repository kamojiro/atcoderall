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
    input! {
        W: usize,
        N: usize,
        LR: [(usize, usize); N],
        //array: [(usize,usize);N],
    }
    let mut lazy_segment_tree = LazySegmentTree::new(W + 1, || 0, |x, y| x.max(y));
    for (l, r) in LR {
        let t = lazy_segment_tree.query(l..(r + 1));
        println!("{}", t + 1);
        lazy_segment_tree.update(l..(r + 1), t + 1);
    }
}

// Lazy segment tree for range query and range update, alike problems
// The closures must fulfill the defining laws of monoids
// Indexing is 0-based
// The code is based on the following web site.
// https://algo-logic.info/segment-tree/
#[derive(Clone, PartialEq, Debug)]
struct LazySegmentTree<A, CUnit, CMult> {
    data: Vec<A>,
    lazy: Vec<A>,
    monoid_unit_closure: CUnit,
    monoid_op_closure: CMult,
}

#[allow(dead_code)]
impl<A, CUnit, CMult> LazySegmentTree<A, CUnit, CMult>
where
    A: Copy + std::cmp::Eq,
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
            lazy: vec![monoid_unit_closure(); 2 * nn - 1],
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
        let lazy = vec![monoid_unit_closure(); 2 * nn - 1];
        Self {
            data,
            lazy,
            monoid_unit_closure,
            monoid_op_closure,
        }
    }

    fn eval(&mut self, k: usize) {
        if self.lazy[k] == (self.monoid_unit_closure)() {
            return;
        }
        let n = (self.lazy.len() + 1) / 2;
        if k < n - 1 {
            self.lazy[k * 2 + 1] = self.lazy[k];
            self.lazy[k * 2 + 2] = self.lazy[k];
        }
        self.data[k] = self.lazy[k];
        self.lazy[k] = (self.monoid_unit_closure)();
    }

    fn sub_update(&mut self, a: usize, b: usize, x: A, k: usize, l: usize, r: usize) {
        self.eval(k);
        if a <= l && r <= b {
            self.lazy[k] = x;
            self.eval(k);
        } else if a < r && l < b {
            self.sub_update(a, b, x, k * 2 + 1, l, (l + r) / 2);
            self.sub_update(a, b, x, k * 2 + 2, (l + r) / 2, r);
            self.data[k] = (self.monoid_op_closure)(self.data[k * 2 + 1], self.data[k * 2 + 2]);
        }
    }

    fn update_internal(&mut self, a: usize, b: usize, x: A) {
        let n = (self.lazy.len() + 1) / 2;
        self.sub_update(a, b, x, 0, 0, n)
    }

    fn sub_query_internal(&mut self, a: usize, b: usize, k: usize, l: usize, r: usize) -> A {
        self.eval(k);
        if r <= a || b <= l {
            (self.monoid_unit_closure)()
        } else if a <= l && r <= b {
            self.data[k]
        } else {
            let vl = self.sub_query_internal(a, b, k * 2 + 1, l, (l + r) / 2);
            let vr = self.sub_query_internal(a, b, k * 2 + 2, (l + r) / 2, r);
            (self.monoid_op_closure)(vl, vr)
        }
    }

    fn query_internal(&mut self, a: usize, b: usize) -> A {
        let n = (self.lazy.len() + 1) / 2;
        self.sub_query_internal(a, b, 0, 0, n)
    }
}

trait LazyRangeQuery<T> {
    type Output;
    fn query(&mut self, r: T) -> Self::Output;
    fn update(&mut self, r: T, x: Self::Output);
}

#[allow(dead_code)]
impl<A, CUnit, CMult> LazyRangeQuery<std::ops::Range<usize>> for LazySegmentTree<A, CUnit, CMult>
where
    A: Copy + std::cmp::Eq,
    CUnit: Fn() -> A,
    CMult: Fn(A, A) -> A,
{
    type Output = A;
    fn query(&mut self, range: std::ops::Range<usize>) -> A {
        return self.query_internal(range.start, range.end);
    }

    fn update(&mut self, range: std::ops::Range<usize>, x: A) {
        self.update_internal(range.start, range.end, x);
    }
}
