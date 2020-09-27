import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder__bit_code = """
def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


def _bsf(n: int) -> int:
    x = 0
    while n % 2 == 0:
        x += 1
        n //= 2

    return x
"""

atcoder._bit = types.ModuleType('atcoder._bit')
exec(_atcoder__bit_code, atcoder._bit.__dict__)


_atcoder__math_code = """
import typing


def _is_prime(n: int) -> bool:
    '''
    Reference:
    M. Forisek and J. Jancina,
    Fast Primality Testing for Integers That Fit into a Machine Word
    '''

    if n <= 1:
        return False
    if n == 2 or n == 7 or n == 61:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for a in (2, 7, 61):
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0:
            return False
    return True


def _inv_gcd(a: int, b: int) -> typing.Tuple[int, int]:
    a %= b
    if a == 0:
        return (b, 0)

    # Contracts:
    # [1] s - m0 * a = 0 (mod b)
    # [2] t - m1 * a = 0 (mod b)
    # [3] s * |m1| + t * |m0| <= b
    s = b
    t = a
    m0 = 0
    m1 = 1

    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u  # |m1 * u| <= |m1| * s <= b

        # [3]:
        # (s - t * u) * |m1| + t * |m0 - m1 * u|
        # <= s * |m1| - t * u * |m1| + t * (|m0| + |m1| * u)
        # = s * |m1| + t * |m0| <= b

        s, t = t, s
        m0, m1 = m1, m0

    # by [3]: |m0| <= b/g
    # by g != b: |m0| < b/g
    if m0 < 0:
        m0 += b // s

    return (s, m0)


def _primitive_root(m: int) -> int:
    if m == 2:
        return 1
    if m == 167772161:
        return 3
    if m == 469762049:
        return 3
    if m == 754974721:
        return 11
    if m == 998244353:
        return 3

    divs = [2] + [0] * 19
    cnt = 1
    x = (m - 1) // 2
    while x % 2 == 0:
        x //= 2

    i = 3
    while i * i <= x:
        if x % i == 0:
            divs[cnt] = i
            cnt += 1
            while x % i == 0:
                x //= i
        i += 2

    if x > 1:
        divs[cnt] = x
        cnt += 1

    g = 2
    while True:
        for i in range(cnt):
            if pow(g, (m - 1) // divs[i], m) == 1:
                break
        else:
            return g
        g += 1
"""

atcoder._math = types.ModuleType('atcoder._math')
exec(_atcoder__math_code, atcoder._math.__dict__)



