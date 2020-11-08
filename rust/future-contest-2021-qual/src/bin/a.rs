#![allow(non_snake_case)]
use proconio::{input, fastout};
use std::cmp;
use std::collections::{VecDeque,HashMap};

pub fn main() {
    let _ = ::std::thread::Builder::new()
        .name("run".to_string())
        .stack_size(32 * 1024 * 1024)
        .spawn(run)
        .unwrap()
        .join();
}


#[derive(Clone, Debug)]
pub struct Input {
    pub N: usize,
    pub M: usize,
    pub cards: Vec<(usize,usize)>,
    pub U: usize,
    pub D: usize,
    pub L: usize,
    pub R: usize,
    pub I: usize,
    pub O: usize,
}

// read_input
fn read_input() -> Input {
    let N: usize = 100;
    input! {
        cards: [(usize,usize);N],
    }
    let M:usize = 20;
    let U:usize = 100;
    let D:usize = 200;
    let L:usize = 300;
    let R:usize = 400;
    let I:usize = 1000;
    let O:usize = 2000;
    Input {
        N,
        M,
        cards,
        U,
        D,
        L,
        R,
        I,
        O,
    }
}

//compute_score
fn compute_score(output: &Vec<usize>) -> usize{
    let mut ret: usize = 0;
    for z in output{
        if z == &2000{
            // ret += 1;
        }else if z == &1000{
            // ret += 1;
        }else if z >= &400{
            ret += z-400;
        }else if z >= &300{
            ret += z-300;
        }else if z >= &200{
            ret += z-200;
        }else if z >= &100{
            ret += z-100;
        }
    }
    4000-ret
}

fn stupid_solve(input: &Input) -> Vec<usize>{
    let mut ret:Vec<usize> = Vec::new();
    let mut x:usize = 0;
    let mut y:usize = 0;
    for (ax,ay) in &input.cards{
        // //x vs ax
        // if x < *ax{
        //     ret.push(input.D+(ax-x));
        // }else if x > *ax{
        //     ret.push(input.U+(x-ax));            
        // }
        // if y < *ay{
        //     ret.push(input.R+(ay-y));
        // }else if y > *ay{
        //     ret.push(input.L+(y-ay));
        // }
        // x = *ax;
        // y = *ay;
        // ret.push(input.I);
        compare_and_input(&input,&mut ret,&(x,y), &(*ax,*ay));
        x = *ax;
        y = *ay;
        ret.push(input.I);
    }
    ret
}

fn almost_stupid_solve(input: &Input, start: (usize,usize)) -> Vec<usize>{
    let mut ret:Vec<usize> = Vec::new();
    let mut board: Vec<Vec<usize>> =  vec![vec![1000;input.M];input.M];
    let mut card_place = HashMap::new();
    let mut i:usize = 0;
    for &(x,y) in &input.cards{
        board[x][y] = i;
        card_place.insert(i,(x,y));
        i += 1;

    }
    
    let mut x:usize = start.0;
    let mut y:usize = start.1;
    // for &(ax,ay) in &input.cards{
    for i in 0..100{
        let &(ax,ay) = card_place.get(&i).unwrap();
        let mut num:usize=0;
        let mut other_num:usize=0;
        let mut tx = x;
        let mut ty = y;
        while tx != ax{
            if board[tx][ty] < 1000{
                num += 1;
            }else{
                other_num += 1;
            }
            if tx < ax{
                tx += 1;
            }else if tx > ax{
                tx -= 1;
            }
                
        }
        while ty != ay{
            if board[tx][ty] < 1000{
                num += 1;
            }else{
                other_num += 1;
            }
            if ty < ay{
                ty += 1;
            }else if ty > ay{
                ty -= 1;
            }
        }
        let mut tx = x;
        let mut ty = y;
        let mut count:usize = 0;
        let mut stack:Vec<usize> = Vec::new();
        while tx != ax{
            if board[tx][ty] < 1000{
                if count < other_num{
                    stack.push(board[tx][ty]);
                    count += 1;
                    board[tx][ty] = 1000;
                    ret.push(input.I);
                }
            }else{
                if (count >= other_num) && (count > 0){
                    board[tx][ty] = stack.pop().unwrap();
                    card_place.insert(board[tx][ty],(tx,ty));
                    ret.push(input.O);
                    count -= 1;
                }
                other_num -= 1;
            }
            if tx < ax{
                tx += 1;
                ret.push(input.D+1);
            }else if tx > ax{
                tx -= 1;
                ret.push(input.U+1);
            }
                
        }
        while ty != ay{
            if board[tx][ty] < 1000{
                if count < other_num{
                    stack.push(board[tx][ty]);
                    count += 1;
                    board[tx][ty] = 1000;
                    ret.push(input.I);
                }
            }else{
                if (count >= other_num) && (count > 0){
                    board[tx][ty] = stack.pop().unwrap();
                    card_place.insert(board[tx][ty],(tx,ty));
                    count -= 1;
                    ret.push(input.O);
                }
                other_num -= 1;
            }
            if ty < ay{
                ty += 1;
                ret.push(input.R+1);
            }else if ty > ay{
                ty -= 1;
                ret.push(input.L+1);
            }
        }
        // eprintln!("stakc");
        // eprintln!("{} {:?}",count, stack);
        board[ax][ay] = 1000;
        ret.push(input.I);
        x = ax;
        y = ay;

    }
    ret
}


