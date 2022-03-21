#![allow(non_snake_case)]

use num::ToPrimitive;
use petgraph::unionfind::UnionFind;
use proconio::*;
use proconio::marker::Bytes;
use std::collections::VecDeque;
use std::io::prelude::*;

const L: usize = 30;
const T: usize = 300;

#[macro_export]
macro_rules! mat {
	($($e:expr),*) => { Vec::from(vec![$($e),*]) };
	($($e:expr,)*) => { Vec::from(vec![$($e),*]) };
	($e:expr; $d:expr) => { Vec::from(vec![$e; $d]) };
	($e:expr; $d:expr $(; $ds:expr)+) => { Vec::from(vec![mat![$e $(; $ds)*]; $d]) };
}

pub fn get_time() -> f64 {
	static mut STIME: f64 = -1.0;
	let t = std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).unwrap();
	let ms = t.as_secs() as f64 + t.subsec_nanos() as f64 * 1e-9;
	unsafe {
		if STIME < 0.0 {
			STIME = ms;
		}
		ms - STIME
	}
}

#[derive(Debug, Clone)]
pub struct Place{
    N: usize,
    pets: Vec<(usize, usize, usize)>,
    M: usize,
    humans: Vec<(usize, usize)>,
    office: Vec<Vec<bool>>,
}


pub fn solve06(turn: usize, place: &mut Place, position_left_end: &mut Vec<bool>) -> Vec<u8>{
    let mut human_move = Vec::new();
    let mut new_place = place.clone();
    let mut scopes_of_responsibility = Vec::new();
    for i in 0..place.M{
        scopes_of_responsibility.push(L/place.M*i + 1);
    }
    scopes_of_responsibility.push(31);
    let draft = make_draft06();

    if turn < 200{
        for i in 0..place.M{
            let mut action = drawing_partition(&mut new_place, &draft, i, scopes_of_responsibility[i], scopes_of_responsibility[i+1]);
            if action == b'f'{
                action = solve06_01(i, &mut new_place, turn, position_left_end);
            }
            update_place(&mut new_place,place.humans[i] ,action);
            human_move.push(action);
        }
    }else if turn < 275{
        for i in 0..place.M{
            let action = solve06_02(i, &mut new_place, turn, position_left_end);
            update_place(&mut new_place, place.humans[i] ,action);
            human_move.push(action);
        }        
    }else if turn < 280{
        for i in 0..place.M{
            if i < 2{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,11)))
            }else if i < 4{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,20)))                
            }else if i%2 == 0{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,11)))
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,20)))
            }
        }
    }else{
        let dog = solve06_10(place) && (count_dogs(place) > 0);
        for i in 0..place.M{
            if i == 1{
                if dog{
                    human_move.push(b'r');
                    continue;
                }
            }else if i == 2{
                if dog{
                    human_move.push(b'l');
                    continue;
                }
            }
            if i < 2{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,11)))
            }else if i < 4{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,20)))                
            }else if i%2 == 0{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,11)))
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,20)))
            }

        }
    }
    human_move
}

pub fn solve06_01(human_number: usize, place: &mut Place, turn: usize, position_left_end: &mut Vec<bool>) -> u8{
    if human_number >= 4{
        return begin_with_a_single_step(place, place.humans[human_number], (15,15))
    }
    let left_end = vec![6, 9, 20, 25];
    let right_end = vec![6, 11, 22, 25];
    let (x,y) = place.humans[human_number];
    if !(place.humans[human_number].0 == 15 && left_end[human_number] <= y && y <= right_end[human_number]){
        return begin_with_a_single_step(place, (x,y), (15,left_end[human_number]))
    }
    let directions = match y{
        6 => 7,
        9 => 3,
        11 => 1,
        20 => 1,
        22 => 3,
        25 => 11,
        _ => 0,
    };
    let threshold_pets = place.N/5;
    if directions & 1 == 1{
        if check_positionability((x-1,y), &place){
            let (human_num, pet_num) = check_surrounded_nums(place,(x-1, y));
            if human_num == 0 && pet_num >= threshold_pets{
                return b'u'
            }
        }}
    if directions & 2 == 2{
        if check_positionability((x+1,y), &place){
            let (human_num, pet_num) = check_surrounded_nums(place,(x+1, y));
            if human_num == 0 && pet_num >= threshold_pets{
                return b'd'
            }
        }
    }
    if directions & 4 == 4{
        if check_positionability((x,y-1), &place){
            let (human_num, pet_num) = check_surrounded_nums(place,(x, y-1));
            if human_num == 0 && pet_num >= threshold_pets{
                return b'l'
            }
        }
    }
    if directions & 8 == 8{
        if check_positionability((x,y+1), &place){
            let (human_num, pet_num) = check_surrounded_nums(place,(x, y+1));
            if human_num == 0 && pet_num >= threshold_pets{
                return b'r'
            }
        }
    }
    if place.humans[human_number] == (15, left_end[human_number]){
        position_left_end[human_number] = true;
    }
    if place.humans[human_number] == (15, right_end[human_number]){
        position_left_end[human_number] = false;
    }
    if position_left_end[human_number]{
        begin_with_a_single_step(place, place.humans[human_number], (15, right_end[human_number]))
    }else{
        begin_with_a_single_step(place, place.humans[human_number], (15, left_end[human_number]))
    }
}

