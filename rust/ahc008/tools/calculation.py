#import sys
#input = sys.stdin.readline
import subprocess
def main():
    proc = subprocess.run("cargo run --release --bin tester ../../target/release/a < in/0000.txt > out.txt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(proc.stderr)
    print(int(proc.stderr.split()[-1]))
if __name__ == '__main__':
    main()