fn compare_and_input(input: &Input, output: &mut Vec<usize>,p:&(usize,usize),q:&(usize,usize)){
    if p.0 < q.0{
        output.push(input.D+(q.0-p.0));
    }else if p.0 > q.0{
        output.push(input.U+(p.0-q.0));            
    }
    if p.1 < q.1{
        output.push(input.R+(q.1-p.1));
    }else if p.1 > q.1{
        output.push(input.L+(p.1-q.1));
    }
}

fn diff_abs(x:usize, y:usize) -> usize{
    if x > y{
        x-y
    }else{
        y-x
    }
}

fn dist(p:&(usize,usize),q:&(usize,usize)) -> usize{
    diff_abs(p.0,q.0) + diff_abs(p.1,q.1)
}

fn solve_with_one_card(input: &Input, start: (usize,usize)) -> Vec<usize>{
    // we will compare with (1) d(x_0,x_1)+d(x_1,x_2) and (2) d(x_0,x_2)+d(x_2,p)+d(p,x_1)+d(x_1,p)
    // (1) d(x_0,x_1)+d(x_1,x_2)
    // (2) d(x_0,x_2)+d(x_2,p)+d(p,x_1)*2
    // ,where p is temporary.
    let mut ret:Vec<usize> = Vec::new();
    let mut board: Vec<Vec<usize>> =  vec![vec![1000;input.M];input.M];
    let mut i:usize = 0;
    for &(x,y) in &input.cards{
        board[x][y] = i;
        i += 1;
    }
    // eprintln!("{:?}", board);
    let mut x:usize = start.0;
    let mut y:usize = start.1;
    let mut i:usize = 0;
    while i < input.N{
        if i == input.N-1{
            compare_and_input(&input, &mut ret, &(x,y), &input.cards[i]);
            ret.push(input.I);
            break
        }
        let (px,py) = input.cards[i];
        let (ppx,ppy) = input.cards[i+1];
        let d1 = dist(&(x,y), &(px,py)) + dist(&(px,py), &(ppx,ppy));
        // make square with 
        let lx = cmp::min(px,ppx);
        let rx = cmp::max(px,ppx);
        let ly = cmp::min(py,ppy);
        let ry = cmp::max(py,ppy);
        let mut p:(usize,usize) = (0,0);
        let mut dxp:usize = 1000;
        for fx in lx..rx{
            for fy in ly..ry{
                if board[fx][fy] < 1000{
                    continue
                }
                if dist(&(ppx,ppy),&(fx,fy)) + dist(&(px,py), &(fx,fy))*2 < dxp{
                    dxp = dist(&(ppx,ppy),&(fx,fy)) + dist(&(px,py), &(fx,fy))*2;
                    p.0 = fx;
                    p.1 = fy;
                }
            }
        }
        let d2 = dist(&(x,y),&(ppx,ppy)) + dxp;
        if d1 <= d2{
            // eprintln!("{} {}",i, "d1" );

            i += 1;
            board[px][py] = 1000;
            compare_and_input(&input, &mut ret, &(x,y), &(px,py));
            ret.push(input.I);
            x = px;
            y = py;
        }else{
            // eprintln!("{} {}",i, "d2" );
            i += 2;
            board[px][py] = 1000;
            board[ppx][ppy] = 1000;
            compare_and_input(&input, &mut ret, &(x,y), &(ppx,ppy));
            ret.push(input.I);
            compare_and_input(&input, &mut ret, &(ppx,ppy), &(p.0,p.1));
            ret.push(input.O);
            compare_and_input(&input, &mut ret, &(p.0,p.1), &(px,py));
            ret.push(input.I);
            compare_and_input(&input, &mut ret, &(px,py), &(p.0,p.1));
            ret.push(input.I);
            x = p.0;
            y = p.1;
        }
    }
    ret
}