pub fn solve06_02(human_number: usize, place: &mut Place, turn: usize, position_left_end: &mut Vec<bool>) -> u8{
    if human_number >= 4{
        return begin_with_a_single_step(place, place.humans[human_number], (15,15))
    }
    let left_end = vec![6, 9, 20, 25];
    let right_end = vec![6, 11, 22, 25];
    let (x,y) = place.humans[human_number];
    if !(place.humans[human_number].0 == 15 && left_end[human_number] <= y && y <= right_end[human_number]){
        return begin_with_a_single_step(place, (x,y), (15,left_end[human_number]))
    }
    let directions = match y{
        6 => 7,
        9 => 3,
        11 => 1,
        20 => 1,
        22 => 3,
        25 => 11,
        _ => 0,
    };
    let mut _score = calcurate_score(place);
    let mut t = b'.';
    if directions & 1 == 1{
        if check_positionability((x-1,y), &place){
            let new_score = calcurate_new_score(place, (x-1,y));
            if _score < new_score{
                _score = new_score;
                t = b'u';
            }
        }}
    if directions & 2 == 2{
        if check_positionability((x+1,y), &place){
            let new_score = calcurate_new_score(place, (x+1,y));
            if _score < new_score{
                _score = new_score;
                t = b'd';
            }
        }
    }
    if directions & 4 == 4{
        if check_positionability((x,y-1), &place){
            let new_score = calcurate_new_score(place, (x,y-1));
            if _score < new_score{
                _score = new_score;
                t = b'l';
            }
        }
    }
    if directions & 8 == 8{
        if check_positionability((x,y+1), &place){
            let new_score = calcurate_new_score(place, (x,y+1));
            if _score < new_score{
                _score = new_score;
                t = b'r';
            }
        }
    }
    if t != b'.'{
        return t
    }

    if place.humans[human_number] == (15, left_end[human_number]){
        position_left_end[human_number] = true;
    }
    if place.humans[human_number] == (15, right_end[human_number]){
        position_left_end[human_number] = false;
    }
    if position_left_end[human_number]{
        begin_with_a_single_step(place, place.humans[human_number], (15, right_end[human_number]))
    }else{
        begin_with_a_single_step(place, place.humans[human_number], (15, left_end[human_number]))
    }
}

pub fn solve06_10(place: &mut Place) -> bool{
    check_positionability((15,12), place) && check_positionability((15,19), place)
}

pub fn count_dogs(place: &Place) -> usize{
    place.pets.iter().filter(|&(_,_,x)| *x == 4).count()
}

pub fn check_surrounded_nums(place: &Place, partition: (usize, usize)) -> (usize, usize){
    let (human_num, pet_num) = count_surrounded_nums(place);
    let mut new_place = place.clone();
    new_place.office[partition.0][partition.1] = false;
    let (new_human_num, new_pet_num) = count_surrounded_nums(&new_place);
    (new_human_num - human_num, new_pet_num - pet_num)
}

pub fn count_surrounded_nums(place: &Place) -> (usize, usize){
    let mut human_num = 0;
    let mut pet_num = 0;
    let forest = make_union_find_tree(place);
    for i in 0..place.M{
        let (x,y) = place.humans[i];
        if !forest.equiv(x*(L+1)+y, 15*(L+1)+15){
            human_num += 1;
        }
    }
    for i in 0..place.N{
        let (x,y,_) = place.pets[i];
        if !forest.equiv(x*(L+1)+y, 15*(L+1)+15){
            pet_num += 1;
        }
    }
    (human_num, pet_num)
}

