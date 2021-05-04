for i in {0000..0050}
do
    cargo run --bin a < ../tools/in/$i.txt 2>> a.txt 1>/dev/null
done
         