_atcoder_modint_code = """
from __future__ import annotations
import typing

# import atcoder._math


class ModContext:
    context = []

    def __init__(self, mod: int) -> None:
        assert 1 <= mod

        self.mod = mod

    def __enter__(self) -> None:
        self.context.append(self.mod)

    def __exit__(self, exc_type: typing.Any, exc_value: typing.Any,
                 traceback: typing.Any) -> None:
        self.context.pop()

    @classmethod
    def get_mod(cls) -> int:
        return cls.context[-1]


class Modint:
    def __init__(self, v: int = 0) -> None:
        self._mod = ModContext.get_mod()
        if v == 0:
            self._v = 0
        else:
            self._v = v % self._mod

    def mod(self) -> int:
        return self._mod

    def val(self) -> int:
        return self._v

    def __iadd__(self, rhs: typing.Union[Modint, int]) -> Modint:
        if isinstance(rhs, Modint):
            self._v += rhs._v
        else:
            self._v += rhs
        if self._v >= self._mod:
            self._v -= self._mod
        return self

    def __isub__(self, rhs: typing.Union[Modint, int]) -> Modint:
        if isinstance(rhs, Modint):
            self._v -= rhs._v
        else:
            self._v -= rhs
        if self._v < 0:
            self._v += self._mod
        return self

    def __imul__(self, rhs: typing.Union[Modint, int]) -> Modint:
        if isinstance(rhs, Modint):
            self._v = self._v * rhs._v % self._mod
        else:
            self._v = self._v * rhs % self._mod
        return self

    def __ifloordiv__(self, rhs: typing.Union[Modint, int]) -> Modint:
        if isinstance(rhs, Modint):
            inv = rhs.inv()._v
        else:
            inv = atcoder._math._inv_gcd(rhs, self._mod)[1]
        self._v = self._v * inv % self._mod
        return self

    def __pos__(self) -> Modint:
        return self

    def __neg__(self) -> Modint:
        return Modint() - self

    def __pow__(self, n: int) -> Modint:
        assert 0 <= n

        return Modint(pow(self._v, n, self._mod))

    def inv(self) -> Modint:
        eg = atcoder._math._inv_gcd(self._v, self._mod)

        assert eg[0] == 1

        return Modint(eg[1])

    def __add__(self, rhs: typing.Union[Modint, int]) -> Modint:
        if isinstance(rhs, Modint):
            result = self._v + rhs._v
            if result >= self._mod:
                result -= self._mod
            return raw(result)
        else:
            return Modint(self._v + rhs)

    def __sub__(self, rhs: typing.Union[Modint, int]) -> Modint:
        if isinstance(rhs, Modint):
            result = self._v - rhs._v
            if result < 0:
                result += self._mod
            return raw(result)
        else:
            return Modint(self._v - rhs)

    def __mul__(self, rhs: typing.Union[Modint, int]) -> Modint:
        if isinstance(rhs, Modint):
            return Modint(self._v * rhs._v)
        else:
            return Modint(self._v * rhs)

    def __floordiv__(self, rhs: typing.Union[Modint, int]) -> Modint:
        if isinstance(rhs, Modint):
            inv = rhs.inv()._v
        else:
            inv = atcoder._math._inv_gcd(rhs, self._mod)[1]
        return Modint(self._v * inv)

    def __eq__(self, rhs: typing.Union[Modint, int]) -> bool:
        if isinstance(rhs, Modint):
            return self._v == rhs._v
        else:
            return self._v == rhs

    def __ne__(self, rhs: typing.Union[Modint, int]) -> bool:
        if isinstance(rhs, Modint):
            return self._v != rhs._v
        else:
            return self._v != rhs


def raw(v: int) -> Modint:
    x = Modint()
    x._v = v
    return x
"""

atcoder.modint = types.ModuleType('atcoder.modint')
atcoder.modint.__dict__['atcoder'] = atcoder
atcoder.modint.__dict__['atcoder._math'] = atcoder._math
exec(_atcoder_modint_code, atcoder.modint.__dict__)
ModContext = atcoder.modint.ModContext

Modint = atcoder.modint.Modint


