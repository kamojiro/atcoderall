python tester/generator.py $1 >input.txt
cd A
cargo run < ../input.txt > output.txt
cd ../
python tester/tester.py input.txt output.txt