pub fn make_union_find_tree(place: &Place) -> UnionFind<usize>{
    let mut forest = UnionFind::new((L+1)*(L+1));
    for x in 1..=L{
        for y in 1..=L{
            if !place.office[x][y]{
                continue;
            }
            if x > 1{
                if place.office[x-1][y]{
                    forest.union(x*(L+1)+y, (x-1)*(L+1)+y);
                }
            }
            if x < L{
                if place.office[x+1][y]{
                    forest.union(x*(L+1)+y, (x+1)*(L+1)+y);
                }
            }
            if y > 1{
                if place.office[x][y-1]{
                    forest.union(x*(L+1)+y, x*(L+1)+(y-1));
                }
            }
            if y < L{
                if place.office[x][y+1]{
                    forest.union(x*(L+1)+y, x*(L+1)+(y+1));
                }
            }
        }
    }
    forest
}



pub fn update_place(place: &mut Place, human: (usize, usize), action: u8){
    let (x,y) = human;
    if action == b'U'{
        place.humans.push((x-1,y))
    }else if action == b'D'{
        place.humans.push((x+1,y))
    }else if action == b'L'{
        place.humans.push((x,y-1))
    }else if action == b'R'{
        place.humans.push((x,y+1))
    }else if action == b'u'{
        place.office[x-1][y] = false;
    }else if action == b'd'{
        place.office[x+1][y] = false; 
    }else if action == b'l'{
        place.office[x][y-1] = false; 
    }else if action == b'r'{
        place.office[x][y+1] = false; 
    }
}

pub fn make_draft06() -> Vec<Vec<bool>>{
    let partitions = vec![
        (1, 5), (1, 10), (1, 16) , (1, 21) , (1, 26) ,
        (2, 5), (2, 10), (2, 16) , (2, 21) , (2, 26) ,
        (3, 5), (3, 10), (3, 16) , (3, 21) , (3, 26) ,
        (4, 5), (4, 10), (4, 16) , (4, 21) , (4, 26) ,
        (5, 5), (5, 10), (5, 16) , (5, 21) , (5, 26) ,
        (6, 5), (6, 10), (6, 16) , (6, 21) , (6, 26) ,
        (7, 5), (7, 10), (7, 16) , (7, 21) , (7, 26) ,
        (8, 5), (8, 10), (8, 16) , (8, 21) , (8, 26) ,
        (9, 5), (9, 10), (9, 16) , (9, 21) , (9, 26) ,
        (10, 5), (10, 10), (10, 16) , (10, 21) , (10, 26) ,
        (11, 5), (11, 10), (11, 16) , (11, 21) , (11, 26) ,
        (12, 6), (12, 10), (12, 16) , (12, 21) , (12, 25) ,
        (13, 7), (13, 8), (13, 10), (13, 16) , (13, 21) ,(13, 23),  (13, 24) ,
        (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 12), (14, 13), (14, 14), (14, 15), (14, 17), (14, 18), (14, 19), (14, 26), (14, 27), (14, 28), (14, 29), (14, 30),

        (16, 5), (16, 12), (16, 13), (16, 14), (16, 15), (16, 16), (16, 17), (16, 18), (16, 19), (16, 26),
        (17, 5) , (17, 7), (17, 8) , (17, 10) , (17, 21) , (17,23), (17, 24), (17, 26) ,
        (18, 5) , (18, 8) , (18, 11), (18, 12), (18, 13), (18, 14), (18, 15), (18, 17), (18, 18), (18, 19), (18, 20), (18, 23) , (18, 26) ,
        (19, 5) , (19, 8) , (19, 16) , (19, 23) , (19, 26) ,
        (20, 5) , (20, 9) , (20, 16) , (20, 22) , (20, 26) ,
        (21, 5) , (21, 10) , (21, 16) , (21, 21) , (21, 26) ,
        (22, 5) , (22, 10) , (22, 16) , (22, 21) , (22, 26) ,
        (23, 5) , (23, 10) , (23, 16) , (23, 21) , (23, 26) ,
        (24, 5) , (24, 10) , (24, 16) , (24, 21) , (24, 26) ,
        (25, 5) , (25, 10) , (25, 16) , (25, 21) , (25, 26) ,
        (26, 5) , (26, 10) , (26, 16) , (26, 21) , (26, 26) ,
        (27, 5) , (27, 10) , (27, 16) , (27, 21) , (27, 26) ,
        (28, 5) , (28, 10) , (28, 16) , (28, 21) , (28, 26) ,
        (29, 5) , (29, 10) , (29, 16) , (29, 21) , (29, 26) ,
        (30, 5) , (30, 10) , (30, 16) , (30, 21) , (30, 26) ,

    ];
    let mut draft = vec![vec![false; L+1]; L+1];
    for &(x,y) in &partitions{
        draft[x][y] = true;
    }
    draft
}

