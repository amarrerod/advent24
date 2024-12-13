use std::collections::{HashSet, VecDeque};
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_file(filename: &str) -> io::Result<Vec<Vec<u32>>> {
    let data_file = Path::new(file!()).parent().unwrap().join(filename);
    let file = File::open(data_file)?;
    let map = io::BufReader::new(file)
        .lines()
        .map(|l| {
            return l
                .unwrap()
                .chars()
                .map(|n| n.to_digit(10).unwrap())
                .collect::<Vec<u32>>();
        })
        .collect::<Vec<Vec<u32>>>();

    Ok(map)
}

fn get_neighbors(i: &u32, j: &u32, limit: &u32) -> Vec<(u32, u32)> {
    let right = if j + 1 < *limit {
        Some((*i, j + 1))
    } else {
        None
    };
    let left = if j >= &1 { Some((*i, j - 1)) } else { None };
    let up = if i >= &1 { Some((i - 1, *j)) } else { None };
    let down = if i + 1 < *limit {
        Some((i + 1, *j))
    } else {
        None
    };
    [right, left, up, down]
        .into_iter()
        .filter_map(|p| p)
        .collect()
}

fn get_trailheads(map: &Vec<Vec<u32>>) -> HashSet<(u32, u32)> {
    let rows = map.len() as u32;
    let cols = map.len() as u32;
    let mut heads: HashSet<(u32, u32)> = HashSet::new();
    for i in 0..rows {
        for j in 0..cols {
            if map[i as usize][j as usize] == 0 {
                if get_neighbors(&i, &j, &rows)
                    .iter()
                    .any(|&(x, y)| map[x as usize][y as usize] == 1)
                {
                    heads.insert((i, j));
                }
            }
        }
    }
    heads
}

fn calculate_hikings(head: &(u32, u32), map: &Vec<Vec<u32>>) -> Vec<(u32, u32)> {
    let rows = map.len() as u32;
    let _cols = rows;
    let mut reachable: Vec<(u32, u32)> = Vec::new();
    let mut stack: VecDeque<(u32, u32)> = VecDeque::new();
    stack.push_back(*head);
    while !stack.is_empty() {
        let (cx, cy): (u32, u32) = stack.pop_back().unwrap();
        if map[cx as usize][cy as usize] == 9 {
            reachable.push((cx, cy));
        }
        for (nx, ny) in get_neighbors(&cx, &cy, &rows).into_iter().rev() {
            if let Some(result) =
                map[nx as usize][ny as usize].checked_sub(map[cx as usize][cy as usize])
            {
                if result == 1 {
                    stack.push_back((nx, ny));
                }
            }
        }
    }
    reachable
}

pub fn solve_parts() {
    println!("{:} Day 10 {:}", "=".repeat(20), "=".repeat(20));

    let map = read_file("input.txt").unwrap();
    let heads = get_trailheads(&map);

    let solutions: (u32, u32) = heads
        .iter()
        .map(|head| {
            let reachables = calculate_hikings(head, &map);
            let l = reachables.len() as u32;
            (HashSet::<(u32, u32)>::from_iter(reachables).len() as u32, l)
        })
        .fold((0, 0), |(sx, sy), (x, y)| (sx + x, sy + y));
    println!("The solutions are: {:?}", solutions);
}
