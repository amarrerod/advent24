use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_file(filename: &str) -> io::Result<HashMap<u128, u128>> {
    let data_file = Path::new(file!()).parent().unwrap().join(filename);
    let file = File::open(data_file)?;
    let mut line = String::new();
    let _ = io::BufReader::new(file).read_line(&mut line);
    let mut numbers: HashMap<u128, u128> = HashMap::new();

    line.split_whitespace()
        .map(|x| x.parse::<u128>().unwrap())
        .for_each(|num| *numbers.entry(num).or_insert(0) += 1);
    Ok(numbers)
}

fn blink(stone: u128) -> Vec<u128> {
    if stone == 0 {
        return vec![1];
    }
    let s = stone.to_string();
    if s.len() % 2 == 0 {
        let left = &s[..s.len() / 2];
        let right = &s[s.len() / 2..];
        return vec![
            left.parse::<u128>().unwrap(),
            right.parse::<u128>().unwrap(),
        ];
    }
    return vec![stone * 2024];
}

pub fn solve_parts() {
    println!("{:} Day 11 {:}", "=".repeat(20), "=".repeat(20));

    let mut stones = read_file("input.txt").unwrap();
    for _ in 0..75 {
        let mut new_stones = HashMap::new();
        for (stone, counter) in stones.iter() {
            for child in blink(*stone) {
                *new_stones.entry(child).or_insert(0) += counter;
            }
        }
        stones = new_stones;
    }
    println!("The result is: {:}", stones.values().sum::<u128>());
}
