import subprocess
from subprocess import PIPE

proc = subprocess.run("cargo run --release --bin tester in/0000.txt cargo run --bin a", stdout=PIPE, stderr=PIPE, shell=True)
# proc = subprocess.run("pwd", stdout=PIPE, stderr=PIPE, shell=True)
# pwd = proc.stdout
# proc = subprocess.run("less " + pwd.strip() + "/in/0000.txt", stdout=PIPE, stderr=PIPE, text=True)
output = proc.stderr
ret = output.split()
print(ret[-1].decode())