_atcoder_convolution_code = """
import typing

# import atcoder._bit
# import atcoder._math
# from atcoder.modint import ModContext, Modint


_sum_e = {}  # _sum_e[i] = ies[0] * ... * ies[i - 1] * es[i]


def _butterfly(a: typing.List[Modint]) -> None:
    g = atcoder._math._primitive_root(a[0].mod())
    n = len(a)
    h = atcoder._bit._ceil_pow2(n)

    if a[0].mod() not in _sum_e:
        es = [Modint(0)] * 30  # es[i]^(2^(2+i)) == 1
        ies = [Modint(0)] * 30
        cnt2 = atcoder._bit._bsf(a[0].mod() - 1)
        e = Modint(g) ** ((a[0].mod() - 1) >> cnt2)
        ie = e.inv()
        for i in range(cnt2, 1, -1):
            # e^(2^i) == 1
            es[i - 2] = e
            ies[i - 2] = ie
            e = e * e
            ie = ie * ie
        sum_e = [Modint(0)] * 30
        now = Modint(1)
        for i in range(cnt2 - 2):
            sum_e[i] = es[i] * now
            now *= ies[i]
        _sum_e[a[0].mod()] = sum_e
    else:
        sum_e = _sum_e[a[0].mod()]

    for ph in range(1, h + 1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        now = Modint(1)
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                left = a[i + offset]
                right = a[i + offset + p] * now
                a[i + offset] = left + right
                a[i + offset + p] = left - right
            now *= sum_e[atcoder._bit._bsf(~s)]


_sum_ie = {}  # _sum_ie[i] = es[0] * ... * es[i - 1] * ies[i]


def _butterfly_inv(a: typing.List[Modint]) -> None:
    g = atcoder._math._primitive_root(a[0].mod())
    n = len(a)
    h = atcoder._bit._ceil_pow2(n)

    if a[0].mod() not in _sum_ie:
        es = [0] * 30  # es[i]^(2^(2+i)) == 1
        ies = [0] * 30
        cnt2 = atcoder._bit._bsf(a[0].mod() - 1)
        e = Modint(g) ** ((a[0].mod() - 1) >> cnt2)
        ie = e.inv()
        for i in range(cnt2, 1, -1):
            # e^(2^i) == 1
            es[i - 2] = e
            ies[i - 2] = ie
            e = e * e
            ie = ie * ie
        sum_ie = [0] * 30
        now = Modint(1)
        for i in range(cnt2 - 2):
            sum_ie[i] = ies[i] * now
            now *= es[i]
        _sum_ie[a[0].mod()] = sum_ie
    else:
        sum_ie = _sum_ie[a[0].mod()]

    for ph in range(h, 0, -1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        inow = Modint(1)
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                left = a[i + offset]
                right = a[i + offset + p]
                a[i + offset] = left + right
                a[i + offset + p] = Modint(
                    (a[0].mod() + left.val() - right.val()) * inow.val())
            inow *= sum_ie[atcoder._bit._bsf(~s)]


def convolution_mod(a: typing.List[Modint],
                    b: typing.List[Modint]) -> typing.List[Modint]:
    n = len(a)
    m = len(b)

    if n == 0 or m == 0:
        return []

    if min(n, m) <= 60:
        if n < m:
            n, m = m, n
            a, b = b, a
        ans = [Modint(0) for _ in range(n + m - 1)]
        for i in range(n):
            for j in range(m):
                ans[i + j] += a[i] * b[j]
        return ans

    z = 1 << atcoder._bit._ceil_pow2(n + m - 1)

    while len(a) < z:
        a.append(Modint(0))
    _butterfly(a)

    while len(b) < z:
        b.append(Modint(0))
    _butterfly(b)

    for i in range(z):
        a[i] *= b[i]
    _butterfly_inv(a)
    a = a[:n + m - 1]

    iz = Modint(z).inv()
    for i in range(n + m - 1):
        a[i] *= iz

    return a


def convolution(mod: int, a: typing.List[typing.Any],
                b: typing.List[typing.Any]) -> typing.List[typing.Any]:
    n = len(a)
    m = len(b)

    if n == 0 or m == 0:
        return []

    with ModContext(mod):
        a2 = list(map(Modint, a))
        b2 = list(map(Modint, b))

        return list(map(lambda c: c.val(), convolution_mod(a2, b2)))


def convolution_int(
        a: typing.List[int], b: typing.List[int]) -> typing.List[int]:
    n = len(a)
    m = len(b)

    if n == 0 or m == 0:
        return []

    mod1 = 754974721  # 2^24
    mod2 = 167772161  # 2^25
    mod3 = 469762049  # 2^26
    m2m3 = mod2 * mod3
    m1m3 = mod1 * mod3
    m1m2 = mod1 * mod2
    m1m2m3 = mod1 * mod2 * mod3

    i1 = atcoder._math._inv_gcd(mod2 * mod3, mod1)[1]
    i2 = atcoder._math._inv_gcd(mod1 * mod3, mod2)[1]
    i3 = atcoder._math._inv_gcd(mod1 * mod2, mod3)[1]

    c1 = convolution(mod1, a, b)
    c2 = convolution(mod2, a, b)
    c3 = convolution(mod3, a, b)

    c = [0] * (n + m - 1)
    for i in range(n + m - 1):
        c[i] += (c1[i] * i1) % mod1 * m2m3
        c[i] += (c2[i] * i2) % mod2 * m1m3
        c[i] += (c3[i] * i3) % mod3 * m1m2
        c[i] %= m1m2m3

    return c
"""

atcoder.convolution = types.ModuleType('atcoder.convolution')
atcoder.convolution.__dict__['atcoder'] = atcoder
atcoder.convolution.__dict__['atcoder._bit'] = atcoder._bit
atcoder.convolution.__dict__['atcoder._math'] = atcoder._math
atcoder.convolution.__dict__['ModContext'] = atcoder.modint.ModContext
atcoder.convolution.__dict__['Modint'] = atcoder.modint.Modint
exec(_atcoder_convolution_code, atcoder.convolution.__dict__)
convolution = atcoder.convolution.convolution

#import sys
#input = sys.stdin.readline
# from atcoder.convolution import convolution

def main():
    Q = 998244353
    N, M = map( int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(" ".join(map(str,convolution(Q,A,B))))
if __name__ == '__main__':
    main()
