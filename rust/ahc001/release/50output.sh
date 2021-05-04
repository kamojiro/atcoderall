for i in {0000..0009}
do
    cargo run --bin a < ../tools/in/$i.txt 2>/dev/null 1> ../tools/out/$i.txt
done
         