pub fn drawing_partition(place: &mut Place, draft: &Vec<Vec<bool>>, human_number: usize, left_end: usize, right_end: usize) -> u8{
    for x in 1..=L{
        for y in left_end..right_end{
            if !draft[x][y]{continue;}
            if !place.office[x][y]{continue;}
            if check_neighbor(place, place.humans[human_number], (x,y)){
                return try_place_partition(place.humans[human_number], (x,y), place)
            }
            return begin_with_a_single_step_neighbor(place, place.humans[human_number], (x,y))
        }
    }
    b'f'
}

pub fn begin_with_a_single_step_neighbor(place: &Place, start: (usize, usize), goal: (usize, usize)) -> u8{
    let neighbor_goal = nearest_neighbor(place, start, goal);
    begin_with_a_single_step(place, start, neighbor_goal)
}

pub fn nearest_neighbor(place: &Place, start: (usize, usize), goal: (usize, usize)) -> (usize, usize){
    let unreached = (L+1)*(L+1)+1;
    let mut distance = vec![vec![unreached; L+1];L+1];
    let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
    queue.push_back(start);
    distance[goal.0][goal.1] = 0;
    while let Some((x,y)) = queue.pop_front(){
        let t = distance[x][y];
        if x > 1{
            if place.office[x-1][y] && distance[x-1][y] == unreached{
                distance[x-1][y] = t+1;
                queue.push_back((x-1,y));
                if check_neighbor(place, (x-1, y), goal){
                    return (x-1,y)
                }
            }
        }
        if x < L{
            if place.office[x+1][y] && distance[x+1][y] == unreached{
                distance[x+1][y] = t+1;
                queue.push_back((x+1, y));
                if check_neighbor(place, (x+1, y), goal){
                    return (x+1,y)
                }
            }
        }
        if y > 1{
            if place.office[x][y-1] && distance[x][y-1] == unreached{
                distance[x][y-1] = t+1;
                queue.push_back((x,y-1));
                if check_neighbor(place, (x, y-1), goal){
                    return (x,y-1)
                }
            }
        }
        if y < L{
            if place.office[x][y+1] && distance[x][y+1] == unreached{
                distance[x][y+1] = t+1;
                queue.push_back((x,y+1));
                if check_neighbor(place, (x, y-1), goal){
                    return (x,y-1)
                }
            }
        }
    }
    goal
}


pub fn check_neighbor(place: &Place, x:(usize, usize), y:(usize, usize)) -> bool{
    if ((x.0 as i64) - (y.0 as i64)).abs() == 1 && ((x.1 as i64) - (y.1 as i64)).abs() == 0{
        return true
    }
    if ((x.0 as i64) - (y.0 as i64)).abs() == 0 && ((x.1 as i64) - (y.1 as i64)).abs() == 1{
        return true
    }
    false
}


fn main() {
	get_time();
	let mut stdin: source::line::LineSource<std::io::BufReader<std::io::Stdin>> = proconio::source::line::LineSource::new(std::io::BufReader::new(std::io::stdin()));
	input!(from &mut stdin, N: usize, pets: [(usize, usize, usize); N], M: usize, humans: [(usize, usize); M]);
    let mut office = vec![vec![true; L+1]; L+1];
    for i in 0..=L{
        office[0][i] = false;
        office[i][0] = false;
    }
    let mut place = Place{N, pets, M, humans, office};
    // let t: Vec<u8> = (0..M).map(|_| b'.').collect();
    let mut position_left_end = vec![false; 4];
    for i in 0..T{
        // println!("{}", t.iter().map(|&s| s as char).collect::<String>());
        let human_movement = solve06(i, &mut place, &mut position_left_end);
        give_order_to_humans(&human_movement, &mut place);
        std::io::stdout().flush().unwrap();
        input!(from &mut stdin, pets_move: [Bytes; N]);
        move_pets(&mut place, &pets_move)
    }

}

pub fn calcurate_new_score(place: &Place, partition: (usize, usize)) -> i64{
    let mut new_place = place.clone();
    new_place.office[partition.0][partition.1] = false;
    calcurate_score(&new_place)
}

