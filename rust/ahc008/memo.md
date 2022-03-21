# AtCoder Heuristic Contest 003

## commands

cargo run --release --bin tester ../../target/release/a < in/0000.txt > out.txt
file:///home/ochir/atcoder/rust/ahc008/tools/out.txt
cargo run --release --bin tester ../../target/release/a < in/0002.txt > out.txt
for i in {0000..1000}; do echo $i; cargo run --release --bin tester ../../target/release/a < in/$i.txt > out/$i.txt; done


```
for i in range(1, 11):
    print(", ".join(map(lambda x:str(x), [(i,4),(i,8),(i,12),(i,15),(i,19),(i,23),(i,27),""])))

```

## Idea

- はじめに全部仕切りで埋める
  - そのあと、人間だけの部分を増やすように広げていく
- 基本的に、人間だけの領域を増やすのが大事な気がする。
- いい感じの位置にペットがくるまで待つ
- 犬を最初に処理する
- 一旦単純な分割にした
- 序盤は3匹以上で閉じ込めるとかのほうがいい気がする

## diary

### 20220220

部屋割を細かくした。
さすがにそろそろ自動的に集計するプログラムが必要な気がする。
部屋の分割のために人を動かすのに結構時間がかかる。
盤面を埋めれば埋めるほど時間がかかる気がする。
10000ケースやったときにWAが出ても全然おかしくない状況。


### 20220218

犬を最後に処理するようにした。
与えられた座標に従って仕切りを設置する関数を追加した。
最後に犬を処理するだけで得点が10倍になった。
最終形を見る限りほとんどのペットのいる領域が人間ゾーンと仕切られている。
いいかんじに鳩の巣原理っぽくやって残る領域を増やせばうまく行きそう。

### 20220216

犬の処理は諦めて。
一旦単純な分割にした

### 20220215

ここまでのまとめ。
犬を処理した。
