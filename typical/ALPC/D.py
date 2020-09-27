import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder_maxflow_code = """
from __future__ import annotations

from typing import NamedTuple, Optional, List


class MFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int

    class _Edge:
        def __init__(self, dst: int, cap: int) -> None:
            self.dst = dst
            self.cap = cap
            self.rev: Optional[MFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MFGraph._Edge(dst, cap)
        re = MFGraph._Edge(src, 0)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = e.rev
        return MFGraph.Edge(
            re.dst,
            e.dst,
            e.cap + re.cap,
            re.cap
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def change_edge(self, i: int, new_cap: int, new_flow: int) -> None:
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = sum(e.cap for e in self._g[s])

        current_edge = [0] * self._n
        level = [0] * self._n

        def fill(arr: List[int], value: int) -> None:
            for i in range(len(arr)):
                arr[i] = value

        def bfs() -> bool:
            fill(level, self._n)
            queue = []
            q_front = 0
            queue.append(s)
            level[s] = 0
            while q_front < len(queue):
                v = queue[q_front]
                q_front += 1
                next_level = level[v] + 1
                for e in self._g[v]:
                    if e.cap == 0 or level[e.dst] <= next_level:
                        continue
                    level[e.dst] = next_level
                    if e.dst == t:
                        return True
                    queue.append(e.dst)
            return False

        def dfs(lim: int) -> int:
            stack = []
            edge_stack = []
            stack.append(t)
            while stack:
                v = stack[-1]
                if v == s:
                    flow = min(lim, min(e.cap for e in edge_stack))
                    for e in edge_stack:
                        e.cap -= flow
                        e.rev.cap += flow
                    return flow
                next_level = level[v] - 1
                while current_edge[v] < len(self._g[v]):
                    e = self._g[v][current_edge[v]]
                    re = e.rev
                    if level[e.dst] != next_level or re.cap == 0:
                        current_edge[v] += 1
                        continue
                    stack.append(e.dst)
                    edge_stack.append(re)
                    break
                else:
                    stack.pop()
                    if edge_stack:
                        edge_stack.pop()
                    level[v] = self._n
            return 0

        flow = 0
        while flow < flow_limit:
            if not bfs():
                break
            fill(current_edge, 0)
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                flow += f
                if f == 0:
                    break
        return flow

    def min_cut(self, s: int) -> List[bool]:
        visited = [False] * self._n
        stack = [s]
        visited[s] = True
        while stack:
            v = stack.pop()
            for e in self._g[v]:
                if e.cap > 0 and not visited[e.dst]:
                    visited[e.dst] = True
                    stack.append(e.dst)
        return visited
"""

atcoder.maxflow = types.ModuleType('atcoder.maxflow')
exec(_atcoder_maxflow_code, atcoder.maxflow.__dict__)
MFGraph = atcoder.maxflow.MFGraph

#import sys
#input = sys.stdin.readline
# from atcoder.maxflow import MFGraph

def main():
    N, M = map( int, input().split())
    S = [ list( input()) for _ in range(N)]
    graph = MFGraph(N*M+2);
    s = N*M
    g = N*M+1
    for i in range(N):
        for j in range(M):
            if S[i][j] == "#":
                continue
            if (i+j)%2 == 0:
                graph.add_edge(s,i*M+j,1)
            else:
                graph.add_edge(i*M+j,g,1)
                continue
            if i > 0:
                if S[i-1][j] == ".":
                    graph.add_edge(i*M+j,(i-1)*M+j,1)
            if i < N-1:
                if S[i+1][j] == ".":
                    graph.add_edge(i*M+j,(i+1)*M+j,1)
            if j > 0:
                if S[i][j-1] == ".":
                    graph.add_edge(i*M+j,i*M+j-1,1)
            if j < M-1:
                if S[i][j+1] == ".":
                    graph.add_edge(i*M+j,i*M+j+1,1)

    ans = graph.flow(s,g)
    print(ans)

    for e in graph.edges():
        if e.src == s or e.dst == g or e.flow == 0:
            continue
        i0, j0 = e.src//M, e.src%M
        i1, j1 = e.dst//M, e.dst%M
        # print(i0,j0, i1,j1,e.flow)
        if i0 == i1:
            if j0 > j1:
                j0, j1 = j1, j0
            S[i0][j0] = '>'
            S[i1][j1] = '<'
        else:
            if i0 > i1:
                i0, i1 = i1, i0
            S[i0][j0] = 'v'
            S[i1][j1] = '^'
    print("\n".join([ "".join(S[i]) for i in range(N)]))


if __name__ == '__main__':
    main()