fn preprocess(input: &Input) -> (Vec<usize>,Input){
    let N = input.N;
    let M = input.M;
    let U = input.U;
    let D = input.D;
    let L = input.L;
    let R = input.R;
    let I = input.I;
    let O = input.O;

    let mut board: Vec<Vec<usize>> =  vec![vec![1000;input.M];input.M];
    let mut i:usize = 0;
    for &(x,y) in &input.cards{
        board[x][y] = i;
        i += 1;
    }

    let mut output: Vec<usize> = Vec::new();
    let mut deque: VecDeque<usize> = VecDeque::new();
    for i in 0..input.M{
        if i%2 == 0{
            for j in 0..input.M{
                if board[i][j] < 1000{
                    output.push(input.I);
                    deque.push_front(board[i][j]);
                }
                if j == input.M-1{
                    output.push(input.D+1);
                }else{
                    output.push(input.R+1);
                }
            }
        }else{
            for j in (0..input.M).rev(){
                if board[i][j] < 1000{
                    output.push(input.I);
                    deque.push_front(board[i][j]);
                }
                if j == 0{
                    if i < (input.M-1){
                        output.push(input.D+1);                        
                    }
                }else{
                    output.push(input.L+1);
                }
            }
        }
    }
    let mut cards: Vec<(usize,usize)> = vec![(0,0);input.N];
    let mut t:usize = 0;
    for i in (10..input.M).rev(){
        if i%2 == 1{
            for j in 0..10{
                cards[deque[t]] = (i,j);
                if j == 9{
                    output.push(input.O);
                    output.push(input.U+1);
                }else{
                    output.push(input.O);
                    output.push(input.R+1);
                }
                t += 1;
            }
        }else{
            for j in (0..10).rev(){
                cards[deque[t]] = (i,j);
                if j == 0{
                    output.push(input.O);
                    if i != 10{
                        output.push(input.U+1);
                    }
                }else{
                    output.push(input.O);
                    output.push(input.L+1);
                }
                t += 1;
            }
        }

    }
    // eprintln!("{:?}", deque );
    // eprintln!("{:?}", cards);
    (output,
     Input {
        N,
        M,
        cards,
        U,
        D,
        L,
        R,
        I,
        O,
    })

}

fn inner_circle(p: &(usize,usize)) -> bool{
    if p.0 <= 2{
        return false
    }
    if p.0 >= 16{
        return false
    }
    if p.0 <= 9{
        if (12-p.0 <= p.1) && (p.1 <= 7+p.0){
            return true
        }
    }else{
        if (p.0 == 10) || (p.0 == 11){
            if (4 <= p.1) && (p.1 <= 15){
                return true
            }
        }else{
            if (p.0-6 <= p.1) && (p.1 <= 25-p.0){
                return true
            }
        }
    }
    false
}

