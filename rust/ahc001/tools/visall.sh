echo points > points.txt
s=0
for i in {0000..0009}
do
    t=`cargo run --release --bin vis in/$i.txt out/$i.txt`
    s=`expr $s + $t`
    mv out.svg svgs/$i.svg
done
echo $s
