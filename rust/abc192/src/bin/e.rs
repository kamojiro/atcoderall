#![allow(non_snake_case)]
use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[fastout]
fn main() {
    input!{
        N: usize,
        M: usize,
        X: usize,
        Y: usize,
        ABTM: [(usize, usize, usize, usize); M]
    }

    let mut adj_list: Vec<Vec<Edge>> = vec![vec![];N];
    // println!("{:?}", ABTM);
    for i in 0..M{
        adj_list[ABTM[i].0-1].push(Edge{time: ABTM[i].3, cost: ABTM[i].2, position: ABTM[i].1-1});
        adj_list[ABTM[i].1-1].push(Edge{time: ABTM[i].3, cost: ABTM[i].2, position: ABTM[i].0-1});
    }
    let mut dist: Vec<usize> = (0..N).map(|_| std::usize::MAX).collect();
    
    let mut heap = BinaryHeap::new();

    let start = X-1;
    let goal = Y-1;
                            
    // We're at `start`, with a zero cost
    dist[X-1] = 0;
    heap.push(State { cost: 0, position: start });
    while let Some(State { cost, position }) = heap.pop() {
        // println!("{} {}", cost, position);
        // println!("{:?}", dist);
        if position == goal{
            println!("{}", cost);
            return
        } 
        // Important as we may have already found a better way
        if cost > dist[position] { continue; }

        // For each node we can reach, see if we can find a way with
        // a lower cost going through this node
        // println!("position {}",position );
        for edge in &adj_list[position] {
            // println!("{}", edge.position);
            let next = State { cost: cost + ((cost + edge.time-1)/edge.time*edge.time - cost) + edge.cost, position: edge.position };

            // If so, add it to the frontier and continue
            if next.cost < dist[next.position] {
                heap.push(next);
                // Relaxation, we have now found a better way
                dist[next.position] = next.cost;
            }
        }
    }
    println!("-1");
}

#[derive(Copy, Clone)]
struct Edge {
    time: usize,
    cost: usize,
    position: usize,
}


#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    cost: usize,
    position: usize,
}

// The priority queue depends on `Ord`.
// Explicitly implement the trait so the queue becomes a min-heap
// instead of a max-heap.
impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        // Notice that the we flip the ordering on costs.
        // In case of a tie we compare positions - this step is necessary
        // to make implementations of `PartialEq` and `Ord` consistent.
        other.cost.cmp(&self.cost)
            .then_with(|| self.position.cmp(&other.position))
    }
}

// `PartialOrd` needs to be implemented as well.
impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

// -*- coding:utf-8-unix -*-

use proconio::{fastout, input};

use num_traits::{pow, One};
use std::ops::{Add, Div, Mul, Sub};

const MODULUS: usize = 1000000007;

#[derive(Clone, Copy, PartialEq, Debug)]
struct ModP(usize);