fn preprocess3(input: &Input) -> (Vec<usize>,Input){
    let N = input.N;
    let M = input.M;
    let U = input.U;
    let D = input.D;
    let L = input.L;
    let R = input.R;
    let I = input.I;
    let O = input.O;

    let mut board: Vec<Vec<usize>> =  vec![vec![1000;input.M];input.M];
    let mut i:usize = 0;
    for &(x,y) in &input.cards{
        board[x][y] = i;
        i += 1;
    }

    let mut output: Vec<usize> = Vec::new();
    let mut cards: Vec<(usize,usize)> = vec![(0,0);input.N];
    let mut stack: Vec<usize> = Vec::new();
    
    for i in 0..10{
        for j in i..(19-i){
            let x = i;
            let y = j;

            if inner_circle(&(x,y)){
                if board[x][y] < 1000{
                    cards[board[x][y]] = (x,y);
                }else{
                    
                    cards[stack.pop().unwrap()] = (x,y);
                    output.push(input.O);
                }
            }else{
                if board[x][y] < 1000{
                    stack.push(board[x][y]);
                    output.push(input.I);
                }
            }
            output.push(input.R+1);
        }
        for j in i..(19-i){
            let x = j;
            let y = 19-i;

            if inner_circle(&(x,y)){
                if board[x][y] < 1000{
                    cards[board[x][y]] = (x,y);
                }else{
                    cards[ stack.pop().unwrap()] = (x,y);
                    output.push(input.O);
                }
            }else{
                if board[x][y] < 1000{
                    stack.push(board[x][y]);
                    output.push(input.I);
                }
            }
            output.push(input.D+1);
        }
        for j in ((i+1)..(20-i)).rev(){
            let x = 19-i;
            let y = j;

            if inner_circle(&(x,y)){
                if board[x][y] < 1000{
                    cards[board[x][y]] = (x,y);
                }else{
                    // eprintln!("{} {} {:?}",x,y, stack);
                    // if x == 13 && y == 10{
                    //     stdout_from_output(&output);
                    // }
                    cards[ stack.pop().unwrap()] = (x,y);
                    output.push(input.O);
                }
            }else{
                if board[x][y] < 1000{
                    stack.push(board[x][y]);
                    output.push(input.I);
                }
            }
            output.push(input.L+1);
        }
        for j in ((i+1)..(20-i)).rev(){
            let x = j;
            let y = i;

            if inner_circle(&(x,y)){
                if board[x][y] < 1000{
                    cards[board[x][y]] = (x,y);
                }else{
                    cards[ stack.pop().unwrap()] = (x,y);
                    output.push(input.O);
                }
            }else{
                if board[x][y] < 1000{
                    stack.push(board[x][y]);
                    output.push(input.I);
                }
            }
            if j == i+1{
                if i < 9{
                    output.push(input.R+1)
                }
            }else{
                output.push(input.U+1);
            }
        }
    }
    
    (output,
     Input {
        N,
        M,
        cards,
        U,
        D,
        L,
        R,
        I,
        O,
    })

}

fn preprocess2(input: &Input) -> (Vec<usize>,Input){
    let N = input.N;
    let M = input.M;
    let U = input.U;
    let D = input.D;
    let L = input.L;
    let R = input.R;
    let I = input.I;
    let O = input.O;

    let mut board: Vec<Vec<usize>> =  vec![vec![1000;input.M];input.M];
    let mut i:usize = 0;
    for &(x,y) in &input.cards{
        board[x][y] = i;
        i += 1;
    }

    let mut output: Vec<usize> = Vec::new();
    let mut deque: VecDeque<usize> = VecDeque::new();
    for i in 0..10{
        if i%2 == 0{
            for j in 0..input.M{
                if board[i][j] < 1000{
                    output.push(input.I);
                    deque.push_front(board[i][j]);
                }
                if j == input.M-1{
                    output.push(input.D+1);
                }else{
                    output.push(input.R+1);
                }
            }
        }else{
            for j in (0..input.M).rev(){
                if board[i][j] < 1000{
                    output.push(input.I);
                    deque.push_front(board[i][j]);
                }
                if j == 0{
                    output.push(input.D+1);                        
                }else{
                    output.push(input.L+1);
                }
            }
        }
    }
    // eprintln!("area zero");
    // eprintln!("{}", output.len());

    for j in 0..10{
        if j%2 == 0{
            for i in 10..20{
                if board[i][j] < 1000{
                    output.push(input.I);
                    deque.push_front(board[i][j]);
                }
                if i == 19{
                    output.push(input.R+1);
                }else{
                    output.push(input.D+1);
                }
            }
        }else{
            for i in (10..20).rev(){
                if board[i][j] < 1000{
                    output.push(input.I);
                    deque.push_front(board[i][j]);
                }
                if i == 10{
                    output.push(input.R+1);
                }else{
                    output.push(input.U+1);
                }
            }
        }
    }
    // eprintln!("{}", output.len());
    // eprintln!("{:?}", output[255]);
    // eprintln!("area one");

    let mut cards: Vec<(usize,usize)> = vec![(0,0);input.N];
    let mut t:usize = 0;
    // eprintln!("{}", deque.len());

    for i in 10..input.M{
        // eprintln!("{} {}",i,t );

        if i%2 == 0{
            for j in 10..20{
                if board[i][j] < 1000{
                    cards[board[i][j]] = (i,j);
                }else{
                    cards[deque[t]] = (i,j);
                    t += 1;
                    output.push(input.O);
                }

                if j == 19{
                    output.push(input.D+1);
                }else{
                    output.push(input.R+1);
                }
            }
        }else{
            for j in (10..20).rev(){
                if board[i][j] < 1000{
                    cards[board[i][j]] = (i,j);
                }else{
                    cards[deque[t]] = (i,j);
                    t += 1;
                    output.push(input.O);
                }

                if j == 10{
                    if i != 19{
                        output.push(input.D+1);
                    }
                }else{
                    output.push(input.L+1);
                }
            }
        }


    }
    // eprintln!("area two");

    // eprintln!("{:?}", deque );
    // eprintln!("{:?}", cards);
    (output,
     Input {
        N,
        M,
        cards,
        U,
        D,
        L,
        R,
        I,
        O,
    })

}

