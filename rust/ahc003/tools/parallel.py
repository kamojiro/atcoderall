import subprocess
from subprocess import PIPE

from concurrent import futures

A = []

def test(index):
    cmd = "cargo run --release --bin tester in/" +"{:0>4d}".format(index)+ ".txt cargo run --bin a"
    proc = subprocess.run(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    output = proc.stderr
    ret = output.split()
    A.append((ret[-1].decode(), index))

    # proc = subprocess.run("cargo run --release --bin tester in/0000.txt cargo run --bin a", stdout=PIPE, stderr=PIPE, shell=True)


future_list = []
N = 100
with futures.ThreadPoolExecutor(max_workers=16) as executor:
    for i in range(N):
        future = executor.submit(fn=test, index=i)
        future_list.append(future)
    _ = futures.as_completed(fs=future_list)



m = min(map(int, map(lambda x:x[0], A)))
M = max(map(int, map(lambda x:x[0], A)))
mindex = 0
Mindex = 0
for i, a in enumerate(A):
    if int(a[0]) == m:
        mindex = a[1]
    if int(a[0]) == M:
        Mindex = a[1]
print("min:", m,"argmin:", mindex)
print("max:", M,"argmax:", Mindex)
print(sum(map(int, map(lambda x:x[0], A))))