impl One for ModP {
    fn one() -> Self {
        return ModP(1);
    }
}
impl Add for ModP {
    type Output = Self;
    fn add(self, rhs: Self) -> Self {
        return ModP((self.0 + rhs.0) % MODULUS);
    }
}
impl Sub for ModP {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self {
        return ModP((self.0 + MODULUS - rhs.0) % MODULUS);
    }
}
impl Mul for ModP {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self {
        return ModP((self.0 * rhs.0) % MODULUS);
    }
}
impl Div for ModP {
    type Output = Self;
    fn div(self, rhs: Self) -> Self {
        if rhs.0 == 0 {
            panic!("Tried to divide by ModP(0)!");
        }
        let rhs_inv = pow(rhs, MODULUS - 2);
        return self * rhs_inv;
    }
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
#[allow(dead_code)]
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

// Number-theoretic transformation
// The length of f must be a power of 2
// and zeta must be a primitive f.len()th root of unity
// start and skip should be 0 and 1 respectively for the root invocation
// The inverse can be calculated by doing the same
// with the original zeta's inverse as zeta
// and dividing by f.len()
#[allow(dead_code)]
fn number_theoretic_transformation(
    f: &Vec<ModP>,
    start: usize,
    skip: usize,
    zeta: ModP,
) -> Vec<ModP> {
    let n = f.len() / skip;
    if n == 1 {
        return vec![f[start]];
    }
    let g0 = number_theoretic_transformation(f, start, skip * 2, zeta * zeta);
    let g1 = number_theoretic_transformation(f, start + skip, skip * 2, zeta * zeta);
    let mut pow_zeta = ModP(1);
    let mut g = Vec::new();
    for i in 0..n {
        g.push(g0[i % (n / 2)] + pow_zeta * g1[i % (n / 2)]);
        pow_zeta = pow_zeta * zeta;
    }
    return g;
}

// BIT from https://github.com/rust-lang-ja/atcoder-rust-base/blob/ja-all-enabled/examples/abc157-e-proconio.rs
// It requires commutativity so that "plus" operation works
use alga::general::{AbstractGroupAbelian, Operator};
use std::marker::PhantomData;
use std::ops::{Range, RangeInclusive, RangeTo, RangeToInclusive};

struct FenwickTree<A, O> {
    partial_sums: Vec<A>,
    phantom_operator: PhantomData<O>,
}

#[allow(dead_code)]
impl<A: AbstractGroupAbelian<O>, O: Operator> FenwickTree<A, O> {
    fn new(n: usize) -> Self {
        Self {
            partial_sums: vec![A::identity(); n],
            phantom_operator: PhantomData,
        }
    }

    fn operate_to_index(&mut self, i: usize, x: &A) {
        let mut i1 = i + 1;
        while i1 <= self.partial_sums.len() {
            self.partial_sums[i1 - 1] = self.partial_sums[i1 - 1].operate(x);
            // add "the last nonzero bit" to i1
            i1 += 1 << i1.trailing_zeros();
        }
    }
}

trait RangeQuery<T> {
    type Output;
    fn query(&self, r: T) -> Self::Output;
}

impl<A: AbstractGroupAbelian<O>, O: Operator> RangeQuery<RangeToInclusive<usize>>
    for FenwickTree<A, O>
{
    type Output = A;
    fn query(&self, range: RangeToInclusive<usize>) -> A {
        let mut sum = A::identity();
        let mut i1 = range.end + 1;
        while i1 > 0 {
            sum = sum.operate(&self.partial_sums[i1 - 1]);
            i1 -= 1 << i1.trailing_zeros();
        }
        return sum;
    }
}

impl<A: AbstractGroupAbelian<O>, O: Operator> RangeQuery<RangeTo<usize>> for FenwickTree<A, O> {
    type Output = A;
    fn query(&self, range: RangeTo<usize>) -> A {
        if range.end == 0 {
            return A::identity();
        } else {
            return self.query(..=range.end - 1);
        }
    }
}

impl<A: AbstractGroupAbelian<O>, O: Operator> RangeQuery<RangeInclusive<usize>>
    for FenwickTree<A, O>
{
    type Output = A;
    fn query(&self, range: RangeInclusive<usize>) -> A {
        return self
            .query(..=*range.end())
            .operate(&self.query(..*range.start()).two_sided_inverse());
    }
}

impl<A: AbstractGroupAbelian<O>, O: Operator> RangeQuery<Range<usize>> for FenwickTree<A, O> {
    type Output = A;
    fn query(&self, range: Range<usize>) -> A {
        return self.query(range.start..=range.end - 1);
    }
}

use std::cell::Cell;

#[derive(Debug, Clone)]
struct EquivalenceRelation {
    parent: Vec<Cell<usize>>,
    rank: Vec<Cell<usize>>,
}

#[allow(dead_code)]
impl EquivalenceRelation {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(Cell::new(i));
        }
        let rank = vec![Cell::new(0); n];
        return Self { parent, rank };
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
        let aarank = self.rank[aa].get();
        let bbrank = self.rank[bb].get();
        if aarank > bbrank {
            self.parent[bb].set(aa);
        // self.rank[aa] = aarank.max(bbrank + 1);
        } else {
            self.parent[aa].set(bb);
            self.rank[bb].set(bbrank.max(aarank + 1));
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