pub fn calcurate_score(place: &Place) -> i64{
    let mut forest = UnionFind::new((L+1)*(L+1));
    for x in 1..=L{
        for y in 1..=L{
            if !place.office[x][y]{
                continue;
            }
            if x > 1{
                if place.office[x-1][y]{
                    forest.union(x*(L+1)+y, (x-1)*(L+1)+y);
                }
            }
            if x < L{
                if place.office[x+1][y]{
                    forest.union(x*(L+1)+y, (x+1)*(L+1)+y);
                }
            }
            if y > 1{
                if place.office[x][y-1]{
                    forest.union(x*(L+1)+y, x*(L+1)+(y-1));
                }
            }
            if y < L{
                if place.office[x][y+1]{
                    forest.union(x*(L+1)+y, x*(L+1)+(y+1));
                }
            }
      
        }
    }
    let mut area_count = vec![0; (L+1)*(L+1)];
    for x in 1..=L{
        for y in 1..=L{
            if place.office[x][y]{
                area_count[forest.find(x*(L+1)+y)] += 1;
            }
        }
    }
    let mut pets_count = vec![0; (L+1)*(L+1)];
    for &(x, y, _) in place.pets.iter(){
        pets_count[forest.find(x*(L+1)+y)] += 1;
    }
    let mut s: f64 = 0.0;
    let p: f64 = 100000000.0;
    for &(x, y) in place.humans.iter(){
        s += p*(area_count[forest.find(x*(L+1)+y)] as f64)/(2_i32.pow(pets_count[forest.find(x*(L+1)+y)] as u32) as f64)
    }
    (s/((900*place.M) as f64)).round().to_i64().unwrap()
}


pub fn move_pets(place: &mut Place, pets_move: &Vec<Vec<u8>>){
    for i in 0..place.N{
        let (mut x, mut y, t) = place.pets[i];
        for &direction in pets_move[i].iter(){
            if direction == b'U'{
                x -= 1;
            }else if direction == b'D'{
                x += 1;
            }else if direction == b'L'{
                y -= 1;
            }else if direction == b'R'{
                y += 1;
            }
        }
        place.pets[i] = (x, y, t)
    }
}

pub fn give_order_to_humans(human_movement: &Vec<u8>, place: &mut Place){
    for i in 0..place.M{
        let (x,y) = place.humans[i];
        if human_movement[i] == b'U'{
            place.humans[i].0 -= 1;
        }else if human_movement[i] == b'D'{
            place.humans[i].0 += 1;
        }else if human_movement[i] == b'L'{
            place.humans[i].1 -= 1;
        }else if human_movement[i] == b'R'{
            place.humans[i].1 += 1;
        }else if human_movement[i] == b'u'{
            place.office[x-1][y] = false;
        }else if human_movement[i] == b'd'{
            place.office[x+1][y] = false; 
        }else if human_movement[i] == b'l'{
            place.office[x][y-1] = false; 
        }else if human_movement[i] == b'r'{
            place.office[x][y+1] = false; 
        }
    }
    println!("{}", human_movement.iter().map(|&s| s as char).collect::<String>())
}

pub fn begin_with_a_single_step(place: &Place, now: (usize, usize), goal: (usize, usize)) -> u8{
    if now == goal{
        return b'.'
    }
    let unreached = (L+1)*(L+1)+1;
    let mut distance = vec![vec![unreached; L+1];L+1];
    let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
    queue.push_back(goal);
    distance[goal.0][goal.1] = 0;
    while let Some((x,y)) = queue.pop_front(){
        let t = distance[x][y];
        if x > 1{
            if place.office[x-1][y] && distance[x-1][y] == unreached{
                distance[x-1][y] = t+1;
                queue.push_back((x-1,y));
                if now == (x-1,y){
                    return b'D'
                }
            }
        }
        if x < L{
            if place.office[x+1][y] && distance[x+1][y] == unreached{
                distance[x+1][y] = t+1;
                queue.push_back((x+1, y));
                if now == (x+1,y){
                    return b'U'
                }

            }
        }
        if y > 1{
            if place.office[x][y-1] && distance[x][y-1] == unreached{
                distance[x][y-1] = t+1;
                queue.push_back((x,y-1));
                if now == (x, y-1){
                    return b'R'
                }
            }
        }
        if y < L{
            if place.office[x][y+1] && distance[x][y+1] == unreached{
                distance[x][y+1] = t+1;
                queue.push_back((x,y+1));
                if now == (x, y+1){
                    return b'L'
                }
            }
        }
    }
    // connected を仮定
    b'.'
}

pub fn try_place_partition(human_place: (usize, usize), placement: (usize, usize), place: &Place) -> u8{
    if check_positionability(placement, place){
        if human_place.0 - 1 == placement.0{
            return b'u'
        }else if human_place.0 + 1 == placement.0{
            return b'd'
        }else if human_place.1 - 1 == placement.1{
            return b'l'
        }else if human_place.1 + 1 == placement.1{
            return b'r'
        }
    }
    b'.'
}