fn solve(input: &Input) -> Vec<usize>{
    // stupid_solve(&input)
    let mut outputs: Vec<Vec<usize>> = Vec::new();

    outputs.push(solve_with_one_card(&input,(0,0)));
    // let output1 = solve_with_one_card(&input,(0,0));
    // outputs.push(output1);
    let (output20, input2) = preprocess(&input);
    let mut output2 = output20;
    let mut outputa2:Vec<usize> = vec![0;output2.len()];
    outputa2.copy_from_slice(&output2[..]);
    let mut output21 = solve_with_one_card(&input2,(10,0));
    output2.append(&mut output21);
    outputs.push(output2);
    let mut outputa21 = almost_stupid_solve(&input2, (10,0));
    outputa2.append(&mut outputa21);
    outputs.push(outputa2);
    
    let (output30, input3) = preprocess2(&input);
    let mut output3 = output30;
    let mut outputa3:Vec<usize> = vec![0;output3.len()];
    outputa3.copy_from_slice(&output3[..]);
    let mut output31 = solve_with_one_card(&input3,(19,10));
    output3.append(&mut output31);
    outputs.push(output3);
    let mut outputa31 = almost_stupid_solve(&input3, (19,10));
    outputa3.append(&mut outputa31);
    outputs.push(outputa3);


    let (output40, input4) = preprocess3(&input);
    let mut output4 = output40;
    let mut outputa4:Vec<usize> = vec![0;output4.len()];
    outputa4.copy_from_slice(&output4[..]);
    let mut output41 = solve_with_one_card(&input4,(10,9));
    output4.append(&mut output41);
    eprintln!("output4 {}", compute_score(&output4));
    outputs.push(output4);
    let mut outputa41 = almost_stupid_solve(&input4, (10,9));
    outputa4.append(&mut outputa41);
    eprintln!("outputa4 {}", compute_score(&outputa4));
    outputs.push(outputa4);

    
    outputs.push(almost_stupid_solve(&input,(0,0)));
    let mut scores: Vec<usize> = Vec::new();
    for output in &outputs{
        scores.push(compute_score(&output));
    }
    let m = scores.iter().max().unwrap();
    let mut output: Vec<usize> = Vec::new();
    for i in 0..scores.len(){
        if scores[i] == *m{
            for t in &outputs[i]{
                output.push(*t);
            }
        }
    }
    output

}


// u: 100+x
// D: 200+x
// L: 300+x
// R: 400+x
// I: 1000
// O: 2000
// (x > 0)

#[fastout]
fn stdout_from_output(output: &Vec<usize>){
    for z in output{
        if z == &2000{
            print!("O");
        }else if z == &1000{
            print!("I");
        }else if z >= &400{
            for _ in 0..(z-400){
                print!("R");
            }
        }else if z >= &300{
            for _ in 0..(z-300){
                print!("L");
            }
        }else if z >= &200{
            for _ in 0..(z-200){
                print!("D");
            }
        }else if z >= &100{
            for _ in 0..(z-100){
                print!("U");
            }
        }
    }
    println!("");
}

// #[fastout]
fn run() {
    // 計測開始
    // get_time();
    let input = read_input();
    let out = solve(&input);
    eprintln!("{:?}",out );

    stdout_from_output(&out);
}