pub fn check_positionability(placement: (usize, usize), place: &Place) -> bool{
    if !place.office[placement.0][placement.1]{
        return false
    }
    let px = placement.0 as i32;
    let py = placement.1 as i32;
    for &(x,y,_) in place.pets.iter(){
        if x as i32 == px && y as i32 == py{
            return false
        }
        if ((x as i32) - px).abs() == 0 && ((y as i32) - py).abs() == 1{
            return false
        }
        if ((x as i32) - px).abs() == 1 && ((y as i32) - py).abs() == 0{
            return false
        }
    }
    for &(x,y) in place.humans.iter(){
        if x as i32 == px && y as i32 == py{
            return false
        }
    }
    true
}


















pub fn solve01(turn: usize, place: &mut Place) -> Vec<u8>{
    let mut human_move = Vec::new();
    if turn < L+1{
        for i in 0..place.M{
            human_move.push(begin_with_a_single_step(place, place.humans[i], (L/2,L/2)))
        }
    }else if turn < T-10{
        for i in 0..place.M{
            if i == 0{
                human_move.push(solve_01_01(i, place));
            }else if i == 1{
                human_move.push(solve_01_02(i, place));
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (28,28)))
            }
        }
    }else{
        for i in 0..place.M{
            if i == 0{
                human_move.push(try_place_partition((28,28), (28,29), place));
            }else if i == 1{
                human_move.push(try_place_partition((28,28), (29,28), place));
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (28,28)))
            }
        }
    }
    human_move
}

pub fn solve_01_01( human_number: usize, place: &mut Place) -> u8{
    let human_place = place.humans[human_number];
    for x in 1..=29{
        if x == 28{continue;}
        if !place.office[x][29]{continue;}
        if human_place == (x, 28){
            return try_place_partition((x,28), (x,29), place)
        }
        return begin_with_a_single_step(place, human_place, (x, 28))
    }
    begin_with_a_single_step(place, human_place, (28, 28))
}

pub fn solve_01_02(human_number: usize, place: &mut Place) -> u8{
    let human_place = place.humans[human_number];
    for y in 1..=27{
        if !place.office[29][y]{continue;}
        if human_place == (28, y){
            return try_place_partition((28,y), (29,y), place)
        }
        return begin_with_a_single_step(place, human_place, (28, y))
    }
    begin_with_a_single_step(place, human_place, (28, 28))
}



pub fn solve02(turn: usize, place: &mut Place) -> Vec<u8>{
    let mut human_move = Vec::new();
    if turn <= L*2{
        for i in 0..place.M{
            if i == 0{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (14,29)))
            }else if i == 1{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (17,29)))
            }else if i%2 == 0{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (1,30)))
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (30,30)))
            }
        }
    }else if turn < T-10{
        for i in 0..place.M{
            if i == 0{
                human_move.push(solve_02_01(i, place));
            }else if i == 1{
                human_move.push(solve_02_02(i, place));
            }else if i%2 == 0{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (1,30)))
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (30,30)))
            }
        }
    }else{
        for i in 0..place.M{
            if i == 0{
                human_move.push(try_place_partition((1,30), (2,30), place));
            }else if i == 1{
                human_move.push(try_place_partition((30,30), (29,30), place));
            }else{
                human_move.push(b'.')
            }
        }
    }
    human_move
}

pub fn solve_02_01(human_number: usize, place: &mut Place) -> u8{
    let human_place = place.humans[human_number];
    for x in (1..15).rev(){
        if !place.office[x+1][29]{continue;}
        if human_place == (x, 29){
            return try_place_partition(human_place, (x+1, 29), place)
        }
        return begin_with_a_single_step(place, human_place, (x, 29))
    }
    begin_with_a_single_step(place, human_place, (1, 30))
}

pub fn solve_02_02(human_number: usize, place: &mut Place) -> u8{
    let human_place = place.humans[human_number];
    for x in 17..=30{
        if !place.office[x-1][29]{continue;}
        if human_place == (x, 29){
            return try_place_partition(human_place, (x-1, 29), place)
        }
        return begin_with_a_single_step(place, human_place, (x, 29))
    }
    begin_with_a_single_step(place, human_place, (30, 30))
}

pub fn solve03(turn: usize, place: &mut Place) -> Vec<u8>{
    let mut human_move = Vec::new();
    if turn <= L*2{
        for i in 0..place.M{
            if i == 0{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (2,29)))
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (1,30)))
            }
        }
    }else if turn < T-40{
        for i in 0..place.M{
            if i == 0{
                human_move.push(solve_03_01(i, place));
            }else{
                human_move.push(b'.')
            }                
        }
    }else if turn < T - 10{
        for i in 0..place.M{
            human_move.push(begin_with_a_single_step(place, place.humans[i], (30,29)))
        }
    }else{
        for i in 0..place.M{
            if i == 0{
                human_move.push(try_place_partition((30,29), (30,30), place));
            }else{
                human_move.push(b'.')
            }                
        }        
    }
    human_move
}

pub fn solve_03_01(human_number: usize, place: &mut Place) -> u8{
    let human_place = place.humans[human_number];
    for x in 2..=30{
        if !place.office[x-1][29]{continue;}
        if human_place == (x, 29){
            return try_place_partition(human_place, (x-1, 29), place)
        }
        return begin_with_a_single_step(place, human_place, (x, 29))
    }
    begin_with_a_single_step(place, human_place, (1, 30))
}

pub fn solve04(turn: usize, place: &mut Place) -> Vec<u8>{
    let mut human_move = Vec::new();
    if turn <= L*2{
        for i in 0..place.M{
            if i == 0{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (14,29)))
            }else if i == 1{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (17,29)))
            }else if i%2 == 0{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (1,30)))
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (30,30)))
            }
        }
    }else if turn < 90{
        for i in 0..place.M{
            if i == 0{
                human_move.push(solve_02_01(i, place));
            }else if i == 1{
                human_move.push(solve_02_02(i, place));
            }else if i%2 == 0{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (1,30)))
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (30,30)))
            }
        }
    }else if turn < 95{
        for i in 0..place.M{
            if i == 0{
                human_move.push(try_place_partition((1,30), (2,30), place));
            }else if i == 1{
                human_move.push(try_place_partition((30,30), (29,30), place));
            }else{
                human_move.push(b'.')
            }
        }
    }else if turn < 110{
        for i in 0..place.M{
            if i == 0{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (2,6)))
            }else if i == 1{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (29,12)))
            }else if i == 2{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (2,18)))
            }else if i == 3{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (29,24)))
            }else if i == 4{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (14,26)))
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,28)))
            }
        }
    }else if turn < 250{
        for i in 0..place.M{
            if i == 0{
                human_move.push(solve_04_01(place, i, 6))
            }else if i == 1{
                human_move.push(solve_04_02(place, i, 12))
            }else if i == 2{
                human_move.push(solve_04_01(place, i, 18))
            }else if i == 3{
                human_move.push(solve_04_02(place, i, 24))
            }else if i == 4{
                human_move.push(solve_04_03(place, i, 28))
            }
            else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,15)))
            }
        }
    }else{
        let mut temp_place = place.clone();
        for i in 0..place.M{
            if i < 5{
                let z = match i{
                    0 => 6,
                    1 => 12,
                    2 => 18,
                    3 => 24,
                    4 => 28,
                    _ => 50,
                };
                let mut current_score = calcurate_score(place);
                let mut partition = place.humans[i];
                if check_positionability((14, z), &temp_place){
                    let new_score = calcurate_new_score(&temp_place, (14,z));
                    if current_score < new_score{
                        current_score = new_score;
                        partition = (14,z)
                    }
                }
                if check_positionability((16, z), &temp_place){
                    let new_score = calcurate_new_score(&temp_place, (16,z));
                    if current_score < new_score{
                        current_score = new_score;
                        partition = (16,z)
                    }
                }
                human_move.push(try_place_partition(place.humans[i], partition, place));
                if place.humans[i] != partition{
                    temp_place.office[partition.0][partition.1] = false;
                }
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,15)))
            }
        }
    }
    human_move
}

pub fn solve_04_01(place: &mut Place, human_number: usize,  axis: usize) -> u8{
    for x in 1..=14{
        if !place.office[x][axis]{continue;}
        if place.humans[human_number] == (x+1, axis){
            return try_place_partition((x+1, axis), (x, axis), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (x+1, axis));
    }
    for y in ((axis-4)..axis).rev(){
        if !place.office[14][y]{continue;}
        if place.humans[human_number] == (14, y-1){
            return try_place_partition((14, y-1), (14, y), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (14, y-1));        
    }
    for x in (16..=30).rev(){
        if !place.office[x][axis]{continue;}
        if place.humans[human_number] == (x-1, axis){
            return try_place_partition((x-1, axis), (x, axis), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (x-1, axis));
    }
    for y in ((axis-4)..axis).rev(){
        if !place.office[16][y]{continue;}
        if place.humans[human_number] == (16, y-1){
            return try_place_partition((16, y-1), (16, y), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (16, y-1));        
    }
    begin_with_a_single_step(place, place.humans[human_number], (15, axis-5))
}

pub fn solve_04_02(place: &mut Place, human_number: usize,  axis: usize) -> u8{
    for x in (16..=30).rev(){
        if !place.office[x][axis]{continue;}
        if place.humans[human_number] == (x-1, axis){
            return try_place_partition((x-1, axis), (x, axis), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (x-1, axis));
    }
    for y in ((axis-4)..axis).rev(){
        if !place.office[16][y]{continue;}
        if place.humans[human_number] == (16, y-1){
            return try_place_partition((16, y-1), (16, y), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (16, y-1));        
    }

    for x in 1..=14{
        if !place.office[x][axis]{continue;}
        if place.humans[human_number] == (x+1, axis){
            return try_place_partition((x+1, axis), (x, axis), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (x+1, axis));
    }
    for y in ((axis-4)..axis).rev(){
        if !place.office[14][y]{continue;}
        if place.humans[human_number] == (14, y-1){
            return try_place_partition((14, y-1), (14, y), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (14, y-1));        
    }
    begin_with_a_single_step(place, place.humans[human_number], (15, axis-5))
}

pub fn solve_04_03(place: &mut Place, human_number: usize,  axis: usize) -> u8{
    for y in (axis-3)..axis{
        if !place.office[14][y]{continue;}
        if place.humans[human_number] == (14, y+1){
            return try_place_partition((14, y+1), (14, y), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (14, y+1));        
    }

    for y in (axis-3)..axis{
        if !place.office[16][y]{continue;}
        if place.humans[human_number] == (16, y+1){
            return try_place_partition((16, y+1), (16, y), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (16, y+1));        
    }

    begin_with_a_single_step(place, place.humans[human_number], (15, axis))
}

pub fn solve05(turn: usize, place: &mut Place) -> Vec<u8>{
    let mut human_move = Vec::new();
    if turn <= L*2{
        for i in 0..place.M{
            if i == 0{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (2,6)))
            }else if i == 1{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (29,12)))
            }else if i == 2{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (2,18)))
            }else if i == 3{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (29,24)))
            }else if i == 4{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (14,26)))
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,i%5*6+1)))
            }
        }
    }else{
        let mut temp_place = place.clone();
        for i in 0..place.M{
            if i < 5{
                let z = match i{
                    0 => 1,
                    1 => 7,
                    2 => 13,
                    3 => 19,
                    4 => 30,
                    _ => 50,
                };
                if i < 4{
                    if !place.office[14][z+1] && !place.office[16][z+1] && place.humans[i] == (15,z){
                    }else{
                        if i == 0{
                            human_move.push(solve_04_01(place, i, 6))
                        }else if i == 1{
                            human_move.push(solve_04_02(place, i, 12))
                        }else if i == 2{
                            human_move.push(solve_04_01(place, i, 18))
                        }else if i == 3{
                            human_move.push(solve_04_02(place, i, 24))
                        }
                        continue;
                    }
                }else if i == 4{
                    if !place.office[14][z-1] && !place.office[16][z-1] && place.humans[i] == (15,z){
                    }else{
                        human_move.push(solve_05_03(place, i, 30));
                        continue;
                    }
                }
 
                let mut current_score = calcurate_score(place);
                let mut partition = place.humans[i];
                if check_positionability((14, z), &temp_place){
                    let new_score = calcurate_new_score(&temp_place, (14,z));
                    if current_score < new_score{
                        current_score = new_score;
                        partition = (14,z)
                    }
                }
                if check_positionability((16, z), &temp_place){
                    let new_score = calcurate_new_score(&temp_place, (16,z));
                    if current_score < new_score{
                        current_score = new_score;
                        partition = (16,z)
                    }
                }
                human_move.push(try_place_partition(place.humans[i], partition, place));
                if place.humans[i] != partition{
                    temp_place.office[partition.0][partition.1] = false;
                }
            }else{
                human_move.push(begin_with_a_single_step(place, place.humans[i], (15,i%5*6+1)))
            }
        }
    }
    human_move
}

pub fn solve_05_03(place: &mut Place, human_number: usize,  axis: usize) -> u8{
    for y in (axis-5)..axis{
        if !place.office[14][y]{continue;}
        if place.humans[human_number] == (14, y+1){
            return try_place_partition((14, y+1), (14, y), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (14, y+1));        
    }

    for y in (axis-5)..axis{
        if !place.office[16][y]{continue;}
        if place.humans[human_number] == (16, y+1){
            return try_place_partition((16, y+1), (16, y), place)
        }
        return begin_with_a_single_step(place, place.humans[human_number], (16, y+1));        
    }

    begin_with_a_single_step(place, place.humans[human_number], (15, axis))
}

